from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QStackedWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QWidget
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont
import config, ArrayPage, AddButton

class LeftPage(QStackedWidget):
    def __init__(self, parent):
        super(LeftPage, self).__init__()
        self.parent = parent
        # create the font
        font = QFont()
        font.setFamily("Serif")
        font.setFixedPitch( True )
        font.setPointSize(10)
        self.setFont(font)
        # make hte stylesheet for the stacked layout
        self.setStyleSheet("""
        background-color:"""+ config.backgroundColor + """;
        color:"""+ config.accentColor1 + """;
        text-align:center;
        """)
        # create the buttons 
        self.createArr = AddButton.AddButton(self, "Create Array")
        # add the create array button to the stacked layout
        self.addWidget(self.createArr)
        # create a second widget to hold the array buttons
        self.arrayButtons = QWidget()
        # create a vertical layout to store the array buttons
        self.arrayButtonsLayout = QVBoxLayout()
        self.arrayButtonsLayout.setSpacing(0)

        self.addNumber = AddButton.AddButton(self, "Add Number")
        self.addString = AddButton.AddButton(self, "Add String")
        self.addObject = AddButton.AddButton(self, "Add Object")
        # add the array buttons to the layout
        self.arrayButtonsLayout.addWidget(self.addNumber)
        self.arrayButtonsLayout.addWidget(self.addString)
        self.arrayButtonsLayout.addWidget(self.addObject)

        # add the array buttons layout to the array buttons widget
        self.arrayButtons.setLayout(self.arrayButtonsLayout)
        # add the array buttons widget to the stacked layout
        self.addWidget(self.arrayButtons)


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