from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class SaveInfo(QWidget):
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

        self.box1 = QtWidgets.QVBoxLayout()
        self.box1.setContentsMargins(50, 0, 0, 5)

        self.label = QtWidgets.QLabel("What would you like to name the new file?\n")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("QLabel {font-size: %dpx;}" % (27))
        self.text_field = QtWidgets.QLineEdit()
        # self.text_field.setGeometry(100, 80, 400, 50)
        self.text_field.setAlignment(Qt.AlignCenter)
        # self.text_field.resize(10, 20)
        self.text_field.setFixedSize(400, 50)
        # self.text_field.move(500, 600)
        self.text_field.setStyleSheet(
            "QLineEdit {border-radius: %dpx; border: 1px solid black; background-color: white;}" % (8))

        self.Ok_button = QtWidgets.QPushButton("Ok")
        self.Ok_button.setStyleSheet(
            "QPushButton { color: white; background-color: teal; font-size: %dpx; border-radius: %dpx;}" % (
                20, 8))

        self.Ok_button.setFixedSize(120, 50)
        self.buttons_box = QtWidgets.QHBoxLayout()
        self.buttons_box.addWidget(self.Ok_button)
        self.buttons_box.setAlignment(Qt.AlignCenter)

        self.box.addWidget(self.label)
        self.box1.addWidget(self.text_field)
        # self.box.addWidget(self.box1)
        self.box.addLayout(self.box1)
        self.box.addLayout(self.buttons_box)

        self.outer_layout = QtWidgets.QVBoxLayout()
        self.outer_layout.setContentsMargins(50, 20, 50, 20)
        self.outer_layout.addWidget(self.inner_frame)

        self.outer_frame.setLayout(self.outer_layout)
        self.setLayout(self.outer_frame.layout())
        self.setGeometry(100, 100, 500, 500)
        # self.Ok_button.clicked.connect(self.Ok_button_fun)

        self.Ok_button.clicked.connect(self.switch_screen)

    def resizeEvent(self, event):
        font = self.label.font()
        font.setPointSize(int(event.size().height() / 20))
        self.label.setFont(font)
        self.Ok_button.setFont(font)
        super().resizeEvent(event)

    def Ok_button_fun(self):
        print('Clicked ok button')

    def switch_screen(self):
        self.parent().setCurrentIndex(7)
