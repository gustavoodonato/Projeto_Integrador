from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QLabel, QFrame, QTextEdit,
    QSizePolicy
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont
from ui.components.botao_retornar import BotaoRetornar
from ui.modals.modal_adicionar import ModalAdicionar
from ui.modals.modal_visualizar import ModalVisualizar
from ui.modals.modal_atualizar import ModalAtualizar
from ui.modals.modal_deletar import ModalDeletar

CRIMSON     = "#911712"
CRIMSON_HOV = "#A52020"
GRAY        = "#D9D9D9"
WHITE       = "#FFFFFF"
BORDER      = "#C5C5C5"
TEXT_LABEL  = "#2C2C2C"


class TelaProfessor(QMainWindow):
    retornar_login = Signal()

    def __init__(self, nome=""):
        super().__init__()
        self.nome = nome
        self.setWindowTitle("Painel do Jogo")
        self.setMinimumSize(820, 520)
        self.setStyleSheet(f"background-color: {WHITE};")

        central = QWidget()
        self.setCentralWidget(central)
        root_layout = QVBoxLayout(central)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        root_layout.addWidget(self._build_topbar())
        root_layout.addWidget(self._build_main(), stretch=1)
        root_layout.addWidget(self._build_bottombar())

    def _build_topbar(self):
        bar = QWidget()
        bar.setFixedHeight(46)
        bar.setStyleSheet(f"background-color: {WHITE};")
        layout = QHBoxLayout(bar)
        layout.setContentsMargins(14, 8, 14, 8)
        layout.setAlignment(Qt.AlignLeft)

        btn = BotaoRetornar()
        btn.clicked.connect(self.retornar_login.emit)
        layout.addWidget(btn)
        return bar

    def _build_main(self):
        wrapper = QWidget()
        layout = QHBoxLayout(wrapper)
        layout.setContentsMargins(16, 10, 16, 16)
        layout.setSpacing(20)

        layout.addWidget(self._card_desempenho())
        layout.addWidget(self._card_admin())
        return wrapper

    def _card_desempenho(self):
        card = self._make_card()
        layout = card.layout()
        layout.addWidget(self._card_header("Desenpenho dos\nJogadores"))

        body = QWidget()
        body_l = QVBoxLayout(body)
        body_l.setContentsMargins(16, 16, 16, 16)
        body_l.setSpacing(0)

        body_l.addWidget(self._label("Histórico de partidas:"), alignment=Qt.AlignTop)
        body_l.addStretch()
        body_l.addWidget(self._label("Pontuação dos Alunos:"))
        body_l.addStretch()

        layout.addWidget(body, stretch=1)
        return card

    def _card_admin(self):
        card = self._make_card()
        layout = card.layout()
        layout.addWidget(self._card_header("Administração de\nJogadores"))

        body = QWidget()
        body_l = QVBoxLayout(body)
        body_l.setContentsMargins(16, 10, 16, 16)
        body_l.setSpacing(0)

        acoes = [
            ("Adicionar Usuário:",          "Adicionar",  self._abrir_adicionar),
            ("Visualizar Usuários:",         "Visualizar", self._abrir_visualizar),
            ("Atualizar Dados de Usuários:", "Atualizar",  self._abrir_atualizar),
            ("Deletar Dados de Usuários:",   "Deletar",    self._abrir_deletar),
        ]
        for i, (texto, btn_text, metodo) in enumerate(acoes):
            row = self._admin_row(texto, btn_text, last=(i == len(acoes) - 1))
            botao = row.findChild(QPushButton)
            botao.clicked.connect(metodo)
            body_l.addWidget(row, stretch=1)

        layout.addWidget(body, stretch=1)
        return card

    def _abrir_adicionar(self):
        modal = ModalAdicionar(parent=self)
        modal.exec()

    def _abrir_visualizar(self):
        modal = ModalVisualizar(parent=self)
        modal.exec()

    def _abrir_atualizar(self):
        modal = ModalAtualizar(parent=self)
        modal.exec()

    def _abrir_deletar(self):
        modal = ModalDeletar(parent=self)
        modal.exec()

    def _make_card(self):
        card = QFrame()
        card.setStyleSheet(f"""
            QFrame {{
                background-color: {GRAY};
                border-radius: 14px;
            }}
        """)
        card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout = QVBoxLayout(card)
        layout.setContentsMargins(10, 8, 10, 10)
        layout.setSpacing(10)
        return card

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

    def _admin_row(self, label_text, btn_text, last=False):
        row = QWidget()
        row.setStyleSheet("background: transparent;")
        layout = QHBoxLayout(row)
        layout.setContentsMargins(0, 10, 0, 10)

        lbl = QLabel(label_text)
        lbl.setFont(QFont("Arial", 10, QFont.Bold))
        lbl.setStyleSheet(f"color: {TEXT_LABEL}; background: transparent;")
        layout.addWidget(lbl, stretch=1)

        btn = QPushButton(btn_text)
        btn.setFixedSize(90, 28)
        btn.setFont(QFont("Verdana Black", 13, QFont.Bold))
        btn.setCursor(Qt.PointingHandCursor)
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {CRIMSON};
                color: {WHITE};
                border: none;
                border-radius: 6px;
            }}
            QPushButton:hover  {{ background-color: {CRIMSON_HOV}; }}
            QPushButton:pressed {{ background-color: {CRIMSON};     }}
        """)
        layout.addWidget(btn)

        if not last:
            wrapper = QWidget()
            wrapper.setStyleSheet("background: transparent;")
            v = QVBoxLayout(wrapper)
            v.setContentsMargins(0, 0, 0, 0)
            v.setSpacing(0)
            v.addWidget(row)
            line = QFrame()
            line.setFrameShape(QFrame.HLine)
            line.setStyleSheet(f"color: {BORDER};")
            v.addWidget(line)
            return wrapper

        return row

    def _build_bottombar(self):
        bar = QWidget()
        bar.setFixedHeight(12)
        bar.setStyleSheet(f"background-color: {WHITE};")
        return bar