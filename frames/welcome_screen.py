from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class WelcomeScreen(QWidget):
    def __init__(self, width, height, top, bottom, left, right, text_size):
        super().__init__()
        self.initUI(width, height, top, bottom, left, right, text_size)

    def initUI(self, width, height, top, bottom, left, right, text_size):
        # Set window properties
        self.setGeometry(300, 300, width + left + right, height + top + bottom)
        self.setWindowTitle("Extracto")
        # Create label
        self.label = QLabel("Welcome to Product-to-be-Named\n\nby\n\nCompany-to-be-Named", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setStyleSheet(
            "QLabel { border: 1px solid black; background-color: lightgray; color: teal; padding: 20px; margin-top: %dpx; margin-bottom: %dpx; margin-left: %dpx; margin-right: %dpx; font-size: %dpx; font-weight: bold}" % (
                top, bottom, left, right, text_size))
        self.label.setGeometry(left, top, width, height)

    def resizeEvent(self, event):
        self.label.setGeometry(0, 0, self.width(), self.height())

    def switch_screen(self):
        self.parent().setCurrentIndex(1)
