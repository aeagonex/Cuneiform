from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

import sys

def start():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(128,102)
    w.move(0, 0)
    w.setWindowTitle('Simple')
    btn = QtWidgets.QPushButton("Hi")
    btn.move(50, 50)
    btn.resize(btn.sizeHint())
    w.show()

    sys.exit(app.exec_())

start()