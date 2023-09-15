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

        self.label1 = QLabel("Texto :)")
        self.v_layout.addChildWidget(self.label1)

        self.setCentralWidget(self.cw)

        # Window title
        self.setWindowTitle("Calculator")

        
    def adjustFixedSize(self):
        # Last thing to do
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
