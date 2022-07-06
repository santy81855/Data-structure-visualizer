from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont
import config, ArrayPage

class DataStructureButton(QPushButton):
    def __init__(self, parent, text):
        super(DataStructureButton, self).__init__()
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
        config.mainWin.stackedWidget.setCurrentIndex(1)
        print("hello")