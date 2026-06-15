from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QFrame, QSizePolicy, QGridLayout, QApplication
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor, QPen, QBrush, QPolygon, QFont
from PySide6.QtCore import QPoint

from ui.components.botao_retornar import BotaoRetornar
from ui.components.layout_pedra import LayoutPedra
from ui.components.card_informacoes import CardInformacoes


class MesaJogo(QFrame):
    """Desenha o octógono vermelho e organiza as pedras jogadas em serpentina."""

    PEDRAS_POR_LINHA = 5

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(260)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet("background-color: transparent;")

        # Contador usado para calcular a posição de cada pedra na serpentina
        self.total_pedras_jogadas = 0

        # Grid onde as pedras são posicionadas
        self.grid_pedras = QGridLayout()
        self.grid_pedras.setSpacing(6)
        self.grid_pedras.setContentsMargins(60, 40, 60, 40)
        self.grid_pedras.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addLayout(self.grid_pedras)

    def paintEvent(self, event):
        """Desenha o octógono vermelho como fundo da mesa."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        w = self.width()
        h = self.height()
        corte = 30

        pontos = QPolygon([
            QPoint(corte, 0),
            QPoint(w - corte, 0),
            QPoint(w, corte),
            QPoint(w, h - corte),
            QPoint(w - corte, h),
            QPoint(corte, h),
            QPoint(0, h - corte),
            QPoint(0, corte),
        ])

        painter.setPen(QPen(QColor("#1a1a1a"), 4))
        painter.setBrush(QBrush(QColor("#911712")))
        painter.drawPolygon(pontos)

    def adicionar_pedra(self, pedra_widget):
        linha = self.total_pedras_jogadas // self.PEDRAS_POR_LINHA
        coluna = self.total_pedras_jogadas % self.PEDRAS_POR_LINHA

        # Linhas ímpares: inverte a coluna (direita → esquerda)
        if linha % 2 == 1:
            coluna = (self.PEDRAS_POR_LINHA - 1) - coluna

        self.grid_pedras.addWidget(pedra_widget, linha, coluna)
        self.total_pedras_jogadas += 1

        # Cresce a altura da mesa quando uma nova linha começa
        linhas_usadas = (self.total_pedras_jogadas // self.PEDRAS_POR_LINHA) + 1
        nova_altura = max(260, linhas_usadas * 80 + 80)
        self.setMinimumHeight(nova_altura)


class TelaPartida(QWidget):
    def __init__(self, nivel=1, parent=None):
        super().__init__(parent)

        self.nivel = nivel

        self.setWindowTitle("Partida")
        self.setMinimumSize(950, 650)
        self.setStyleSheet("background-color: #f0f0f0;")

        self._setup_ui()

    def _setup_ui(self):
        layout_raiz = QVBoxLayout(self)
        layout_raiz.setContentsMargins(20, 20, 20, 20)
        layout_raiz.setSpacing(12)

        # — Linha do topo: botão retornar —
        linha_topo = QHBoxLayout()
        self.botao_retornar = BotaoRetornar()
        linha_topo.addWidget(self.botao_retornar, alignment=Qt.AlignLeft | Qt.AlignTop)
        linha_topo.addStretch()
        layout_raiz.addLayout(linha_topo)

        self.botao_comprar = QPushButton("Comprar Pedra")
        self.botao_comprar.setFixedHeight(32)
        self.botao_comprar.setFont(QFont("Verdana Black", 18, QFont.Bold))
        self.botao_comprar.setStyleSheet("""
            QPushButton {
                background-color: #911712;
                color: white;
                border-radius: 6px;
                font-size: 15px;
                padding: 0 16px;
            }
            QPushButton:hover { background-color: #c91a14; }
            QPushButton:disabled { background-color: #a81410; }
        """)
        linha_topo.addWidget(self.botao_comprar, alignment=Qt.AlignRight | Qt.AlignTop)

        self.mesa = MesaJogo()
        layout_raiz.addWidget(self.mesa)

        linha_inferior = QHBoxLayout()
        linha_inferior.setSpacing(16)

        self.card_dicas = CardInformacoes("Dicas")
        linha_inferior.addWidget(self.card_dicas, alignment=Qt.AlignBottom)

        area_central = QVBoxLayout()
        area_central.setSpacing(8)

        self.bandeja = QFrame()
        self.bandeja.setFixedHeight(100)
        self.bandeja.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.bandeja.setStyleSheet("""
            QFrame {
                background-color: #AAAAAA;
                border-radius: 10px;
            }
        """)

        self.layout_mao = QHBoxLayout(self.bandeja)
        self.layout_mao.setContentsMargins(16, 10, 16, 10)
        self.layout_mao.setSpacing(10)
        self.layout_mao.setAlignment(Qt.AlignCenter)

        area_central.addWidget(self.bandeja)
        linha_inferior.addLayout(area_central)

        # Card de pontuação (direita)
        self.card_pontuacao = CardInformacoes("Pontuação")
        linha_inferior.addWidget(self.card_pontuacao, alignment=Qt.AlignBottom)

        layout_raiz.addLayout(linha_inferior)
