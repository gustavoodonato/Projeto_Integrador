import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QFrame, QSizePolicy, QDialog, QScrollArea
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from components.botao_sair import BotaoSair


texto_termos = """
TERMOS DE USO

1. ACEITAÇÃO DOS TERMOS
Ao utilizar esta aplicação, você concorda com os presentes Termos de Uso...

2. USO DA APLICAÇÃO
Esta aplicação é fornecida para uso pessoal e não comercial...

3. PRIVACIDADE
Seus dados são tratados conforme nossa Política de Privacidade...

4. RESPONSABILIDADES
O usuário é responsável por todas as atividades realizadas em sua conta...

5. MODIFICAÇÕES
Reservamo-nos o direito de modificar estes termos a qualquer momento...

6. DISPOSIÇÕES GERAIS
Estes termos são regidos pelas leis brasileiras...
""" * 5



class ModalVisualizar(QDialog):
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
        layout_modal_visualizar = QVBoxLayout(self)
        layout_modal_visualizar.setSpacing(8)  # ✅ Espaçamento geral reduzido
        layout_modal_visualizar.setContentsMargins(20, 20, 20, 20)

        botao_sair_modal_visualizar = BotaoSair()
        botao_sair_modal_visualizar.clicked.connect(self.close)
        layout_modal_visualizar.addWidget(botao_sair_modal_visualizar, alignment=Qt.AlignLeft | Qt.AlignTop)



        titulo_modal_visualizar = QLabel("Visualizar Usuários")
        titulo_modal_visualizar.setFont(QFont("Verdana", 22, QFont.Bold))
        titulo_modal_visualizar.setAlignment(Qt.AlignCenter)
        titulo_modal_visualizar.setStyleSheet("""
            QLabel {
                background-color: #911712;
                color: white;
                border-radius: 18px;
                padding: 10px 14px;
            }
        """)
        layout_modal_visualizar.addWidget(titulo_modal_visualizar)
        layout_modal_visualizar.addSpacing(12) 

        area_scroll = QScrollArea()
        area_scroll.setWidgetResizable(True)
        area_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        area_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        termos_label = QLabel(texto_termos)
        termos_label.setStyleSheet("""
            QLabel {
                background-color: white;
                color: black;
                padding: 10px 14px;
            }
        """)
        termos_label.setWordWrap(True)
        termos_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        termos_label.setContentsMargins(8, 8, 8, 8)

        area_scroll.setWidget(termos_label)
        layout_modal_visualizar.addWidget(area_scroll)

    def showEvent(self, event):
        super().showEvent(event)
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModalVisualizar()
    window.show()
    sys.exit(app.exec())