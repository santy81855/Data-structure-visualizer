from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont
import config, DSButton

class ArrayWidget(QWidget):
    def __init__(self, parent):
        super(ArrayWidget, self).__init__()
        self.parent = parent