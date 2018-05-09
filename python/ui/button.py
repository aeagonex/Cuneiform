
from os import getcwd

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore    import QSize
from PyQt5.QtGui     import QImage, QIcon, QPixmap, QColor
from PyQt5.QtCore    import Qt

SIZE = QSize(32, 32)

imageDir = getcwd() + "\\python\\ui\images\\"

class Button(QPushButton):
    def __init__(self):
      super().__init__()

      pixmap = QPixmap(imageDir + 'home.png')
      mask = pixmap.createMaskFromColor(QColor('transparent'), Qt.MaskInColor)
      pixmap.fill(QColor(150,150,150))
      pixmap.setMask(mask)

      icon = QIcon(pixmap)
      self.setIcon(icon)

      self.setFixedSize(SIZE)
      self.setIconSize(SIZE)

      self.setStyleSheet("border: 0px solid black; background: transparent")
