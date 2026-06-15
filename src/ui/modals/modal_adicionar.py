from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QDialog
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from ui.components.botao_sair import BotaoSair
from PySide6.QtWidgets import QMessageBox
from database.crud_usuario import adicionar_usuario

class BotaoAdicionar(QPushButton):
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

class ModalAdicionar(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Termos de Uso")
        self.setFixedSize(600, 500)
        self.setWindowFlags(
            Qt.Dialog |
            Qt.CustomizeWindowHint
        )
        self.setStyleSheet("""
            QDialog {
                background-color: white;
                border-radius: 6px;
                padding: 10px 14px;
            }
        """)
        self._build_ui()

    def _build_ui(self):
        layout_modal_adicionar = QVBoxLayout(self)
        layout_modal_adicionar.setSpacing(4)  
        layout_modal_adicionar.setContentsMargins(20, 20, 20, 20)

        botao_sair = BotaoSair()
        botao_sair.clicked.connect(self.close)
        layout_modal_adicionar.addWidget(botao_sair, alignment=Qt.AlignLeft | Qt.AlignTop)

        label_adicionar_usuario = QLabel("Adicionar Usuário")
        label_adicionar_usuario.setFont(QFont("Verdana", 22, QFont.Bold))
        label_adicionar_usuario.setAlignment(Qt.AlignCenter)
        label_adicionar_usuario.setStyleSheet("""
            QLabel {
                background-color: #911712;
                color: white;
                border-radius: 6px;
                padding: 10px 14px;
            }
        """)
        layout_modal_adicionar.addWidget(label_adicionar_usuario)
        layout_modal_adicionar.addSpacing(12)  # Espaço após o título

        label_adicionar_login = QLabel("Login:")
        label_adicionar_login.setFont(QFont("Verdana Black", 16, QFont.Bold))
        label_adicionar_login.setStyleSheet("color: #111; background: transparent;")

        self.campo_adicionar_login = QLineEdit()
        self.campo_adicionar_login.setPlaceholderText("Insira o login do aluno que deseja adicionar ao banco de alunos: (Aluno: nomealuno@aluno.cpf)")
        self.campo_adicionar_login.setMinimumHeight(52)
        self.campo_adicionar_login.setFont(QFont("Verdana", 12))
        self.campo_adicionar_login.setStyleSheet("""
            QLineEdit {
                background-color: #F0E0E0;
                border: 1.5px solid #ccc;
                border-radius: 6px;
                padding: 0 5px;
                color: #333;
            }
            QLineEdit:focus {
                border: 2px solid #E8201A;
                background-color: #fff;
            }
        """)

        layout_modal_adicionar.addWidget(label_adicionar_login)
        layout_modal_adicionar.addWidget(self.campo_adicionar_login)
        layout_modal_adicionar.addSpacing(10)  
        label_adicionar_senha = QLabel("Senha:")
        label_adicionar_senha.setFont(QFont("Verdana Black", 16, QFont.Bold))
        label_adicionar_senha.setStyleSheet("color: #111; background: transparent;")

        self.campo_adicionar_senha = QLineEdit()
        self.campo_adicionar_senha.setPlaceholderText(
            "Insira senha aqui: (Ela deve seguir este padrão: Nome@AnoDeNascimento) "
        )
        self.campo_adicionar_senha.setMinimumHeight(52)
        self.campo_adicionar_senha.setFont(QFont("Arial", 12))
        self.campo_adicionar_senha.setStyleSheet("""
            QLineEdit {
                background-color: #F0E0E0;
                border: 1.5px solid #ccc;
                border-radius: 6px;
                padding: 0 14px;
                color: #333;
            }
            QLineEdit:focus {
                border: 2px solid #E8201A;
                background-color: #fff;
            }
        """)

        layout_modal_adicionar.addWidget(label_adicionar_senha)
        layout_modal_adicionar.addWidget(self.campo_adicionar_senha)
        layout_modal_adicionar.addSpacing(16)  

        linha_botao = QHBoxLayout()
        self.botao_adicionar = BotaoAdicionar("Adicionar Aluno")
        self.botao_adicionar.setFixedWidth(280)
        self.botao_adicionar.clicked.connect(self.adicionar_aluno)
        linha_botao.addStretch()
        linha_botao.addWidget(self.botao_adicionar)
        linha_botao.addStretch()
        layout_modal_adicionar.addLayout(linha_botao)

    def adicionar_aluno(self):

        email = self.campo_adicionar_login.text().strip()
        senha = self.campo_adicionar_senha.text().strip()

        if not email or not senha:
            QMessageBox.warning(
                self,
                "Erro",
                "Preencha todos os campos."
        )
            return
        nome = email.split("@")[0]
            
        try:

            adicionar_usuario(
            nome,
            email,
            senha,
          "Aluno"
            )

            QMessageBox.information(
                self,
                "Sucesso",
                "Aluno adicionado com sucesso!"
        )

            self.close()

        except Exception as erro:

            QMessageBox.critical(
            self,
            "Erro",
            f"Erro ao adicionar aluno:\n{erro}"
        )

    def showEvent(self, event):
        super().showEvent(event)
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
