# Example File for using the base gui.
from PyQt6.QtWidgets import QApplication

from base import MainWindowBase

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindowBase(cfg='config_ex.yml')
    window.show()
    app.exec()

