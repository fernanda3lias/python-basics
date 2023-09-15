from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget)

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Layout config
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        # Window title
        self.setWindowTitle("Calculator")

    def addWidgetToVLayout(self, widget: QWidget):
        # Add widget
        self.v_layout.addWidget(widget)

    def adjustFixedSize(self):
        # Last thing to do
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
