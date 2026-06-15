import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFrame, QSizePolicy
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont
from components.botao_retornar import BotaoRetornar
from components.card_dificuldade import CardDificuldade
from modals.modal_como_jogar import CardComoJogar
from components.card_desempenho_alunos import CardDesempenho

class TelaAluno(QWidget):
    retornar_login = Signal()

    def __init__(self, nome="", partidas_ganhas=0, partidas_perdidas=0, pontuacao=0):
        super().__init__()
        self.nome = nome
        self.partidas_ganhas = partidas_ganhas
        self.partidas_perdidas = partidas_perdidas
        self.pontuacao = pontuacao
        self.setWindowTitle("Tela Aluno")
        self.setMinimumSize(750, 560)
        self._setup_ui()

    def _setup_ui(self):
        self.setStyleSheet("background-color: #fefefe;")

        layout_raiz = QVBoxLayout(self)
        layout_raiz.setContentsMargins(20, 20, 20, 20)
        layout_raiz.setSpacing(12)

        linha_topo = QHBoxLayout()
        linha_topo.setSpacing(12)

        self.botao_retornar = BotaoRetornar()
        self.botao_retornar.clicked.connect(self.retornar_login.emit)
        linha_topo.addWidget(self.botao_retornar, alignment=Qt.AlignLeft | Qt.AlignTop)

        self.label_bem_vindo = self._criar_label_titulo(f"Bem Vindo, {self.nome}\nà Tela de Seleção de Jogo!")
        linha_topo.addWidget(self.label_bem_vindo, stretch=1)

        self.card_como_jogar = self._criar_card_como_jogar()
        self.card_como_jogar.setFixedWidth(280)
        linha_topo.addWidget(self.card_como_jogar)

        layout_raiz.addLayout(linha_topo)

        linha_meio = QHBoxLayout()
        linha_meio.setSpacing(20)

        self.card_desempenho = CardDesempenho(
            partidas_ganhas=self.partidas_ganhas,
            partidas_perdidas=self.partidas_perdidas,
            pontuacao=self.pontuacao
        )
        self.card_desempenho.setFixedWidth(220)
        linha_meio.addWidget(self.card_desempenho)

        coluna_central = QVBoxLayout()
        coluna_central.setSpacing(16)

        self.label_dificuldade = self._criar_label_titulo("Escolha o Nível de Dificuldade que Deseja Jogar")
        coluna_central.addWidget(self.label_dificuldade)

        linha_cards = QHBoxLayout()
        linha_cards.setSpacing(16)

        self.card_facil = CardDificuldade(
            title="Nível Fácil",
            description=(
                "Neste nível, os jogadores deverão relacionar as fórmulas químicas "
                "com suas respectivas funções inorgânicas. Cada pedra do dominó possui, "
                "de um lado, uma fórmula química e, do outro, o nome de uma função "
                "inorgânica (ácido, base, sal ou óxido)."
            ),
        )
        self.card_medio = CardDificuldade(
            title="Nível Médio",
            description=(
                "Neste nível, os jogadores deverão relacionar as fórmulas químicas "
                "aos nomes corretos dos compostos inorgânicos. Cada peça do dominó "
                "apresenta, de um lado, a fórmula química de uma substância e, do outro, "
                "o nome de um composto químico."
            ),
        )
        self.card_dificil = CardDificuldade(
            title="Nível Difícil",
            description=(
                "Neste nível, os jogadores deverão associar as propriedades características "
                "das funções inorgânicas às suas respectivas classes químicas. Cada peça "
                "contém, de um lado, uma propriedade química ou característica específica e, "
                "do outro, a classificação correspondente (ácidos, bases, sais ou óxidos)."
            ),
        )

        linha_cards.addWidget(self.card_facil, stretch=1)
        linha_cards.addWidget(self.card_medio, stretch=1)
        linha_cards.addWidget(self.card_dificil, stretch=1)
        coluna_central.addLayout(linha_cards)

        self.botao_iniciar = self._criar_botao_iniciar()
        coluna_central.addWidget(self.botao_iniciar, alignment=Qt.AlignCenter)

        linha_meio.addLayout(coluna_central, stretch=1)
        layout_raiz.addLayout(linha_meio, stretch=1)

    def _criar_label_titulo(self, texto: str) -> QLabel:
        label = QLabel(texto)
        label.setFont(QFont("Verdana", 20, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        label.setStyleSheet("""
            QLabel {
                background-color: #911712;
                color: white;
                border-radius: 6px;
                padding: 10px 14px;
            }
        """)
        return label

    def _criar_card_como_jogar(self) -> QFrame:
        frame = QFrame()
        frame.setStyleSheet("QFrame { background-color: #D9D9D9; border-radius: 18px; }")

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)

        botao = QPushButton("Como Jogar?")
        botao.setFont(QFont("Verdana", 11, QFont.Bold))
        botao.setCursor(Qt.PointingHandCursor)
        botao.setStyleSheet("""
            QPushButton { background-color: #911712; color: white;
                          border: none; border-radius: 6px; padding: 8px 16px; }
            QPushButton:hover   { background-color: #c91a14; }
            QPushButton:pressed { background-color: #a81410; }
        """)
        botao.clicked.connect(self._abrir_como_jogar)
        layout.addWidget(botao)

        descricao = QLabel(
            "Bem vindo ao Quiminó! Este é um jogo um pouco diferente do dominó "
            "tradicional, pois aqui, você deverá elaborar novas estratégias enquanto "
            "aprende sobre o mundo da química."
        )
        descricao.setFont(QFont("Verdana", 10))
        descricao.setAlignment(Qt.AlignCenter)
        descricao.setWordWrap(True)
        descricao.setStyleSheet(
            "color: #444444; background-color: white; border-radius: 6px; padding: 6px;"
        )
        layout.addWidget(descricao)

        return frame

    def _criar_botao_iniciar(self) -> QPushButton:
        botao = QPushButton("Iniciar Partida")
        botao.setFixedSize(400, 80)
        botao.setFont(QFont("Verdana", 20, QFont.Bold))
        botao.setCursor(Qt.PointingHandCursor)
        botao.setStyleSheet("""
            QPushButton { background-color: #911712; color: white;
                          border: none; border-radius: 6px; }
            QPushButton:hover   { background-color: #c91a14; }
            QPushButton:pressed { background-color: #a81410; }
        """)
        return botao

    def _abrir_como_jogar(self):
        modal = CardComoJogar(parent=self)
        modal.exec()