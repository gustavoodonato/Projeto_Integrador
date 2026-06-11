# ── Card: Desempenho dos Jogadores ───────────────────────────
import sys
from PySide6.QtWidgets import (
     QVBoxLayout,QLabel, QFrame,QSizePolicy,QApplication, QWidget
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
from Projeto_Integrador.src.database.usuario import listar_alunos

CRIMSON      = "#8B1A1A"
GRAY     = "#D9D9D9"
WHITE        = "#FFFFFF"
TEXT_LABEL   = "#2C2C2C"

class CardDesempenho(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet(f"""
            QFrame {{
                background-color: {GRAY};
                border-radius: 14px;
            }}
        """)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 8, 10, 10)
        layout.setSpacing(10)
        layout.addWidget(
        self._card_header("Desempenho dos\nJogadores")
        )
        body = QWidget()
        body_l = QVBoxLayout(body)
        body_l.setContentsMargins(16, 16, 16, 16)
        body_l.setSpacing(0)

        body_l.addWidget(
        self._label("Histórico de partidas:"),
        alignment=Qt.AlignTop
        )

        body_l.addStretch()

        body_l.addWidget(
        self._label("Pontuação dos Alunos:")
        )

        self.lista_alunos = QLabel()
        self.lista_alunos.setWordWrap(True)

        body_l.addWidget(self.lista_alunos)

        body_l.addStretch()

        layout.addWidget(body, stretch=1)