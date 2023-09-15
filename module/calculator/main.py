
import sys

from main_window import MainWindow
from PySide6.QtWidgets import QLabel, QApplication, QAbstractButton, QMainWindow, QVBoxLayout, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.adjustFixedSize()

    window.show()
    app.exec()

