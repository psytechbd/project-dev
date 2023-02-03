from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from components.graph import Canvas


class DisplayTHC(QWidget):
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

        self.box = QVBoxLayout()
        self.box.setContentsMargins(0, 5, 5, 20)
        self.inner_frame.setLayout(self.box)

        self.box0 = QHBoxLayout()
        self.box0.setContentsMargins(0, 40, 0, 50)

        self.box1 = QHBoxLayout()
        self.box1.setContentsMargins(10, 0, 5, 5)
        # self.box.setLayout(self.box1)

        self.box2 = QHBoxLayout()
        self.box2.setContentsMargins(0, 0, 0, 145)
        # self.box.setLayout(self.box2)

        self.title_label = QtWidgets.QLabel("<span style='font-size: 17px'><b><u>Filename</u></b></span>")
        self.title_label.setContentsMargins(0, 5, 0, 0)

        self.text_box = QtWidgets.QTextEdit()
        self.text_box.setReadOnly(True)
        self.text_box.setFrameShape(QtWidgets.QFrame.Box)
        self.text_box.setLineWidth(1)
        # self.text_box.setFixedHeight(30)
        # self.text_box.setFixedWidth(100)
        self.text_box.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_box.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_box.setText(
            "<div><div><span style='font-size: 18px; text-align:left'>Total THC</div><div></span><span style='text-align:center'>31.6</span><span style='font-size: 45px'>%</span></div></div>")
        # self.text_box.setAlignment(Qt.AlignCenter)
        self.text_box.setStyleSheet(
            "border :1px solid blue; color: white; background-color: teal; font-size: %dpx;" % (210))
        self.text_box.setFixedSize(460, 290)

        self.elapsed_time_label = QtWidgets.QLabel(
            "<span style='font-size: 17px'>Elapsed time: <span style='color:teal; font-weight: bold'>93:81</span></span>")
        self.elapsed_time_label.setContentsMargins(0, 5, 5, 0)
        # self.elapsed_time_label.setStyleSheet("color: teal")

        self.header_layout = QtWidgets.QHBoxLayout()
        self.header_layout.addWidget(self.title_label)
        self.header_layout.addSpacing(525)
        self.header_layout.addWidget(self.elapsed_time_label)
        self.header_layout.setAlignment(Qt.AlignTop | Qt.AlignRight)
        self.box.addLayout(self.header_layout)

        chart = Canvas(self, 32)
        # self.graph_layout = QtWidgets.QHBoxLayout()
        self.box1.addWidget(self.text_box)
        # self.graph_layout.addSpacing(200)
        self.box2.addWidget(chart)
        # self.graph_layout.setAlignment(Qt.AlignTop | Qt.AlignRight)
        self.box0.addLayout(self.box1)
        self.box0.addLayout(self.box2)
        self.box.addLayout(self.box0)

        self.Going_button = QtWidgets.QPushButton("Cancel")
        self.Going_button.setStyleSheet(
            "QPushButton { color: white; background-color: teal; font-size: %dpx; border-radius: %dpx; border: 1px solid black;}" % (
                20, 8))

        self.Going_button.setFixedSize(90, 35)
        self.buttons_box = QtWidgets.QHBoxLayout()
        self.buttons_box.addWidget(self.Going_button)
        self.buttons_box.setAlignment(Qt.AlignRight)

        # self.box.addLayout(self.graph_box)
        self.box.addLayout(self.buttons_box)

        self.outer_layout = QtWidgets.QVBoxLayout()
        self.outer_layout.setContentsMargins(50, 30, 50, 30)
        self.outer_layout.addWidget(self.inner_frame)

        self.outer_frame.setLayout(self.outer_layout)
        self.setLayout(self.outer_frame.layout())
        # self.setGeometry(100, 100, 500, 500)

        # self.Going_button.clicked.connect(self.Going_button_fun)

        self.Going_button.clicked.connect(self.switch_screen)

    def resizeEvent(self, event):
        super().resizeEvent(event)

    def Going_button_fun(self):
        print('Clicked going button')

    def switch_screen(self):
        self.parent().setCurrentIndex(10)
