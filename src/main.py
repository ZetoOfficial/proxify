import sys
from PyQt6.QtWidgets import QApplication, QDialog
from src.main_ui import Ui_Dialog


def main():
    app = QApplication(sys.argv)
    dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
