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
        self.Rozokar()

    def Rozokar(self):
        self.setWindowTitle("Payroll")
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("new3.jpg"))

        self.line1 = QLineEdit(self)
        self.line1.setFont(QFont('SansSerif', 14))
        self.line1.move(200, 170)
        self.line1.adjustSize()

        self.line2 = QLineEdit(self)
        self.line2.setFont(QFont('SansSerif', 14))
        self.line2.move(550, 170)
        self.line2.adjustSize()

        self.line3 = QLineEdit(self)
        self.line3.setFont(QFont('SansSerif', 14))
        self.line3.move(900, 170)
        self.line3.adjustSize()

        self.line4 = QLineEdit(self)
        self.line4.setFont(QFont('SansSerif', 14))
        self.line4.move(200, 345)
        self.line4.adjustSize()

        self.line5 = QLineEdit(self)
        self.line5.setFont(QFont('SansSerif', 14))
        self.line5.move(550, 345)
        self.line5.adjustSize()

        self.label1 = QLabel(self)
        self.label1.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Black))
        self.label1.setStyleSheet("color: rgb(255,255,255)")
        self.label1.setText('Employee ID')
        self.label1.adjustSize()
        self.label1.move(200, 120)

        self.label2 = QLabel(self)
        self.label2.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Black))
        self.label2.setStyleSheet("color: rgb(255,255,255)")
        self.label2.setText('Employee Name')
        self.label2.adjustSize()
        self.label2.move(550, 120)

        self.label3 = QLabel(self)
        self.label3.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Black))
        self.label3.setStyleSheet("color: rgb(255,255,255)")
        self.label3.setText('Basic Pay')
        self.label3.adjustSize()
        self.label3.move(900, 120)

        self.label4 = QLabel(self)
        self.label4.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Black))
        self.label4.setStyleSheet("color: rgb(255,255,255)")
        self.label4.setText('Overtime')
        self.label4.adjustSize()
        self.label4.move(200, 300)

        self.label5 = QLabel(self)
        self.label5.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Black))
        self.label5.setStyleSheet("color: rgb(255,255,255)")
        self.label5.setText('Bonus')
        self.label5.adjustSize()
        self.label5.move(550, 300)

        self.pushbutton1 = QPushButton("Back", self)
        self.pushbutton1.setFont(QFont('SansSerif', 16))
        self.pushbutton1.resize(self.pushbutton1.sizeHint())
        self.pushbutton1.move(680, 480)
        self.pushbutton1.clicked.connect(self.go_to_Weladmin)

        self.pushbutton2 = QPushButton("Submit", self)
        self.pushbutton2.setFont(QFont('SansSerif', 18))
        self.pushbutton2.resize(self.pushbutton2.sizeHint())
        self.pushbutton2.move(1000, 480)
        self.pushbutton2.clicked.connect(self.Submit)


        self.show()



    def go_to_Weladmin(self):
        from Weladmin import Voption
        self.obj=Voption()
        self.obj.show()
        self.close()

    def Submit(self):
        print("submitted Succesfully")








if __name__=="__main__":
    app=QApplication(sys.argv)
    Vopt=Voption()
    sys.exit(app.exec())