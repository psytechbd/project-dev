import numpy as np
from PyQt5.QtCore import QTimer
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Canvas(FigureCanvas):

    def __init__(self, parent, dpi):
        fig, self.ax = plt.subplots(figsize=(8, 6), dpi=dpi)
        super().__init__(fig)
        self.setParent(parent)

        self.x = [0]
        self.y = [0]

        self.line, = self.ax.plot(self.x, self.y, 'b-')
        self.ax.set_title("Filename", fontweight='bold', fontsize=15)
        self.ax.set_xlabel("Time (minutes)", fontsize=15)
        self.ax.set_ylabel("THC Prediction (%)", fontsize=15)

        self.counter = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_figure)
        self.timer.start(5000)  # 5000 milliseconds = 5 seconds
        self.cursor = Cursor(self.ax, useblit=True, color='black', linewidth=1, linestyle='--')

        self.annotation = self.ax.annotate("", xy=(8, 8), xytext=(8, 8),
                                           textcoords="offset points",
                                           bbox=dict(boxstyle="round", fc="w"))
        self.annotation.set_visible(False)

        self.ax.figure.canvas.mpl_connect("motion_notify_event", self.hover)

    def update_figure(self):
        self.counter += 1
        self.x.append(self.counter)
        self.y.append(np.random.rand())
        self.line.set_data(self.x, self.y)
        self.ax.relim()
        self.ax.autoscale_view()
        self.draw()

    def hover(self, event):
        if event.inaxes == self.line.axes:
            x, y = event.xdata, event.ydata
            self.annotation.xy = x, y
            text = "Time: {:.2f}\nTHC: {:.2f}%".format(x, y)
            self.annotation.set_text(text)
            self.annotation.set_visible(True)
            self.draw()
        else:
            self.annotation.set_visible(False)
