from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QSpacerItem, QSizePolicy
from PyQt5.QtCore    import Qt

from ui.button  import Button

class Toolbar(QWidget):
  def __init__(self, parent = None):
    super().__init__()

    button = QPushButton('Me!')
    strip = QHBoxLayout()
    strip.setAlignment(Qt.AlignTop)
    self.setLayout(strip)
    strip.addWidget(Button())

    verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
    strip.addItem(verticalSpacer)