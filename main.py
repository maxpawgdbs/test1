from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5 import uic
from random import randint
import sys


class NewWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.do_draw = False
        uic.loadUi("UI.ui", self)

        self.button.clicked.connect(self.function)

    def function(self):
        self.do_draw = True
        self.update()

    def paintEvent(self, event):
        if self.do_draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_krug(qp)
            qp.end()

    def draw_krug(self, qp):
        for i in range(10):
            radius = randint(20, 100)
            color = QColor(255, 255, 0)
            pos = QPoint(randint(1, 500), randint(1, 500))

            qp.setBrush(color)
            qp.drawEllipse(pos, radius, radius)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewWindow()
    window.show()
    sys.exit(app.exec_())
