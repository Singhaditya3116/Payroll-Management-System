import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QLabel, QLineEdit, QComboBox)
from PyQt5.QtGui import QFont,QPixmap
from PyQt5.QtCore import QRect
from PyQt5 import QtWidgets, QtGui

class Voption(QWidget):

    def __init__(self):
        super().__init__()
        self.top=100
        self.left=100
        self.width=1300
        self.height=840
        self.Rozokar1()

    def Rozokar1(self):
        self.setWindowTitle("Remove")
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("new3.jpg"))

        self.label1 = QLabel(self)
        self.label1.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Black))
        self.label1.setStyleSheet("color: rgb(255,255,255)")
        self.label1.setText('Employee Id')
        self.label1.adjustSize()
        self.label1.move(50, 25)

        self.line1 = QLineEdit(self)
        self.line1.setFont(QFont('SansSerif', 14))
        self.line1.move(250, 25)
        self.line1.adjustSize()

        self.pushbutton1=QPushButton("Back",self)
        self.pushbutton1.setFont(QFont('SansSerif', 14))
        self.pushbutton1.resize(self.pushbutton1.sizeHint())
        self.pushbutton1.move(180, 100)
        self.pushbutton1.clicked.connect(self.go_to_Weladmin)

        self.pushbutton2 = QPushButton("Remove", self)
        self.pushbutton2.setFont(QFont('SansSerif', 14))
        self.pushbutton2.resize(self.pushbutton1.sizeHint())
        self.pushbutton2.move(370, 100)
        self.pushbutton2.clicked.connect(self.go_to_Weladmin)


        self.show()

    def go_to_Weladmin(self):
        from Weladmin import Voption
        self.Voption = Voption()
        self.Voption.show()
        self.close()





if __name__=="__main__":
    app=QApplication(sys.argv)
    Vopt=Voption()
    sys.exit(app.exec())