from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class EnsureCleanAir(QWidget):
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

        self.label1 = QtWidgets.QLabel("Are you sure?\n")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setStyleSheet(
            "QLabel {font-size: %dpx;}" % (27))
        self.label2 = QtWidgets.QLabel("FILENAME\n")
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setStyleSheet(
            "QLabel {font-size: %dpx;}" % (16))
        self.label2.setWordWrap(True)
        self.start_button = QtWidgets.QPushButton("Yes, I mean it!")
        self.stop_button = QtWidgets.QPushButton("Maybe not...")
        self.start_button.setStyleSheet(
            "QPushButton { color: white; background-color: teal; font-size: %dpx; border-radius: %dpx;}" % (
                20, 8))
        self.stop_button.setStyleSheet(
            "QPushButton { color: white; background-color: teal; font-size: %dpx; border-radius: %dpx;}" % (
                20, 8))

        self.start_button.setFixedSize(240, 50)
        self.stop_button.setFixedSize(240, 50)
        self.buttons_box = QtWidgets.QHBoxLayout()
        self.buttons_box.addWidget(self.start_button)
        self.buttons_box.addSpacing(32)
        self.buttons_box.addWidget(self.stop_button)
        self.buttons_box.setAlignment(Qt.AlignCenter)

        self.box.addWidget(self.label1)
        self.box.addWidget(self.label2)
        self.box.addLayout(self.buttons_box)

        self.outer_layout = QtWidgets.QVBoxLayout()
        self.outer_layout.setContentsMargins(50, 20, 50, 20)
        self.outer_layout.addWidget(self.inner_frame)

        self.outer_frame.setLayout(self.outer_layout)
        self.setLayout(self.outer_frame.layout())
        self.setGeometry(100, 100, 500, 500)

        # self.start_button.clicked.connect(self.start_button_fun)
        # self.stop_button.clicked.connect(self.stop_button_fun)

        self.start_button.clicked.connect(self.switch_screen)
        self.stop_button.clicked.connect(self.switch_screen)

    def resizeEvent(self, event):
        font = self.label1.font()
        font.setPointSize(int(event.size().height() / 20))
        self.label1.setFont(font)
        self.start_button.setFont(font)
        self.stop_button.setFont(font)
        super().resizeEvent(event)

    def start_button_fun(self):
        print('Clicked start button')

    def stop_button_fun(self):
        print('Clicked stop button')

    def switch_screen(self):
        self.parent().setCurrentIndex(8)