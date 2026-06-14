import sys
from PySide6.QtWidgets import (
     QVBoxLayout, QLabel, QFrame, QSizePolicy, QHBoxLayout, QWidget
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

CRIMSON    = "#8B1A1A"
GRAY       = "#D9D9D9"
WHITE      = "#FFFFFF"
TEXT_LABEL = "#2C2C2C"

class CardDesempenho(QFrame):
    def __init__(self, partidas_ganhas=0, partidas_perdidas=0, pontuacao=0, parent=None):
        super().__init__(parent)

        self.setStyleSheet(f"""
            QFrame {{
                background-color: {GRAY};
                border-radius: 6px;
            }}
        """)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 8, 10, 10)
        layout.setSpacing(10)

        layout.addWidget(self._card_header("Partidas\nAnteriores"))

        body = QWidget()
        body_l = QVBoxLayout(body)
        body_l.setContentsMargins(16, 16, 16, 16)
        body_l.setSpacing(12)

        # Linha partidas ganhas / perdidas
        linha = QHBoxLayout()
        self.label_ganhas = self._label(f"Partidas\nVencidas:\n{partidas_ganhas}")
        self.label_perdidas = self._label(f"Partidas\nPerdidas:\n{partidas_perdidas}")
        linha.addWidget(self.label_ganhas)
        linha.addWidget(self.label_perdidas)
        body_l.addLayout(linha)

        body_l.addStretch()

        # Pontuação
        self.label_pontuacao = self._label(f"Pontuação Recorde:\n{pontuacao}")
        body_l.addWidget(self.label_pontuacao)

        layout.addWidget(body, stretch=1)

    def _card_header(self, text):
        lbl = QLabel(text)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setWordWrap(True)
        lbl.setFont(QFont("Arial", 15, QFont.Bold))
        lbl.setStyleSheet(f"""
            background-color: {CRIMSON};
            color: {WHITE};
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
            padding: 14px 10px;
        """)
        lbl.setFixedHeight(72)
        return lbl

    def _label(self, text):
        lbl = QLabel(text)
        lbl.setFont(QFont("Arial", 10, QFont.Bold))
        lbl.setWordWrap(True)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setStyleSheet(f"color: {TEXT_LABEL}; background: transparent;")
        return lbl