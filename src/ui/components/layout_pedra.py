from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel
from PySide6.QtCore import Qt, Signal, QMimeData, QPoint
from PySide6.QtGui import QDrag, QPixmap, QPainter


class LayoutPedra(QFrame):
    pedra_clicada = Signal(object)

    def __init__(self, id_lado_esquerdo=None, id_lado_direito=None, parent=None):
        super().__init__(parent)


        self.id_lado_esquerdo = id_lado_esquerdo
        self.id_lado_direito = id_lado_direito

        self.selecionada = False


        self.posicao_clique = QPoint()

        self._setup_ui()

    def _setup_ui(self):
        self.setFixedSize(120, 60)
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 2px solid #222222;
                border-radius: 6px;
            }
        """)

        layout_principal = QHBoxLayout(self)
        layout_principal.setContentsMargins(4, 4, 4, 4)
        layout_principal.setSpacing(0)

        # --- LADO ESQUERDO ---
        self.label_esquerdo = QLabel()
        self.label_esquerdo.setAlignment(Qt.AlignCenter)
        self.label_esquerdo.setFixedSize(50, 50)
        self.label_esquerdo.setStyleSheet("border: none;")

        if self.id_lado_esquerdo is not None:
            self.label_esquerdo.setText(str(self.id_lado_esquerdo))
        else:
            self.label_esquerdo.setText("?")

        # --- DIVISÓRIA CENTRAL ---
        divisoria = QFrame()
        divisoria.setFixedWidth(2)
        divisoria.setStyleSheet("background-color: #222222; border: none;")

        # --- LADO DIREITO ---
        self.label_direito = QLabel()
        self.label_direito.setAlignment(Qt.AlignCenter)
        self.label_direito.setFixedSize(50, 50)
        self.label_direito.setStyleSheet("border: none;")

        if self.id_lado_direito is not None:
            self.label_direito.setText(str(self.id_lado_direito))
        else:
            self.label_direito.setText("?")

        layout_principal.addWidget(self.label_esquerdo)
        layout_principal.addWidget(divisoria)
        layout_principal.addWidget(self.label_direito)


    def atualizar_conteudo(self, texto_esquerdo, texto_direito):
        self.label_esquerdo.setText(texto_esquerdo)
        self.label_direito.setText(texto_direito)

    def selecionar(self):
        self.selecionada = True
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 2px solid #8B0000;
                border-radius: 6px;
                margin-bottom: 8px;
            }
        """)

    def desselecionar(self):
        self.selecionada = False
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 2px solid #222222;
                border-radius: 6px;
            }
        """)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.posicao_clique = event.pos()
            self.pedra_clicada.emit(self)
        event.accept()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return

        drag = QDrag(self)
        mime = QMimeData()
        dados = f"{self.id_lado_esquerdo},{self.id_lado_direito}"
        mime.setText(dados)
        drag.setMimeData(mime)

        pixmap = QPixmap(self.size())
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        self.render(painter)
        painter.end()

        drag.setPixmap(pixmap)
        drag.setHotSpot(self.posicao_clique)

        drag.exec(Qt.MoveAction)