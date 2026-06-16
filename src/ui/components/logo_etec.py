import base64

from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class LogoEtec(QLabel):
    def __init__(self, width=180, height=90, parent=None):
        super().__init__(parent)

        base64_string = """
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
"""

        dados = base64.b64decode(base64_string)

        pixmap = QPixmap()
        pixmap.loadFromData(dados)

        self.setPixmap(
            pixmap.scaled(
                width,
                height,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )