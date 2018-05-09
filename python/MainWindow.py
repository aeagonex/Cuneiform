from os import getcwd

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from PyQt5.uic import loadUi
from PyQt5 import QtGui

from ui.toolbar import Toolbar

WIDTH = 800
HEIGHT = 600

class cuneiform(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle('Cuneiform')
    self.setStyleSheet('background-color:#343434')

    self.setCentralWidget(QWidget(self))
    self.hbox = QHBoxLayout()
    self.centralWidget().setLayout(self.hbox)
    self.hbox.addWidget(Toolbar(parent=self))

    self.setFixedSize(WIDTH, HEIGHT)

