# ── Card: Desempenho dos Jogadores ───────────────────────────
import sys
from PySide6.QtWidgets import (
     QVBoxLayout,QLabel, QFrame,QSizePolicy,QApplication, QWidget
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

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
        layout.addWidget(self._card_header("Partidas Anteriores"))

        body = QWidget()
        body_l = QVBoxLayout(body)
        body_l.setContentsMargins(16, 16, 16, 16)
        body_l.setSpacing(0)
        body_l.addWidget(
            self._label("Partidas jogadas:"),
            alignment=Qt.AlignTop
        )
        body_l.addStretch()
        body_l.addWidget(
            self._label("Pontuação recorde:")
        )
        body_l.addStretch()

        layout.addWidget(body, stretch=1)

    def _card_header(self, text):
        lbl = QLabel(text)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setWordWrap(True)
        lbl.setFont(QFont("Arial", 15, QFont.Bold))
        lbl.setStyleSheet(f"""
            background-color: {CRIMSON};
            color: {WHITE};
            border-top-left-radius: 14px;
            border-top-right-radius: 14px;
            padding: 14px 10px;
        """)
        lbl.setFixedHeight(72)
        return lbl

    def _label(self, text):
        lbl = QLabel(text)
        lbl.setFont(QFont("Arial", 10, QFont.Bold))
        lbl.setStyleSheet(f"color: {TEXT_LABEL}; background: transparent;")
        return lbl
