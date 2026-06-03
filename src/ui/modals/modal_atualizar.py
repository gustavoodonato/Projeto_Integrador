import sys
from PySide6.QtWidgets import (
    QApplication, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QDialog
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from components.botao_sair import BotaoSair


class BotaoBuscar(QPushButton):
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
                border-radius: 20px;
                padding: 10px 40px;
            }
            QPushButton:hover {
                background-color: #c91a14;
            }
            QPushButton:pressed {
                background-color: #a81410;
            }
        """)

class ModalAtualizar(QDialog):
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
                border-radius: 18px;
                padding: 10px 14px;
            }
        """)
        self._build_ui()

    def _build_ui(self):
        layout_modal_atualizar = QVBoxLayout(self)
        layout_modal_atualizar.setSpacing(4)  
        layout_modal_atualizar.setContentsMargins(20, 20, 20, 20)

        botao_sair_modal_atualizar = BotaoSair()
        botao_sair_modal_atualizar.clicked.connect(self.close)
        layout_modal_atualizar.addWidget(botao_sair_modal_atualizar, alignment=Qt.AlignLeft | Qt.AlignTop)

        label_atualizar_usuario = QLabel("Atualizar Usuário")
        label_atualizar_usuario.setFont(QFont("Verdana", 22, QFont.Bold))
        label_atualizar_usuario.setAlignment(Qt.AlignCenter)
        label_atualizar_usuario.setStyleSheet("""
            QLabel {
                background-color: #911712;
                color: white;
                border-radius: 18px;
                padding: 10px 14px;
            }
        """)
        layout_modal_atualizar.addWidget(label_atualizar_usuario)
        layout_modal_atualizar.addSpacing(12)  # Espaço após o título

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
                border-radius: 10px;
                padding: 0 5px;
                color: #333;
            }
            QLineEdit:focus {
                border: 2px solid #E8201A;
                background-color: #fff;
            }
        """)

        layout_modal_atualizar.addWidget(label_adicionar_login)
        layout_modal_atualizar.addWidget(self.campo_adicionar_login)
        layout_modal_atualizar.addSpacing(10)

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
                border-radius: 10px;
                padding: 0 14px;
                color: #333;
            }
            QLineEdit:focus {
                border: 2px solid #E8201A;
                background-color: #fff;
            }
        """)

        layout_modal_atualizar.addWidget(label_adicionar_senha)
        layout_modal_atualizar.addWidget(self.campo_adicionar_senha)
        layout_modal_atualizar.addSpacing(16)  # Espaço antes do botão

        # ✅ Botão centralizado e adicionado uma única vez
        linha_botao = QHBoxLayout()
        self.botao_atualizar = QPushButton("Atualizar dados do aluno")
        self.botao_atualizar.setFixedWidth(380)
        self.botao_atualizar.setMinimumHeight(60)
        self.botao_atualizar.setFont(QFont("Verdana Black", 18, QFont.Bold))
        self.botao_atualizar.setCursor(Qt.PointingHandCursor)
        self.botao_atualizar.setStyleSheet("""
            QPushButton {
                background-color: #911712;
                color: white;
                border: none;
                border-radius: 20px;
                padding: 10px 40px;
            }
            QPushButton:hover {
                background-color: #c91a14;
            }
            QPushButton:pressed {
                background-color: #a81410;
            }
        """)
        linha_botao.addStretch()
        linha_botao.addWidget(self.botao_atualizar)
        linha_botao.addStretch()
        layout_modal_atualizar.addLayout(linha_botao)

        
    def showEvent(self, event):
        super().showEvent(event)
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModalAtualizar()
    window.show()
    sys.exit(app.exec())