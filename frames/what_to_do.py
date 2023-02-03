from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class WhatToDo(QWidget):
    def __init__(self):
        super().__init__()
        self.outer_frame = QFrame()
        self.outer_frame.setFrameShape(QFrame.Box)
        self.outer_frame.setLineWidth(1)
        self.outer_frame.setContentsMargins(0, 0, 0, 0)

        self.inner_frame = QFrame()
        self.inner_frame.setFrameShape(QFrame.Box)
        self.inner_frame.setLineWidth(1)
        self.inner_frame.setContentsMargins(1, 1, 1, 1)
        self.inner_frame.setStyleSheet("background-color: lightgray;")

        self.box = QVBoxLayout()
        self.box.setContentsMargins(130, 180, 130, 180)
        self.inner_frame.setLayout(self.box)

        self.label = QLabel("What would you like to do?\n")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet(
            "QLabel {font-size: %dpx;}" % (27))
        self.label.setWordWrap(True)
        self.start_button = QPushButton("Start Live Data")
        self.stop_button = QPushButton("Show Old Data")
        self.start_button.setStyleSheet(
            "QPushButton { color: white; background-color: teal; font-size: %dpx; border-radius: %dpx;}" % (
                20, 8))
        self.stop_button.setStyleSheet(
            "QPushButton { color: white; background-color: teal; font-size: %dpx; border-radius: %dpx;}" % (
                20, 8))

        self.start_button.setFixedSize(200, 50)
        self.stop_button.setFixedSize(200, 50)
        self.buttons_box = QHBoxLayout()
        self.buttons_box.addWidget(self.start_button)
        self.buttons_box.addSpacing(32)
        self.buttons_box.addWidget(self.stop_button)
        self.buttons_box.setAlignment(Qt.AlignCenter)

        self.box.addWidget(self.label)
        self.box.addLayout(self.buttons_box)

        self.outer_layout = QVBoxLayout()
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
        font = self.label.font()
        font.setPointSize(int(event.size().height() / 20))
        self.label.setFont(font)
        self.start_button.setFont(font)
        self.stop_button.setFont(font)
        super().resizeEvent(event)

    def start_button_fun(self):
        print('Clicked start button')

    def stop_button_fun(self):
        print('Clicked stop button')

    def switch_screen(self):
        self.parent().setCurrentIndex(2)