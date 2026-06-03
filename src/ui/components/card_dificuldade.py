from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QSizePolicy, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
 
vermelho = "#911712"
cinza  = "#D9D9D9"
cor_texto = "#444444"

estilo_card_normal = f"""
QFrame#CardDificuldade {{
    background-color: {cinza};
    border-radius: 18px;
    border: none;
}}
"""
 
estilo_card_selecionado = f"""
    QFrame#CardDificuldade {{
        background-color: {cinza};
        border-radius: 18px;
        border: 3px solid {vermelho};
    }}
"""

class CardDificuldade(QFrame):
    def __init__(self, title: str, description: str,parent=None,):
        super().__init__(parent)
        self.setObjectName("CardDificuldade")
        self.selecionado = False

        self.setStyleSheet(f"""
        QFrame#CardDificuldade {{
            background-color: {cinza};
            border-radius: 18px;
            border: 3px solid transparent;
        }}
        QFrame#CardDificuldade:hover {{
            border: 2px solid {vermelho};
        }}
    """)
        
        self.layout_banner = QHBoxLayout()
        
        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumHeight(220)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
 
        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(12, 0, 12, 18)
 
        # -- tag vermelha -- #
        self.header_label = QLabel(title)
        self.header_label.setFont(QFont("Verdana", 12, QFont.Bold))
        self.header_label.setStyleSheet(f"""
        QLabel {{
            background-color: {vermelho};
            color: white;
            border-radius: 14px;
            padding: 8px 18px;
            font-weight: 700;
            font-size: 13px;
        }}
    """)
        self.header_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.header_label)
 
        layout.addSpacing(10)
 
        # -- Descrição -- #
        self.descricao_label = QLabel(description)
        self.descricao_label.setFont(QFont("Verdana", 10))
        self.descricao_label.setWordWrap(True)
        self.descricao_label.setAlignment(Qt.AlignCenter)
        self.descricao_label.setStyleSheet(f"""
        QLabel {{
            color: black;
            background-color: white;
            border: 1px solid #cccccc;
            border-radius: 10px;
            padding: 8px;
        }}
    """)
        layout.addWidget(self.descricao_label)
 
        layout.addStretch()
 
    def set_titulo(self, texto: str):
        """Altera o texto do header vermelho."""
        self.header_label.setText(texto)
 
    def set_descricao(self, texto: str):
        """Altera o texto descritivo do card."""
        self.descricao_label.setText(texto)
 
    def set_selecionado(self, selected: bool):
        """Marca ou desmarca o card visualmente."""
        self.selecionado = selected
        self.setStyleSheet(estilo_card_selecionado if selected else estilo_card_normal)
 
    # -- Clique do mouse -- #
    def mousePressEvent(self, evento):
        if evento.button() == Qt.LeftButton:
            self.set_selecionado(True)
            if self.parent():
                for sibling in self.parent().findChildren(CardDificuldade):
                    if sibling is not self:
                        sibling.set_selecionado(False)
        super().mousePressEvent(evento)