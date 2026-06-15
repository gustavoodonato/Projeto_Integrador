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

        for id_peca, esq, dir_ in self.mao:
            widget = LayoutPedra(id_lado_esquerdo=esq, id_lado_direito=dir_)
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
        esq  = widget.id_lado_esquerdo
        dir_ = widget.id_lado_direito

        if not self.mesa:
            self._jogar_pedra(widget)
            return

        ponta_dir = self.mesa[-1][2]
        ponta_esq = self.mesa[0][1]

        if esq == ponta_dir or dir_ == ponta_dir or esq == ponta_esq or dir_ == ponta_esq:
            self._jogar_pedra(widget)
        else:
            self._jogada_invalida(widget)

    def _jogar_pedra(self, widget: LayoutPedra):
        esq  = widget.id_lado_esquerdo
        dir_ = widget.id_lado_direito

        self.mao  = [p for p in self.mao if not (p[1] == esq and p[2] == dir_)]
        self.mesa.append((None, esq, dir_))
        self.tela.mesa.adicionar_pedra(
            LayoutPedra(id_lado_esquerdo=esq, id_lado_direito=dir_)
        )

        self.pontuacao     += 10
        self.total_jogadas += 1
        self.pedra_selecionada = None

        self.tela.card_dicas.atualizar_conteudo("Jogada válida! +10 pontos.")
        self._renderizar_mao()
        self._atualizar_cards()

        if not self.mao:
            self._finalizar_partida()

    def _jogada_invalida(self, widget: LayoutPedra):
        self.pontuacao = max(0, self.pontuacao - 10)
        widget.desselecionar()
        self.pedra_selecionada = None

        ponta_dir = self.mesa[-1][2] if self.mesa else "?"
        self.tela.card_dicas.atualizar_conteudo(
            f"Jogada inválida! -10 pontos.\n"
            f"A pedra precisa ter '{ponta_dir}' em um dos lados."
        )
        self._atualizar_cards()

    def _comprar_pedra(self):
        if not self.monte:
            self.tela.botao_comprar.setEnabled(False)
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