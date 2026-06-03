from PySide6.QtWidgets import (QPushButton, QSizePolicy
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class BotaoRetornar(QPushButton):
    def __init__(self, parent=None):
        super().__init__("Retornar a Tela Inicial", parent)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setFixedSize(200, 42)
        self.setFont(QFont("Verdana Black", 13, QFont.Bold))
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet("""
            QPushButton {
                background-color: #911712;
                color: white;
                border: none;
                border-radius: 18px;
            }
            QPushButton:hover {
                background-color: #c91a14;
            }
            QPushButton:pressed {
                background-color: #a81410;
            }
        """)