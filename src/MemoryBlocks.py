from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont
import config, ArrayPage

class MemoryBlock(QLabel):
    def __init__(self, parent, text):
        super(MemoryBlock, self).__init__()
        self.parent = parent
        self.text = text
        self.setText(self.text)
        # make it a fixed size
        self.setFixedSize(40, 40)
        # create the font
        font = QFont()
        font.setFamily("Serif")
        font.setFixedPitch( True )
        font.setPointSize(10)
        self.setFont(font)
        # make hte stylesheet for the button
        self.setStyleSheet("""
        background-color:"""+ config.accentColor1 + """;
        color:"""+ config.backgroundColor + """;
        text-align:center;
        """)
        # variable to track if the block is used
        self.isUsed = False
    
    # function that makes the buttons inverted colors
    def used(self):
        self.setStyleSheet("""
        background-color:"""+ config.accentColor2 + """;
        color:"""+ config.accentColor1 + """;
        text-align:center;
        """)
        self.isUsed = True
    
    def unused(self):
        self.setStyleSheet("""
        background-color:"""+ config.accentColor1 + """;
        color:"""+ config.backgroundColor + """;
        text-align:center;
        """)
        self.isUsed = False