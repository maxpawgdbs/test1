from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class NewWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window()

    def window(self):
        self.setWindowTitle("Title")
        self.resize(500, 500)
        self.move(300, 300)

        self.button = QPushButton("Click on me", self)
        self.button.resize(150, 50)
        self.button.move(175, 225)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewWindow()
    window.show()
    sys.exit(app.exec_())