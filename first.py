import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QPixmap
from PyQt5.QtCore import QRect
from PyQt5 import QtWidgets, QtGui,QtCore
import pymysql
import mysql.connector



class Admin_login(QWidget):

    def __init__(self):
        super().__init__()
        self.top=100
        self.left=100
        self.width=1300
        self.height=840
        self.label1()


    def label1(self):
        self.setWindowTitle("Login")
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("new3.jpg"))

        self.label1 = QLabel(self)
        self.label1.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.label1.setStyleSheet("color: rgb(255,255,255)")
        self.label1.setText('Username')
        self.label1.adjustSize()
        self.label1.move(50, 50)

        self.label2 = QLabel(self)
        self.label2.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.label2.setStyleSheet("color: rgb(255,255,255)")
        self.label2.setText('Password')
        self.label2.adjustSize()
        self.label2.move(50, 180)

        self.line1 = QLineEdit(self)
        self.line1.setFont(QFont('SansSerif', 14))
        self.line1.move(200, 50)
        self.line1.adjustSize()

        self.line2 = QLineEdit(self)
        self.line2.setFont(QFont('SansSerif', 14))
        self.line2.move(200,180)
        self.line2.adjustSize()

        self.pushbutton1 = QPushButton("Login", self)
        self.pushbutton1.setFont(QFont('SansSerif', 14))
        self.pushbutton1.resize(self.pushbutton1.sizeHint())
        self.pushbutton1.move(300, 280)
        self.pushbutton1.clicked.connect(self.login)

        self.show()

    def login(self):
        username = self.line1.text()
        password = self.line2.text()

        try:
            self.mydb=mysql.connector.connect(host="singh",user="root",passwd="root",db="Empdatabase")
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute("SELECT * FROM login WHERE username=%s AND password=%s",(username,password))
            myresult = self.mycursor.fetchall()
            QMessageBox.about(self, "Login", "Succesfull")

        except:
            QMessageBox.about(self, "Login", "UnSuccesfull")



        '''if(len(myresult)>0):
            QMessageBox.about(self, "Login", "Succesfull")

            from Weladmin import Voption
            self.Vopt = Voption()
            self.Vopt.show()
            self.close()
        else:
            QMessageBox.about(self, "Login", "UnSuccesfull")'''


if __name__=="__main__":
    app = QApplication(sys.argv)
    admin =Admin_login()
    sys.exit(app.exec_())