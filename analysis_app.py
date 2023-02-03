import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from frames.save_info import SaveInfo
from frames.reference import Reference
from frames.what_to_do import WhatToDo
from frames.display_THC import DisplayTHC
from frames.are_you_sure import AreYouSure
from frames.ensure_clean import EnsureClean
from frames.welcome_screen import WelcomeScreen
from frames.ensure_clean_air import EnsureCleanAir
from frames.display_THC_data import DisplayTHCData
from frames.reference_success import ReferenceSuccess
from frames.ensure_pure_solvent import EnsurePureSolvent


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget()
        self.screen1 = WelcomeScreen(700, 500, 25, 25, 70, 70, 30)
        self.screen2 = WhatToDo()
        self.screen3 = DisplayTHCData()
        self.screen4 = Reference()
        self.screen5 = EnsureClean()
        self.screen6 = ReferenceSuccess()
        self.screen7 = SaveInfo()
        self.screen8 = EnsureCleanAir()
        self.screen9 = EnsurePureSolvent()
        self.screen10 = DisplayTHC()
        self.screen11 = AreYouSure(self)
        self.stack.addWidget(self.screen1)
        self.stack.addWidget(self.screen2)
        self.stack.addWidget(self.screen3)
        self.stack.addWidget(self.screen4)
        self.stack.addWidget(self.screen5)
        self.stack.addWidget(self.screen6)
        self.stack.addWidget(self.screen7)
        self.stack.addWidget(self.screen8)
        self.stack.addWidget(self.screen9)
        self.stack.addWidget(self.screen10)
        self.stack.addWidget(self.screen11)
        layout = QHBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.switch_screen)
        self.timer.start()

    def switch_screen(self):
        self.stack.setCurrentIndex(1)
        self.timer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
