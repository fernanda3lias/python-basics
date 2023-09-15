
import sys

from variables import WINDOW_ICON_PATH
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QLabel, QApplication, QAbstractButton, QMainWindow, QVBoxLayout, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    label1 = QLabel("Texto :)")
    label1.setStyleSheet('font-size: 150px')
    window.addWidgetToVLayout(label1)

    # Window icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.adjustFixedSize()

    window.show()
    app.exec()

