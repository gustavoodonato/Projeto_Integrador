import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QFrame,
    QSizePolicy, QDialog, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from components.botao_sair import BotaoSair
from Projeto_Integrador.src.database.crud_usuario import deletar_usuario_email


class ModalDeletar(QDialog):
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
        layout_modal_deletar = QVBoxLayout(self)
        layout_modal_deletar.setSpacing(4)  
        layout_modal_deletar.setContentsMargins(20, 20, 20, 20)

        botao_sair_modal_deletar = BotaoSair()
        botao_sair_modal_deletar.clicked.connect(self.close)
        layout_modal_deletar.addWidget(botao_sair_modal_deletar, alignment=Qt.AlignLeft | Qt.AlignTop)

        label_deletar_usuario = QLabel("Deletar Usuário")
        label_deletar_usuario.setFont(QFont("Verdana", 22, QFont.Bold))
        label_deletar_usuario.setAlignment(Qt.AlignCenter)
        label_deletar_usuario.setStyleSheet("""
            QLabel {
                background-color: #911712;
                color: white;
                border-radius: 18px;
                padding: 10px 14px;
            }
        """)
        layout_modal_deletar.addWidget(label_deletar_usuario)
        layout_modal_deletar.addSpacing(12)  # Espaço após o título

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

        layout_modal_deletar.addWidget(label_adicionar_login)
        layout_modal_deletar.addWidget(self.campo_adicionar_login)
        layout_modal_deletar.addSpacing(10)

        

        # ✅ Botão centralizado e adicionado uma única vez
        linha_botao = QHBoxLayout()
        self.botao_deletar = QPushButton("Deletar dados do aluno")
        self.botao_deletar.setFixedWidth(380)
        self.botao_deletar.setMinimumHeight(60)
        self.botao_deletar.setFont(QFont("Verdana Black", 18, QFont.Bold))
        self.botao_deletar.setCursor(Qt.PointingHandCursor)
        self.botao_deletar.setStyleSheet("""
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
        linha_botao.addWidget(self.botao_deletar)
        linha_botao.addStretch()
        layout_modal_deletar.addLayout(linha_botao)
        self.botao_deletar.clicked.connect(self.deletar_aluno)


    def deletar_aluno(self):

        email = self.campo_adicionar_login.text().strip()

        if not email:

            QMessageBox.warning(
            self,
            "Erro",
            "Digite o email do aluno."
        )

            return

        deletar_usuario_email(email)

        QMessageBox.information(
        self,
        "Sucesso",
        "Aluno removido com sucesso!"
    )

        self.close()


    def showEvent(self, event):
        super().showEvent(event)
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModalDeletar()
    window.show()
    sys.exit(app.exec())
    


