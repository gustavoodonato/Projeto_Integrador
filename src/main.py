import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QColor

from ui.screens.tela_login import TelaLogin
from controllers.controller_tela_login import ControllerTelaLogin


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor("white"))
    app.setPalette(palette)


    tela_login = TelaLogin()
    controller = ControllerTelaLogin(tela_login)
    tela_login.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()