from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class CardInformacoes(QFrame):
    def __init__(self, titulo="", parent=None):
        super().__init__(parent)
        self.titulo = titulo
        self._setup_ui()

    def _setup_ui(self):
        self.setFixedSize(160, 140)
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 2px solid #CCCCCC;
                border-radius: 8px;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 8, 10, 8)
        layout.setSpacing(6)

        label_titulo = QLabel(self.titulo)
        label_titulo.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        font_titulo = QFont()
        font_titulo.setBold(True)
        font_titulo.setPointSize(10)
        label_titulo.setFont(font_titulo)
        label_titulo.setStyleSheet("border: none; color: #333333;")

        self.label_conteudo = QLabel("")
        self.label_conteudo.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.label_conteudo.setWordWrap(True)
        self.label_conteudo.setStyleSheet("border: none; color: #555555;")
        font_conteudo = QFont()
        font_conteudo.setPointSize(9)
        self.label_conteudo.setFont(font_conteudo)

        layout.addWidget(label_titulo)
        layout.addWidget(self.label_conteudo)
        layout.addStretch()

    # Método público — atualiza o conteúdo do card

    def atualizar_conteudo(self, texto):
        self.label_conteudo.setText(texto)