import random
from PySide6.QtCore import QObject, QTimer
from PySide6.QtWidgets import QMessageBox

from database.crud_partida import (buscar_pedras_por_nivel,
    criar_partida,
    finalizar_partida,
    atualizar_pontuacao_usuario,
    incrementar_partidas_ganhas,
)
from ui.components.layout_pedra import LayoutPedra
from ui.modals.modal_resultado_partida import ModalResultado

REACOES = {
    "Ácido":  "Ácido",
    "Base":   "Base",
    "Sal":    "Sal",
    "Óxido":  "Óxido",
}

class ControllerTelaPartida(QObject):
    def __init__(self, tela, nivel: str, id_usuario: int, tela_aluno):
        super().__init__()
        self.tela       = tela
        self.nivel      = nivel
        self.id_usuario = id_usuario
        self.tela_aluno = tela_aluno

        self.pontuacao     = 0
        self.total_jogadas = 0
        self.segundos      = 0

        self.pedra_selecionada = None
        self.mao   = []
        self.monte = []
        self.mesa  = []

        self._iniciar_jogo()

        self.timer = QTimer()
        self.timer.timeout.connect(self._tick)
        self.timer.start(1000)

        self.tela.botao_comprar.clicked.connect(self._comprar_pedra)
        self.tela.botao_retornar.clicked.connect(self._confirmar_saida)

    def _iniciar_jogo(self):
        pecas = list(buscar_pedras_por_nivel(self.nivel))
        print("Peças carregadas:", pecas[:3])  # mostra as 3 primeiras
        random.shuffle(pecas)
        self.mao   = pecas[:7]
        self.monte = pecas[7:]
        self.id_partida = criar_partida(self.id_usuario)
        self._renderizar_mao()
        self._atualizar_cards()

    def _renderizar_mao(self):
        while self.tela.layout_mao.count():
            item = self.tela.layout_mao.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for id_peca, esq, tipo_esq, dir_, tipo_dir in self.mao:
            print(f"Renderizando: esq={esq}, tipo_esq={tipo_esq}, dir={dir_}, tipo_dir={tipo_dir}")  # ← aqui
            widget = LayoutPedra(
                id_lado_esquerdo=esq,
                id_lado_direito=dir_,
                tipo_esquerdo=tipo_esq,
                tipo_direito=tipo_dir,
            )
            widget.pedra_clicada.connect(self._selecionar_pedra)
            self.tela.layout_mao.addWidget(widget)

        self.tela.botao_comprar.setEnabled(len(self.monte) > 0)

    def _atualizar_cards(self):
        m = self.segundos // 60
        s = self.segundos % 60
        self.tela.card_pontuacao.atualizar_conteudo(
            f"Pontos: {self.pontuacao}\nTempo: {m:02d}:{s:02d}\nJogadas: {self.total_jogadas}"
        )

    def _tick(self):
        self.segundos += 1
        self._atualizar_cards()

    def _selecionar_pedra(self, widget: LayoutPedra):
    # Ignora se o widget já foi destruído
        try:    
            _ = widget.selecionada
        except RuntimeError:
            return

        if self.pedra_selecionada and self.pedra_selecionada is not widget:
            try:
                self.pedra_selecionada.desselecionar()
            except RuntimeError:
                pass
            self.pedra_selecionada = None

        if widget.selecionada:
            widget.desselecionar()
            self.pedra_selecionada = None
        else:
            widget.selecionar()
            self.pedra_selecionada = widget
            self._tentar_jogar(widget)

    def _tentar_jogar(self, widget: LayoutPedra):
        tipo_esq = widget.tipo_esquerdo
        tipo_dir = widget.tipo_direito

        if not self.mesa:
            self._jogar_pedra(widget, lado_encaixe=None)
            return

        tipo_ponta_dir = self.mesa[-1][4]
        tipo_ponta_esq = self.mesa[0][2]

        if tipo_esq == tipo_ponta_dir:
         self._jogar_pedra(widget, lado_encaixe="direita")
        elif tipo_dir == tipo_ponta_esq:
            self._jogar_pedra(widget, lado_encaixe="esquerda")
        else:
            self._jogada_invalida(widget, tipo_ponta_dir, tipo_ponta_esq, tipo_ponta_dir, tipo_ponta_esq)

    def _jogar_pedra(self, widget: LayoutPedra, lado_encaixe):
        esq      = widget.id_lado_esquerdo
        tipo_esq = widget.tipo_esquerdo
        dir_     = widget.id_lado_direito
        tipo_dir = widget.tipo_direito

        self.mao = [
        p for p in self.mao
        if not (p[1] == widget.id_lado_esquerdo and p[3] == widget.id_lado_direito)
        ]

        if lado_encaixe == "esquerda":
            self.mesa.insert(0, (None, dir_, tipo_dir, esq, tipo_esq))
        else:
            self.mesa.append((None, esq, tipo_esq, dir_, tipo_dir))

        self.tela.mesa.adicionar_pedra(
        LayoutPedra(
            id_lado_esquerdo=esq,
            id_lado_direito=dir_,
            tipo_esquerdo=tipo_esq,
            tipo_direito=tipo_dir,
        )
        )

        self.pontuacao     += 10
        self.total_jogadas += 1
        self.pedra_selecionada = None

        self.tela.card_dicas.atualizar_conteudo("Jogada válida! +10 pontos.")
        self._renderizar_mao()
        self._atualizar_cards()

        if not self.mao:
            self._finalizar_partida()

    def _jogada_invalida(self, widget, tipo_ponta_dir, tipo_ponta_esq, oposto_dir, oposto_esq):
        self.pontuacao = max(0, self.pontuacao - 10)
        widget.desselecionar()
        self.pedra_selecionada = None

        self.tela.card_dicas.atualizar_conteudo(
        f"Jogada inválida! -10 pontos.\n"
        f"Ponta direita ({tipo_ponta_dir}) precisa de: {oposto_dir}\n"
        f"Ponta esquerda ({tipo_ponta_esq}) precisa de: {oposto_esq}"
        )
        self._atualizar_cards()
        self._verificar_jogo_travado()

    def _existe_jogada_possivel(self):
        if not self.mesa:
            return True  

        tipo_ponta_dir = self.mesa[-1][4]
        tipo_ponta_esq = self.mesa[0][2]

        for _, esq, tipo_esq, dir_, tipo_dir in self.mao:
            if tipo_esq == tipo_ponta_dir or tipo_dir == tipo_ponta_esq:
                return True
        return False
    
    def _verificar_jogo_travado(self):
        if not self.monte and not self._existe_jogada_possivel():
            self.timer.stop()
            finalizar_partida(self.id_partida)

            QMessageBox.information(
                self.tela,
                "Partida travada",
                "Não há mais jogadas possíveis e o monte está vazio.\nA partida foi finalizada.",
            )

            m = self.segundos // 60
            s = self.segundos % 60

            modal = ModalResultado(
                pontuacao=self.pontuacao,
                tempo=f"{m:02d}:{s:02d}",
                total_jogadas=self.total_jogadas,
                parent=self.tela,
        )
        modal.retornar_tela_aluno.connect(self._voltar_tela_aluno)
        modal.exec()

    def _comprar_pedra(self):
        if not self.monte:
            self.tela.botao_comprar.setEnabled(False)
            self._verificar_jogo_travado()
            return

        peca = self.monte.pop(0)
        self.mao.append(peca)
        self._renderizar_mao()
        self.tela.card_dicas.atualizar_conteudo("Pedra comprada do monte.")
        self._atualizar_cards()

    def _confirmar_saida(self):
        resp = QMessageBox.question(
            self.tela,
            "Sair da partida",
            "Deseja sair? O progresso será perdido.",
        )
        if resp == QMessageBox.Yes:
            self.timer.stop()
            finalizar_partida(self.id_partida)
            self.tela.close()
            self.tela_aluno.show()

    def _finalizar_partida(self):
        self.timer.stop()
        finalizar_partida(self.id_partida)
        atualizar_pontuacao_usuario(self.id_usuario, self.pontuacao)
        incrementar_partidas_ganhas(self.id_usuario)

        m = self.segundos // 60
        s = self.segundos % 60

        modal = ModalResultado(
            pontuacao=self.pontuacao,
            tempo=f"{m:02d}:{s:02d}",
            total_jogadas=self.total_jogadas,
            parent=self.tela,
        )
        modal.retornar_tela_aluno.connect(self._voltar_tela_aluno)
        modal.exec()

    def _voltar_tela_aluno(self):
        self.tela.close()
        self.tela_aluno.show()