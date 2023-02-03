from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class ReferenceSuccess(QWidget):
    def __init__(self):
        super().__init__()
        self.outer_frame = QtWidgets.QFrame()
        self.outer_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.outer_frame.setLineWidth(1)
        self.outer_frame.setContentsMargins(0, 0, 0, 0)

        self.inner_frame = QtWidgets.QFrame()
        self.inner_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.inner_frame.setLineWidth(1)
        self.inner_frame.setContentsMargins(1, 1, 1, 1)
        self.inner_frame.setStyleSheet("background-color: lightgray;")

        self.box = QtWidgets.QVBoxLayout()
        self.box.setContentsMargins(130, 180, 130, 180)
        self.inner_frame.setLayout(self.box)

        self.label = QtWidgets.QLabel("Nice job! That was a good baseline!\n")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet(
            "QLabel {font-size: %dpx;}" % (27))
        # self.label.setWordWrap(True)
        self.Going_button = QtWidgets.QPushButton("Let’s Get Going")
        self.Going_button.setStyleSheet(
            "QPushButton { color: white; background-color: teal; font-size: %dpx; border-radius: %dpx;}" % (
                20, 8))

        self.Going_button.setFixedSize(200, 50)
        self.buttons_box = QtWidgets.QHBoxLayout()
        self.buttons_box.addWidget(self.Going_button)
        self.buttons_box.setAlignment(Qt.AlignCenter)

        self.box.addWidget(self.label)
        self.box.addLayout(self.buttons_box)

        self.outer_layout = QtWidgets.QVBoxLayout()
        self.outer_layout.setContentsMargins(50, 20, 50, 20)
        self.outer_layout.addWidget(self.inner_frame)

        self.outer_frame.setLayout(self.outer_layout)
        self.setLayout(self.outer_frame.layout())
        self.setGeometry(100, 100, 500, 500)

        # self.Going_button.clicked.connect(self.Going_button_fun)

        self.Going_button.clicked.connect(self.switch_screen)

    def resizeEvent(self, event):
        font = self.label.font()
        font.setPointSize(int(event.size().height() / 20))
        self.label.setFont(font)
        self.Going_button.setFont(font)
        super().resizeEvent(event)

    def Going_button_fun(self):
        print('Clicked going button')

    def switch_screen(self):
        self.parent().setCurrentIndex(6)