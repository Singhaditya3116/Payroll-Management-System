import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QLabel, QLineEdit, QComboBox)
from PyQt5.QtGui import QFont,QPixmap,QIcon
from PyQt5.QtCore import QRect
from PyQt5 import QtWidgets, QtGui



class Editemp(QWidget):

    def __init__(self):
        super().__init__()
        self.top=100
        self.left=100
        self.width=1300
        self.height=840
        self.Emp_Detail()

    def Emp_Detail(self):
        self.setWindowTitle("Edit Employee")
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("new3.jpg"))

        self.label1 = QLabel(self)
        self.label1.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Black))
        self.label1.setStyleSheet("color: rgb(255,255,255)")
        self.label1.setText('Employee Id')
        self.label1.adjustSize()
        self.label1.move(200, 125)

        self.label2 = QLabel(self)
        self.label2.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Black))
        self.label2.setStyleSheet("color: rgb(255,255,255)")
        self.label2.setText('Full Name')
        self.label2.adjustSize()
        self.label2.move(550, 125)

        self.label3 = QLabel(self)
        self.label3.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Black))
        self.label3.setStyleSheet("color: rgb(255,255,255)")
        self.label3.setText('Address')
        self.label3.adjustSize()
        self.label3.move(900, 125)

        self.label4 = QLabel(self)
        self.label4.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Black))
        self.label4.setStyleSheet("color: rgb(255,255,255)")
        self.label4.setText('Contact')
        self.label4.adjustSize()
        self.label4.move(200, 300)

        self.label5 = QLabel(self)
        self.label5.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Black))
        self.label5.setStyleSheet("color: rgb(255,255,255)")
        self.label5.setText('Email')
        self.label5.adjustSize()
        self.label5.move(550, 300)

        self.label6 = QLabel(self)
        self.label6.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Black))
        self.label6.setStyleSheet("color: rgb(255,255,255)")
        self.label6.setText('Designation')
        self.label6.adjustSize()
        self.label6.move(900, 300)

        self.label7 = QLabel(self)
        self.label7.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Black))
        self.label7.setStyleSheet("color: rgb(255,255,255)")
        self.label7.setText('Department')
        self.label7.adjustSize()
        self.label7.move(200, 450)

        self.label8 = QLabel(self)
        self.label8.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Black))
        self.label8.setStyleSheet("color: rgb(255,255,255)")
        self.label8.setText('Joined Date')
        self.label8.adjustSize()
        self.label8.move(550, 450)

        self.label9 = QLabel(self)
        self.label9.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Black))
        self.label9.setStyleSheet("color: rgb(255,255,255)")
        self.label9.setText('Worked Hour')
        self.label9.adjustSize()
        self.label9.move(900, 450)

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

        self.line6 = QLineEdit(self)
        self.line6.setFont(QFont('SansSerif', 14))
        self.line6.move(900, 345)
        self.line6.adjustSize()

        self.line7 = QLineEdit(self)
        self.line7.setFont(QFont('SansSerif', 14))
        self.line7.move(200, 495)
        self.line7.adjustSize()

        self.line8 = QLineEdit(self)
        self.line8.setFont(QFont('SansSerif', 14))
        self.line8.move(550, 495)
        self.line8.adjustSize()

        self.line9 = QLineEdit(self)
        self.line9.setFont(QFont('SansSerif', 14))
        self.line9.move(900, 495)
        self.line9.adjustSize()

        self.pushbutton1 = QPushButton("  Back", self)
        self.pushbutton1.setFont(QFont('SansSerif', 18))
        self.pushbutton1.setIcon(QIcon(QPixmap("back.png")))
        self.pushbutton1.resize(self.pushbutton1.sizeHint())
        self.pushbutton1.move(600, 600)
        self.pushbutton1.clicked.connect(self.goback)

        self.pushbutton2 = QPushButton("Submit", self)
        self.pushbutton2.setFont(QFont('SansSerif', 18))
        self.pushbutton2.resize(self.pushbutton2.sizeHint())
        self.pushbutton2.move(1000, 600)
        self.pushbutton2.clicked.connect(self.Submit)

        self.show()



    def goback(self):
        from Weladmin import Voption
        self.obj=Voption()
        self.obj.show()
        self.close()

    def Submit(self):
        print("submitted Succesfully")






if __name__=="__main__":
    app=QApplication(sys.argv)
    emp=Editemp()
    sys.exit(app.exec())
