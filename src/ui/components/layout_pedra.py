from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont


class LayoutPedra(QFrame):
    pedra_clicada = Signal(object)

    def __init__(self, id_lado_esquerdo=None, id_lado_direito=None, parent=None):
        super().__init__(parent)
        self.id_lado_esquerdo = id_lado_esquerdo
        self.id_lado_direito = id_lado_direito
        self.selecionada = False
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

        self.label_esquerdo = QLabel()
        self.label_esquerdo.setAlignment(Qt.AlignCenter)
        self.label_esquerdo.setFixedSize(50, 50)
        self.label_esquerdo.setStyleSheet("border: none;")

        # Mostra o ID do lado esquerdo (substituir pelo conteúdo real do banco depois)
        if self.id_lado_esquerdo is not None:
            self.label_esquerdo.setText(str(self.id_lado_esquerdo))
        else:
            self.label_esquerdo.setText("?")

        divisoria = QFrame()
        divisoria.setFixedWidth(2)
        divisoria.setStyleSheet("background-color: #222222; border: none;")

        self.label_direito = QLabel()
        self.label_direito.setAlignment(Qt.AlignCenter)
        self.label_direito.setFixedSize(50, 50)
        self.label_direito.setStyleSheet("border: none;")

        # Mostra o ID do lado direito (substituir pelo conteúdo real do banco depois)
        if self.id_lado_direito is not None:
            self.label_direito.setText(str(self.id_lado_direito))
        else:
            self.label_direito.setText("?")

        # Adiciona tudo no layout
        layout_principal.addWidget(self.label_esquerdo)
        layout_principal.addWidget(divisoria)
        layout_principal.addWidget(self.label_direito)

    # -------------------------------------------------------
    # Métodos públicos — usados pela tela da partida
    # -------------------------------------------------------

    def atualizar_conteudo(self, texto_esquerdo, texto_direito):
        """
        Atualiza o texto exibido em cada lado da pedra.
        Chamar este método depois de buscar os dados no banco de dados.

        Exemplo de uso:
            pedra.atualizar_conteudo("HCl", "Ácido Clorídrico")
        """
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
        self.pedra_clicada.emit(self)