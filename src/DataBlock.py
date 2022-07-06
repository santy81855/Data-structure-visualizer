from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont
import config, ArrayPage

class DataBlock(QWidget):
    def __init__(self, parent, text, isFirst):
        super(DataBlock, self).__init__()
        self.parent = parent
        self.text = text
        # create the font
        font = QFont()
        font.setFamily("Serif")
        font.setFixedPitch( True )
        font.setPointSize(10)
        # create the horizontal laout htat will hold the button and the label
        self.layout = QHBoxLayout()
        self.layout.setSpacing(10)
        self.layout.addStretch(-1)
        # create the text that will show the location of the block
        self.blockText = QLabel(self)
        self.blockText.setStyleSheet("""
        background-color:"""+ config.backgroundColor + """;
        color:"""+ config.accentColor1 + """;
        text-align:center;
        """)
        self.blockText.setFont(font)
        self.blockText.setText(self.text)

        # create a vertical layout to be able to center the block text
        self.blockTextLayout = QVBoxLayout()
        self.blockTextLayout.setSpacing(0)
        
        self.blockTextLayout.addStretch(-1)
        self.blockTextLayout.addWidget(self.blockText)
        self.blockTextLayout.addStretch(-1)

        # add the block text layout to the horizontal layout
        self.layout.addLayout(self.blockTextLayout)

        # make the widget a fixed height
        self.setFixedHeight(100)

        # create the datablock label
        self.block = QLabel(self)
        self.block.setFixedWidth(200)
        self.block.setStyleSheet("""
        background-color:"""+ config.accentColor1 + """;
        color:"""+ config.backgroundColor + """;
        text-align:center;
        """)
        self.block.setFont(font)
        self.block.setText("Null")
        # add the datablock label to the horizontal layout
        self.layout.addWidget(self.block)
        # set the layout
        self.setLayout(self.layout)
        # make the stylesheet for the widget
        self.setStyleSheet("""
        background-color:"""+ config.backgroundColor + """;
        """)
        # variable to track if the block is the first one
        self.first = isFirst
    
    # function that makes the buttons inverted colors
    def used(self):
        self.setStyleSheet("""
        background-color:"""+ config.accentColor2 + """;
        color:"""+ config.accentColor1 + """;
        text-align:center;
        """)
    
    def unused(self):
        self.setStyleSheet("""
        background-color:"""+ config.accentColor1 + """;
        color:"""+ config.backgroundColor + """;
        text-align:center;
        """)