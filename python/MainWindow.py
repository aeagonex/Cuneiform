from os import getcwd

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

class cuneiform(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle('Cuneiform')
    self.setStyleSheet('background-color:#343434')
    self.toolbar = self.addToolBar('Save')
    self.setGeometry(50, 50, 800, 600)