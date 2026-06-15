from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea, QWidget
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from ui.components.botao_sair import BotaoSair

VERMELHO = "#911712"
CINZA = "#D9D9D9"

class CardComoJogar(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 300)
        self.setModal(True)
        self.setStyleSheet("background-color: #fefefe;")
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        # Header customizado (substitui a barra de título nativa)
        header_row = QHBoxLayout()

        header = QLabel("Como Jogar")
        header.setFont(QFont("Verdana", 14, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet(f"""
            QLabel {{
                background-color: {VERMELHO};
                color: white;
                border-radius: 6px;
                padding: 8px 18px;
            }}
        """)
        header_row.addWidget(header)
        layout.addLayout(header_row)

        # Área de regras com scroll
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("border: none;")

        conteudo = QWidget()
        conteudo_layout = QVBoxLayout(conteudo)

        regras = QLabel(
            "Este dominó é um pouco diferente do convencional! Sabendo disto, aqui você compreenderá as regras e o funcionamento do Quiminó!\n\n"
            "O quiminó possui as mesmas regras de um dominó convencional, com 28 pedras, sete para cada jogador, com direito a compra caso\n"
            "o jogador não tenha pedras compatíveis com as da mesa e o jogo acaba quando um jogador não possuir mais pedras em suas mãos\n"
            "ou quando nenhum outro jogador conseguir jogar mais. Entretanto, tem certas diferenças ao jogo tradicional:\n\n"
            "1. Regra um do jogo: Aqui não serão pedras numeradas, mas com conceitos químicos que podem ser combinados uns com os outros!\n"
            "2. Regra dois do jogo: Se a cada pedra que você jogar for compatível com a da mesa, você ganhará 10 pontos!\n"
            "3. Regra três do jogo: Caso você tentar jogar uma pedra na mesa que é incompatível, não ganhará pontos!\n\n"
        )
        regras.setFont(QFont("Verdana", 10))
        regras.setWordWrap(True)
        regras.setAlignment(Qt.AlignTop)
        regras.setStyleSheet("color: #444444; padding: 8px;")
        conteudo_layout.addWidget(regras)

        scroll.setWidget(conteudo)
        layout.addWidget(scroll)

        # Botão fechar
        botao_fechar = BotaoSair()
        botao_fechar.clicked.connect(self.close)
        layout.addWidget(botao_fechar, alignment=Qt.AlignCenter)