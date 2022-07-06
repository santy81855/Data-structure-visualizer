from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QStackedLayout
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont
import config, DSButton, AddButton, MemoryBlocks, LeftPage

class ArrayWidget(QWidget):
    def __init__(self, parent):
        super(ArrayWidget, self).__init__()
        global arrayPage
        self.parent = parent
        config.arrayPage = self
        # add a horizontal layout so we can split the screen into 2 parts
        self.layout = QHBoxLayout()
        self.layout.setSpacing(20)

        # create left, middle and right vertical layouts
        self.leftLayout = QVBoxLayout()
        self.leftLayout.setSpacing(0)
        self.middleLayout = QVBoxLayout()
        self.middleLayout.setSpacing(0)
        self.rightLayout = QVBoxLayout()
        self.rightLayout.setSpacing(5)
        self.rightLayout.addStretch(-1)

        # add the left and right layouts to the horizontal layout
        self.layout.addLayout(self.leftLayout, 33)
        self.layout.addLayout(self.middleLayout, 33)
        
        self.layout.addLayout(self.rightLayout, 33)
        

        # create the left page
        self.leftPage = LeftPage.LeftPage(self)

        # create the mock memory blocks using a QGridLayout
        self.memoryLayout = QGridLayout()
        self.memoryLayout.setSpacing(5)

        # create an array of widgets to represent the memory blocks
        # pass in the size they should be depending on the current size of the mainWin
        self.memoryBlocks = []
        for i in range(0, 50):
            self.memoryBlocks.append(MemoryBlocks.MemoryBlock(self.parent, "0x0{}".format(i)))
        global arrMemoryBlocks
        config.arrMemoryBlocks = self.memoryBlocks
        
        # add the array to the grid layout making it only 10 per row
        for i in range(0, 50):
            self.memoryLayout.addWidget(self.memoryBlocks[i], i // 10, i % 10)
        

        # add the left page to the left layout
        self.leftLayout.addWidget(self.leftPage)

        # add the memory layout to the middle layout
        self.middleLayout.addStretch(-1)
        self.middleLayout.addLayout(self.memoryLayout)
        self.middleLayout.addStretch(-1)

        # add the horizontal layout to the main widget
        self.setLayout(self.layout)