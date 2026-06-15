from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QFrame, QSizePolicy
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QPalette, QColor, QPainter, QPainterPath, QBrush
from ui.components.botao_sair import BotaoSair

class RoundedRedBanner(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(180)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(8)

        titulo = QLabel("Quiminó")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setFont(QFont("Verdana Black", 48, QFont.Bold))
        titulo.setStyleSheet("color: white; background: transparent;")

        subtitulo = QLabel("Dominó de Funções Inorgânicas")
        subtitulo.setAlignment(Qt.AlignCenter)
        subtitulo.setFont(QFont("Verdana", 22, QFont.Bold))
        subtitulo.setStyleSheet("color: white; background: transparent;")

        layout.addWidget(titulo)
        layout.addWidget(subtitulo)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Banner vermelho principal
        main_path = QPainterPath()
        main_path.addRoundedRect(self.rect().adjusted(0, 0, 0, 0), 22, 22)
        painter.setBrush(QBrush(QColor("#911712")))
        painter.drawPath(main_path)

        super().paintEvent(event)


class BotaoEntrar(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setMinimumHeight(60)
        self.setFont(QFont("Verdana Black", 18, QFont.Bold))
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet("""
            QPushButton {
                background-color: #911712;
                color: white;
                border: none;
                font-size: 20px;
                border-radius: 6px;
                padding: 10px 40px;
            }
            QPushButton:hover {
                background-color: #c91a14;
            }
            QPushButton:pressed {
                background-color: #a81410;
            }
        """)


class TelaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiminó – Dominó de Funções Inorgânicas")
        self.setMinimumSize(750, 560)
        self.resize(900, 620)
        self._setup_ui()

    def _setup_ui(self):
        self.setStyleSheet("background-color: #fefefe;")

        # Layout principal
        outer = QVBoxLayout(self)
        outer.setContentsMargins(20, 16, 20, 20)
        outer.setSpacing(0)

        # -- Botão Sair (canto superior esquerdo) --
        top_bar = QHBoxLayout()
        self.btn_sair = BotaoSair()
        self.btn_sair.clicked.connect(self.close)
        top_bar.addWidget(self.btn_sair, alignment=Qt.AlignLeft | Qt.AlignTop)
        top_bar.addStretch()
        outer.addLayout(top_bar)

        outer.addSpacing(12)

        # -- Banner vermelho centralizado --
        banner_row = QHBoxLayout()
        banner_row.setContentsMargins(40, 0, 40, 0)
        self.banner = RoundedRedBanner()
        banner_row.addWidget(self.banner)
        outer.addLayout(banner_row)

        outer.addSpacing(36)

        # -- Seção Login --
        form_layout = QVBoxLayout()
        form_layout.setContentsMargins(120, 0, 120, 0)
        form_layout.setSpacing(12)

        label_login = QLabel("Login:")
        label_login.setFont(QFont("Verdana Black", 16, QFont.Bold))
        label_login.setStyleSheet("color: #111; background: transparent;")

        self.campo_login = QLineEdit()
        self.campo_login.setPlaceholderText(
            "Insira seu login aqui: (Aluno: nomealuno@aluno.cpf / Professor: nomeprof@prof.cpf  )"
        )
        self.campo_login.setMinimumHeight(52)
        self.campo_login.setFont(QFont("Verdana", 12))
        self.campo_login.setStyleSheet("""
            QLineEdit {
                background-color: #F0E0E0;
                border: 1.5px solid #ccc;
                border-radius: 10px;
                padding: 0 14px;
                color: #333;
            }
            QLineEdit:focus {
                border: 2px solid #E8201A;
                background-color: #fff;
            }
        """)

        form_layout.addWidget(label_login)
        form_layout.addWidget(self.campo_login)
        outer.addLayout(form_layout)

        outer.addSpacing(28)

        # Seção --- Senha ---

        form_layout = QVBoxLayout()
        form_layout.setContentsMargins(120, 0, 120, 0)
        form_layout.setSpacing(12)

        label_senha = QLabel("Senha:")
        label_senha.setFont(QFont("Verdana Black", 16, QFont.Bold))
        label_senha.setStyleSheet("color: #111; background: transparent;")

        self.campo_senha = QLineEdit()
        self.campo_senha.setPlaceholderText(
            "Insira senha aqui: (Ela deve seguir este padrão: Nome@AnoDeNascimento) "
        )
        self.campo_senha.setMinimumHeight(52)
        self.campo_senha.setFont(QFont("Arial", 12))
        self.campo_senha.setStyleSheet("""
            QLineEdit {
                background-color: #F0E0E0;
                border: 1.5px solid #ccc;
                border-radius: 10px;
                padding: 0 14px;
                color: #333;
            }
            QLineEdit:focus {
                border: 2px solid #E8201A;
                background-color: #fff;
            }
        """)

        form_layout.addWidget(label_senha)
        form_layout.addWidget(self.campo_senha)
        outer.addLayout(form_layout)

        outer.addSpacing(28)

        # -- Botão Entrar centralizado --
        btn_row = QHBoxLayout()
        self.btn_entrar = BotaoEntrar("Entrar")
        self.btn_entrar.setFixedWidth(280)
        btn_row.addStretch()
        btn_row.addWidget(self.btn_entrar)
        btn_row.addStretch()
        outer.addLayout(btn_row)

        outer.addStretch()       

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor("white"))
    app.setPalette(palette)

    janela = TelaLogin()
    janela.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()