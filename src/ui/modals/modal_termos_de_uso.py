import sys
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout,
    QHBoxLayout, QLabel, QScrollArea, QPushButton,
    QCheckBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


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


class TermosDeUso(QDialog):
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
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(20, 20, 20, 20)

        titulo_termos_uso = QLabel("Termos de Uso do Quiminó")
        titulo_termos_uso.setFont(QFont("Verdana", 14, QFont.Bold))
        titulo_termos_uso.setAlignment(Qt.AlignCenter)
        titulo_termos_uso.setStyleSheet("""
            QLabel {
                background-color: #911712;
                color: white;
                border-radius: 18px;
                padding: 10px 14px;
            }
        """)
        layout.addWidget(titulo_termos_uso)

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
        layout.addWidget(area_scroll)

        # FIX 1 e 2: cor do texto visível + borda na checkbox
        self.checkbox_aceita = QCheckBox("Li e aceito os Termos de Uso")
        self.checkbox_aceita.setStyleSheet("""
            QCheckBox {
                color: #444444;
                font-size: 10pt;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
                border: 2px solid #911712;
                border-radius: 3px;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: #911712;
                border: 2px solid #911712;
            }
        """)
        self.checkbox_aceita.stateChanged.connect(self._on_checkbox_changed)
        layout.addWidget(self.checkbox_aceita)

        btn_layout = QHBoxLayout()

        self.botao_recusar = QPushButton("Recusar")
        self.botao_recusar.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: black;
                padding: 10px 14px;
                border: 1px solid #D9D9D9;
                border-radius: 12px;
            }
            QPushButton:hover { background-color: #f0f0f0; }
            QPushButton:pressed { background-color: #e0e0e0; }
        """)
        self.botao_recusar.clicked.connect(self._on_decline)

        # FIX 3: botão aceitar visível nos estados enabled e disabled
        self.botao_aceitar = QPushButton("Aceitar")
        self.botao_aceitar.setEnabled(False)
        self.botao_aceitar.setStyleSheet("""
            QPushButton:enabled {
                background-color: #911712;
                color: white;
                border: none;
                border-radius: 12px;
                padding: 10px 14px;
            }
            QPushButton:disabled {
                background-color: #D9D9D9;
                color: #888888;
                border: none;
                border-radius: 12px;
                padding: 10px 14px;
            }
            QPushButton:hover:enabled { background-color: #c91a14; }
            QPushButton:pressed:enabled { background-color: #a81410; }
        """)
        self.botao_aceitar.clicked.connect(self._on_accept)

        btn_layout.addWidget(self.botao_recusar)
        btn_layout.addWidget(self.botao_aceitar)
        layout.addLayout(btn_layout)

    def _on_checkbox_changed(self, state):
        self.botao_aceitar.setEnabled(state == Qt.Checked.value)

    def _on_accept(self):
        self.accept()

    def _on_decline(self):
        self.reject()

    def mousePressEvent(self, event):
        event.ignore()

    def mouseMoveEvent(self, event):
        event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            return
        super().keyPressEvent(event)

    def closeEvent(self, event):
        event.ignore()

    def showEvent(self, event):
        super().showEvent(event)
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TermosDeUso()
    window.show()
    sys.exit(app.exec())