from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from components.graph import Canvas


class DisplayTHCData(QWidget):
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
        self.box.setContentsMargins(85, 10, 85, 10)
        self.inner_frame.setLayout(self.box)

        # self.label.setWordWrap(True)
        self.Going_button = QtWidgets.QPushButton("Close")
        self.Going_button.setStyleSheet(
            "QPushButton { color: white; background-color: teal; font-size: %dpx; border-radius: %dpx;}" % (
                20, 8))

        chart = Canvas(self, 70)
        self.graph_box = QtWidgets.QVBoxLayout()
        self.graph_box.addWidget(chart)
        self.graph_box.setAlignment(Qt.AlignTop)

        self.Going_button.setFixedSize(100, 50)
        self.buttons_box = QtWidgets.QHBoxLayout()
        self.buttons_box.addWidget(self.Going_button)
        self.buttons_box.setAlignment(Qt.AlignRight)

        self.box.addLayout(self.buttons_box)
        self.box.addLayout(self.graph_box)

        self.outer_layout = QtWidgets.QVBoxLayout()
        self.outer_layout.setContentsMargins(50, 30, 50, 30)
        self.outer_layout.addWidget(self.inner_frame)

        self.outer_frame.setLayout(self.outer_layout)
        self.setLayout(self.outer_frame.layout())
        # self.setGeometry(100, 100, 500, 500)

        self.Going_button.clicked.connect(self.switch_screen)

    def resizeEvent(self, event):
        super().resizeEvent(event)

    def Going_button_fun(self):
        print('Clicked going button')

    def switch_screen(self):
        self.parent().setCurrentIndex(3)
