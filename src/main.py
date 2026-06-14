import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "src")
    )
)

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QColor

from ui.screens.tela_login import TelaLogin
from ui.modals.modal_termos_de_uso import TermosDeUso
from controllers.controller_tela_login import ControllerTelaLogin


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor("white"))
    app.setPalette(palette)

    # Abre a tela de login primeiro
    tela_login = TelaLogin()
    controller = ControllerTelaLogin(tela_login)
    tela_login.show()

    termos = TermosDeUso(parent=tela_login)
    resultado = termos.exec()

    if resultado != TermosDeUso.Accepted:
        sys.exit(0)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()