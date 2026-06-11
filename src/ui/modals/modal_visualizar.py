import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QFrame, QSizePolicy, QDialog, QScrollArea
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from components.botao_sair import BotaoSair
from Projeto_Integrador.src.database.crud_usuario import listar_usuarios





class ModalVisualizar(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Visualizar Usuários")
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

        texto = ""

        usuarios = listar_usuarios()

        for u in usuarios:
            texto += (
            f"ID: {u[0]}\n"
            f"Nome: {u[1]}\n"
            f"Email: {u[2]}\n"
            f"Tipo: {u[4]}\n"
            f"Vitórias: {u[5]}\n"
            f"Derrotas: {u[6]}\n"
            f"Pontuação: {u[7]}\n"
            "--------------------------\n\n"
            )

        termos_label = QLabel(texto)
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