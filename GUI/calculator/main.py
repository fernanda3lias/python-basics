
import sys

from main_window import MainWindow
from display import Display
from info import Info
from buttons import Button, ButtonsGrid
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
    info = Info('math')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    display.setPlaceholderText("0")
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info)
    window.vLayout.addLayout(buttonsGrid)

    # Run
    window.adjustFixedSize()
    window.show()
    app.exec()

