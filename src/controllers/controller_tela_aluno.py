from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox
from controllers.controller_tela_partida import ControllerTelaPartida
from ui.screens.tela_partida import TelaPartida

niveis_de_dificuldade = {
    "Nível Fácil":   "facil",
    "Nível Médio":   "medio",
    "Nível Difícil": "dificil",
}

class ControllerTelaAluno(QObject):
    def __init__(self, tela, id_usuario: int):
        super().__init__()
        self.tela = tela
        self.id_usuario = id_usuario
        self.nivel_selecionado = None

        self.tela.card_facil.selecionado.connect(self._selecionar_facil)
        self.tela.card_medio.selecionado.connect(self._selecionar_medio)
        self.tela.card_dificil.selecionado.connect(self._selecionar_dificil)

        self.tela.botao_iniciar.clicked.connect(self._iniciar_partida)

    def _selecionar_facil(self):
        self.nivel_selecionado = "Nível Fácil"

    def _selecionar_medio(self):
        self.nivel_selecionado = "Nível Médio"

    def _selecionar_dificil(self):
        self.nivel_selecionado = "Nível Difícil"

    def _iniciar_partida(self):
        if self.nivel_selecionado is None:
            QMessageBox.warning(self.tela, "Atenção", "Selecione um nível de dificuldade para iniciar a partida.")
            return

        nivel_db = niveis_de_dificuldade[self.nivel_selecionado]
        self.tela_partida = TelaPartida(nivel=nivel_db)
        self.controller_partida = ControllerTelaPartida(
            tela = self.tela_partida,
            nivel = nivel_db,
            id_usuario = self.id_usuario,
            tela_aluno = self.tela,
        )
        self.tela_partida.show()
        self.tela.hide()