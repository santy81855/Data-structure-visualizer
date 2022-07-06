from PyQt5 import QtCore
from PyQt5 import QtTest
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont
import config, ArrayPage, DataBlock
import random

class AddButton(QPushButton):
    def __init__(self, parent, text):
        super(AddButton, self).__init__()
        self.parent = parent
        self.text = text
        self.setText(self.text)
        # make it a fixed size
        self.setFixedSize(200, 100)
        # make hte stylesheet for the button
        self.setStyleSheet("""
        background-color:"""+ config.accentColor1 + """;
        color:"""+ config.backgroundColor + """;
        border-radius:10px;
        """)
        # make a function on click
        self.clicked.connect(self.onClick)

    def onClick(self):
        print("hello")
        # if the create array button is pressed
        if self.text.lower() == 'create array':
            # pick a random number between 0 and 44
            num = random.randint(0, 45)
            self.parent.setCurrentIndex(1)
            # now make 5 memory blocks a different color starting with the random number
            # Also add a dataBlock to the right layout each time we use a block
            global arrayStructure
            for i in range(5):
                config.arrMemoryBlocks[num + i].used()
                QtTest.QTest.qWait(300)
                # identify the block if it is the first block
                if len(config.arrayStructure) == 0:
                    config.arrayStructure.append(DataBlock.DataBlock(self, config.arrMemoryBlocks[num + i].text, True))
                else:
                    config.arrayStructure.append(DataBlock.DataBlock(self, config.arrMemoryBlocks[num + i].text, False))
                # we want the memory blocks to build upwards
                if len(config.arrayStructure) == 1:
                    config.arrayPage.rightLayout.insertWidget(config.arrayPage.rightLayout.count(), config.arrayStructure[i])
                else:
                    config.arrayPage.rightLayout.insertWidget(config.arrayPage.rightLayout.count() - i, config.arrayStructure[i])
            
            