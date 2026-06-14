import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from database.verificacao import VerificacaoLogin
from ui.screens.tela_aluno import TelaAluno
from ui.screens.tela_professor import TelaProfessor


class ControllerTelaLogin:
    def __init__(self, tela):
        self.tela = tela
        self.verificacao = VerificacaoLogin()
        self.tela.btn_entrar.clicked.connect(self.realizar_login)

    def realizar_login(self):
        login = self.tela.campo_login.text().strip()
        senha = self.tela.campo_senha.text().strip()

        if not login or not senha:
            self._mostrar_erro("Preencha o login e a senha.")
            return

        resultado = self.verificacao.verificar(login, senha)

        if resultado is None:
            self._mostrar_erro("Login ou senha incorretos.")
            return

        nome, tipo_usuario, partidas_ganhas, partidas_perdidas, pontuacao = resultado

        if tipo_usuario.lower() == "aluno":
            self._abrir_tela_aluno(nome, partidas_ganhas, partidas_perdidas, pontuacao)
        elif tipo_usuario.lower() == "professor":
            self._abrir_tela_professor(nome)
        else:
            self._mostrar_erro("Tipo de usuário desconhecido.")

    def _abrir_tela_aluno(self, nome, partidas_ganhas, partidas_perdidas, pontuacao):
        self.tela_aluno = TelaAluno(
            nome=nome,
            partidas_ganhas=partidas_ganhas,
            partidas_perdidas=partidas_perdidas,
            pontuacao=pontuacao
        )
        self.tela_aluno.retornar_login.connect(self._voltar_login_aluno)  # ← conecta
        self.tela_aluno.show()
        self.tela.close()

    def _abrir_tela_professor(self, nome):
        self.tela_professor = TelaProfessor(nome=nome)
        self.tela_professor.retornar_login.connect(self._voltar_login_professor)  # ← conecta
        self.tela_professor.show()
        self.tela.close()

    def _voltar_login_aluno(self):
        from ui.screens.tela_login import TelaLogin
        self.tela = TelaLogin()
        self.controller = ControllerTelaLogin(self.tela)  # ← salva a referência
        self.tela.show()
        self.tela_aluno.close()

    def _voltar_login_professor(self):
        from ui.screens.tela_login import TelaLogin
        self.tela = TelaLogin()
        self.controller = ControllerTelaLogin(self.tela)  # ← salva a referência
        self.tela.show()
        self.tela_professor.close()

    def _mostrar_erro(self, mensagem):
        from PySide6.QtWidgets import QMessageBox
        msg = QMessageBox(self.tela)
        msg.setWindowTitle("Erro de Login.\nInsira novamente os seus dados.")
        msg.setText(mensagem)
        msg.setIcon(QMessageBox.Warning)
        msg.setStyleSheet("""
        QMessageBox {
            background-color: #FFFFFF;
        }
        QMessageBox QLabel {
            color: #2C2C2C;
            font-family: Verdana;
            font-size: 13px;
            font-weight: bold;
        }
        QMessageBox QPushButton {
            background-color: #911712;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 6px 20px;
            font-family: Verdana;
            font-size: 12px;
            font-weight: bold;
            min-width: 80px;
        }
        QMessageBox QPushButton:hover {
            background-color: #c91a14;
        }
        QMessageBox QPushButton:pressed {
            background-color: #a81410;
        }
    """)
        msg.exec()