from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont
import config, DSButton

class DataStructurePage(QWidget):
    def __init__(self, parent):
        super(DataStructurePage, self).__init__()
        self.parent = parent
        # add a vertical layout
        self.dataStructureLayout = QHBoxLayout()
        self.dataStructureLayout.setSpacing(0)
        # add a button to the vertical layout for each data structure
        self.arrButton = DSButton.DataStructureButton(self, "Array")
        self.dataStructureLayout.addWidget(self.arrButton)
        self.linkedListButton = DSButton.DataStructureButton(self, "Linked List")
        self.dataStructureLayout.addWidget(self.linkedListButton)
        # set the vertical layout
        self.setLayout(self.dataStructureLayout)