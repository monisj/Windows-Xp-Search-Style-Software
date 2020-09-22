from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class BlinkButton(QPushButton):
    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)
        self.default_color = self.getColor()

    def getColor(self):
        return self.palette().color(QPalette.Button)

    def setColor(self, value):
        if value == self.getColor():
            return
        palette = self.palette()
        palette.setColor(self.backgroundRole(), value)
        self.setAutoFillBackground(True)
        self.setPalette(palette)

    def reset_color(self):
        self.setColor(self.default_color)

    color = pyqtProperty(QColor, getColor, setColor)


class Widget(QWidget):

    def __init__(self):
        super(Widget, self).__init__()

        self.resize(300,200)
        layout = QVBoxLayout(self)

        self.button_stop = BlinkButton("Stop")
        layout.addWidget(self.button_stop)

        self.button_start = QPushButton("Start", self)
        layout.addWidget(self.button_start)

        self.animation = QPropertyAnimation(self.button_stop, "color", self)
        self.animation.setDuration(1000)
        self.animation.setLoopCount(100)
        self.animation.setStartValue(self.button_stop.default_color)
        self.animation.setEndValue(self.button_stop.default_color)
        self.animation.setKeyValueAt(0.1, QColor(0,255,0))

        self.button_start.clicked.connect(self.animation.start)
        self.button_stop.clicked.connect(self.stop)

    def stop(self):
        self.animation.stop()
        self.button_stop.reset_color()


