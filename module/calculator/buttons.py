from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty

from PySide6.QtWidgets import QPushButton, QGridLayout, QAbstractButton
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)

class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self._makeGrid()

    def _makeGrid(self):
        for row_number, row_data in enumerate(self._gridMask):
            for column_number, button_text in enumerate(row_data):
                button = Button(button_text)

                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')

                if isEmpty(button_text):
                    #button.setProperty('cssClass', 'specialButton')
                    pixmap = QPixmap(r'files\zerotwo.png')
                    button.setIcon(QIcon(pixmap))
                    button.setIconSize(QSize(80, 80))
                    button.setMaximumHeight(75)


                self.addWidget(button, row_number, column_number)