import sys
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QApplication
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont
from ui.components.botao_retornar import BotaoRetornar


class ModalResultado(QDialog):
    retornar_tela_aluno = Signal()

    def __init__(self, pontuacao: int, tempo: str, total_jogadas: int, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Resultado da Partida")
        self.setFixedSize(400, 300)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setStyleSheet("background-color: white;")
        self._build_ui(pontuacao, tempo, total_jogadas)

    def _build_ui(self, pontuacao, tempo, total_jogadas):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(16)

        titulo = QLabel("Partida Finalizada!")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setFont(QFont("Verdana", 14, QFont.Bold))
        titulo.setStyleSheet("""
            background-color: #911712;
            color: white;
            border-radius: 8px;
            padding: 10px;
        """)
        layout.addWidget(titulo)

        label_pontuacao = QLabel(f"Pontuação: {pontuacao} pts")
        label_pontuacao.setAlignment(Qt.AlignCenter)
        label_pontuacao.setFont(QFont("Verdana", 12))
        label_pontuacao.setStyleSheet("color: #2C2C2C;")

        label_tempo = QLabel(f"Tempo: {tempo}")
        label_tempo.setAlignment(Qt.AlignCenter)
        label_tempo.setFont(QFont("Verdana", 12))
        label_tempo.setStyleSheet("color: #2C2C2C;")

        label_jogadas = QLabel(f"Jogadas realizadas: {total_jogadas}")
        label_jogadas.setAlignment(Qt.AlignCenter)
        label_jogadas.setFont(QFont("Verdana", 12))
        label_jogadas.setStyleSheet("color: #2C2C2C;")

        layout.addWidget(label_pontuacao)
        layout.addWidget(label_tempo)
        layout.addWidget(label_jogadas)

        btn_retornar = BotaoRetornar()
        btn_retornar.clicked.connect(self._on_retornar)
        layout.addWidget(btn_retornar)

    def _on_retornar(self):
        self.retornar_tela_aluno.emit()
        self.accept()