
import sys

from main_window import MainWindow
from display import Display
from info import Info
from variables import WINDOW_ICON_PATH
from styles import setupTheme
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Window icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addWidgetToVLayout(info)


    # Display
    display = Display()
    display.setPlaceholderText("0")
    window.addWidgetToVLayout(display)

    # Run
    window.adjustFixedSize()
    window.show()
    app.exec()

