#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import cuneiform

def initialize():
  app=QApplication(sys.argv)
  widget=cuneiform()
  widget.show()
  sys.exit(app.exec_())

# main()
initialize()
