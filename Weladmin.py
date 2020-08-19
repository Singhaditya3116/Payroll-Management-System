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
        self.setWindowTitle("Welcome Admin")
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("new3.jpg"))

        self.label1 = QLabel(self)
        self.label1.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Black))
        self.label1.setStyleSheet("color: rgb(255,255,255)")
        self.label1.setText('Edit Employee')
        self.label1.adjustSize()
        self.label1.move(550, 140)

        self.label2 = QLabel(self)
        self.label2.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Black))
        self.label2.setStyleSheet("color: rgb(255,255,255)")
        self.label2.setText('Employee Info')
        self.label2.adjustSize()
        self.label2.move(550, 400)

        self.pushbutton1=QPushButton("Add Employee",self)
        self.pushbutton1.setFont(QFont('SansSerif', 14))
        self.pushbutton1.resize(self.pushbutton1.sizeHint())
        self.pushbutton1.move(300, 260)
        self.pushbutton1.clicked.connect(self.linked_to_addemp)


        self.pushbutton2 = QPushButton("Edit Employee", self)
        self.pushbutton2.setFont(QFont('SansSerif', 14))
        self.pushbutton2.resize(self.pushbutton2.sizeHint())
        self.pushbutton2.move(580, 260)
        self.pushbutton2.clicked.connect(self.linked_to_editemp)

        self.pushbutton3 = QPushButton("Remove Employee", self)
        self.pushbutton3.setFont(QFont('SansSerif', 14))
        self.pushbutton3.resize(self.pushbutton3.sizeHint())
        self.pushbutton3.move(860, 260)
        self.pushbutton3.clicked.connect(self.go_to_remove)

        self.pushbutton4 = QPushButton("View Employee", self)
        self.pushbutton4.setFont(QFont('SansSerif', 14))
        self.pushbutton4.resize(self.pushbutton4.sizeHint())
        self.pushbutton4.move(280, 550)

        self.pushbutton5 = QPushButton("Attendance", self)
        self.pushbutton5.setFont(QFont('SansSerif', 14))
        self.pushbutton5.resize(self.pushbutton4.sizeHint())
        self.pushbutton5.move(500, 550)
        self.pushbutton5.clicked.connect(self.go_attend)

        self.pushbutton6 = QPushButton("Experience", self)
        self.pushbutton6.setFont(QFont('SansSerif', 14))
        self.pushbutton6.resize(self.pushbutton4.sizeHint())
        self.pushbutton6.move(720, 550)
        self.pushbutton6.clicked.connect(self.go_empexp)

        self.pushbutton7 = QPushButton("Payroll", self)
        self.pushbutton7.setFont(QFont('SansSerif', 14))
        self.pushbutton7.resize(self.pushbutton4.sizeHint())
        self.pushbutton7.move(940, 550)
        self.pushbutton7.clicked.connect(self.go_payroll)



        self.show()

    def linked_to_addemp(self):
        from addemp import Addemp
        self.Add_emp=Addemp()
        self.Add_emp.show()
        self.close()

    def linked_to_editemp(self):
        from editemp import Editemp
        self.Edit_emp=Editemp()
        self.Edit_emp.show()
        self.close()

    def go_to_remove(self):
        from remove import Voption
        self.Voption=Voption()
        self.Voption.show()
        self.close()

    def go_attend(self):
        from empattd import Voption
        self.Voption = Voption()
        self.Voption.show()
        self.close()

    def go_empexp(self):
        from empexp1 import Voption
        self.Voption = Voption()
        self.Voption.show()
        self.close()

    def go_payroll(self):
        from payroll import Voption
        self.Voption = Voption()
        self.Voption.show()
        self.close()
















if __name__=="__main__":
    app=QApplication(sys.argv)
    Vopt=Voption()
    sys.exit(app.exec())