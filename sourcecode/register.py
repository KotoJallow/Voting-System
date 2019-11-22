# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/register.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import DataAccess, Dialog
from utils import goToLogin

class RegisterUI(object):
    def setupUi(self, MainForm):
        self.Form = MainForm
        MainForm.setObjectName("MainForm")
        MainForm.resize(565, 379)
        MainForm.setMinimumSize(QtCore.QSize(565, 379))
        MainForm.setMaximumSize(QtCore.QSize(565, 379))

        MainForm.setStyleSheet("background-color: #2898cc;")
        self.gridLayout = QtWidgets.QGridLayout(MainForm)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.Mainframe = QtWidgets.QFrame(MainForm)
        self.Mainframe.setMinimumSize(QtCore.QSize(547, 361))
        self.Mainframe.setStyleSheet("background-color: #b5e7ff;;")
        self.Mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Mainframe.setObjectName("Mainframe")
        self.lblMiddleName = QtWidgets.QLabel(self.Mainframe)
        self.lblMiddleName.setGeometry(QtCore.QRect(100, 60, 111, 31))
        self.lblMiddleName.setStyleSheet("border-style: outset;\n"
"font: 25 12pt \"Malgun Gothic Semilight\";\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #fff;\n"
"color: white;\n"
"padding: 1px;\n"
"background-color:#377896;")
        self.lblMiddleName.setObjectName("lblMiddleName")
        self.cbGender = QtWidgets.QComboBox(self.Mainframe)
        self.cbGender.setGeometry(QtCore.QRect(230, 180, 211, 31))
        self.cbGender.setStyleSheet("border-style: outset;\n"
"font: 25 12pt \"Malgun Gothic Semilight\";\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #fff;\n"
"padding: 1px;")
        self.cbGender.setObjectName("cbGender")
        self.cbGender.addItem("")
        self.cbGender.addItem("")
        self.cbGender.addItem("")
        self.lineEditMiddleName = QtWidgets.QLineEdit(self.Mainframe)
        self.lineEditMiddleName.setGeometry(QtCore.QRect(230, 60, 211, 31))
        self.lineEditMiddleName.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #fff;\n"
"background-color:white;\n"
"padding: 4px;\n"
"")
        self.lineEditMiddleName.setObjectName("lineEditMiddleName")
        self.lineEditLastName = QtWidgets.QLineEdit(self.Mainframe)
        self.lineEditLastName.setGeometry(QtCore.QRect(230, 100, 211, 31))
        self.lineEditLastName.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #fff;\n"
"background-color:white;\n"
"padding: 4px;\n"
"")
        self.lineEditLastName.setText("")
        self.lineEditLastName.setObjectName("lineEditLastName")
        self.lblLastName = QtWidgets.QLabel(self.Mainframe)
        self.lblLastName.setGeometry(QtCore.QRect(100, 100, 111, 31))
        self.lblLastName.setStyleSheet("border-style: outset;\n"
"font: 25 12pt \"Malgun Gothic Semilight\";\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #fff;\n"
"color: #fff;\n"
"padding: 1px;\n"
"background-color:#377896;")
        self.lblLastName.setObjectName("lblLastName")
        self.lineEditFirstName = QtWidgets.QLineEdit(self.Mainframe)
        self.lineEditFirstName.setGeometry(QtCore.QRect(230, 20, 211, 31))
        self.lineEditFirstName.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"background-color: #fff;\n"
"border-color: #fff;\n"
"padding: 4px;\n"
"")
        self.lineEditFirstName.setObjectName("lineEditFirstName")
        self.lblFirstName = QtWidgets.QLabel(self.Mainframe)
        self.lblFirstName.setGeometry(QtCore.QRect(100, 20, 111, 31))
        self.lblFirstName.setStyleSheet("border-style: outset;\n"
"font: 25 12pt \"Malgun Gothic Semilight\";\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #fff;\n"
"color:white;\n"
"padding: 1px;\n"
"background-color:#377896;")
        self.lblFirstName.setObjectName("lblFirstName")
        self.lineEditIdNumber = QtWidgets.QLineEdit(self.Mainframe)
        self.lineEditIdNumber.setGeometry(QtCore.QRect(230, 140, 211, 31))
        self.lineEditIdNumber.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #fff;\n"
"background-color:white;\n"
"padding: 4px;\n"
"")
        self.lineEditIdNumber.setText("")
        self.lineEditIdNumber.setObjectName("lineEditIdNumber")
        self.lblIdNumber = QtWidgets.QLabel(self.Mainframe)
        self.lblIdNumber.setGeometry(QtCore.QRect(100, 140, 111, 31))
        self.lblIdNumber.setStyleSheet("border-style: outset;\n"
"font: 25 12pt \"Malgun Gothic Semilight\";\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #fff;\n"
"color:#fff;\n"
"padding: 1px;\n"
"background-color:#377896;")
        self.lblIdNumber.setObjectName("lblIdNumber")
        self.lblGender = QtWidgets.QLabel(self.Mainframe)
        self.lblGender.setGeometry(QtCore.QRect(100, 180, 111, 31))
        self.lblGender.setStyleSheet("border-style: outset;\n"
"font: 25 12pt \"Malgun Gothic Semilight\";\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #fff;\n"
"color: white;\n"
"background-color:#377896;\n"
"padding: 1px;")
        self.lblGender.setObjectName("lblGender")
        self.leftSideBarFrame = QtWidgets.QFrame(self.Mainframe)
        self.leftSideBarFrame.setGeometry(QtCore.QRect(0, -1, 91, 351))
        self.leftSideBarFrame.setMinimumSize(QtCore.QSize(81, 341))
        self.leftSideBarFrame.setStyleSheet("")
        self.leftSideBarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftSideBarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftSideBarFrame.setObjectName("leftSideBarFrame")
        self.rightSideBarFrame = QtWidgets.QFrame(self.Mainframe)
        self.rightSideBarFrame.setGeometry(QtCore.QRect(450, 0, 101, 351))
        self.rightSideBarFrame.setMinimumSize(QtCore.QSize(101, 341))
        self.rightSideBarFrame.setStyleSheet("")
        self.rightSideBarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightSideBarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightSideBarFrame.setObjectName("rightSideBarFrame")
        self.mainContentFrame = QtWidgets.QFrame(self.Mainframe)
        self.mainContentFrame.setGeometry(QtCore.QRect(89, -1, 361, 351))
        self.mainContentFrame.setStyleSheet("background-color:#377896;")
        self.mainContentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainContentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainContentFrame.setObjectName("mainContentFrame")
        self.btnSubmit = QtWidgets.QPushButton(self.mainContentFrame)
        self.btnSubmit.setGeometry(QtCore.QRect(100, 270, 171, 61))
        self.btnSubmit.setStyleSheet("background-color:#b5e7ff;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:30px;\n"
" border-color: white;")
        self.btnSubmit.setObjectName("btnSubmit")
        self.btnSubmit.clicked.connect(self.goToLogin)

        self.lineEditPassword = QtWidgets.QLineEdit(self.mainContentFrame)
        self.lineEditPassword.setGeometry(QtCore.QRect(140, 220, 211, 31))
        self.lineEditPassword.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #fff;\n"
"background-color:white;\n"
"padding: 4px;\n"
"")
        self.lineEditPassword.setText("")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.lblPassword = QtWidgets.QLabel(self.mainContentFrame)
        self.lblPassword.setGeometry(QtCore.QRect(10, 220, 111, 31))
        self.lblPassword.setStyleSheet("border-style: outset;\n"
"font: 25 12pt \"Malgun Gothic Semilight\";\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #fff;\n"
"color:#fff;\n"
"padding: 1px;\n"
"background-color:#377896;")
        self.lblPassword.setObjectName("lblPassword")
        self.mainContentFrame.raise_()
        self.lblMiddleName.raise_()
        self.cbGender.raise_()
        self.lineEditMiddleName.raise_()
        self.lineEditLastName.raise_()
        self.lblLastName.raise_()
        self.lineEditFirstName.raise_()
        self.lblFirstName.raise_()
        self.lineEditIdNumber.raise_()
        self.lblIdNumber.raise_()
        self.lblGender.raise_()
        self.leftSideBarFrame.raise_()
        self.rightSideBarFrame.raise_()
        self.gridLayout.addWidget(self.Mainframe, 0, 0, 1, 1)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Registration"))
        self.lblMiddleName.setText(_translate("MainForm", "Middle Name"))
        self.cbGender.setItemText(0, _translate("MainForm", "Select Gender"))
        self.cbGender.setItemText(1, _translate("MainForm", "Male"))
        self.cbGender.setItemText(2, _translate("MainForm", "Female"))
        self.lineEditMiddleName.setPlaceholderText(_translate("MainForm", "Enter your middle name"))
        self.lineEditLastName.setPlaceholderText(_translate("MainForm", "Enter your last name"))
        self.lblLastName.setText(_translate("MainForm", "Last Name"))
        self.lineEditFirstName.setPlaceholderText(_translate("MainForm", "Enter your first name"))
        self.lblFirstName.setText(_translate("MainForm", "First Name"))
        self.lineEditIdNumber.setPlaceholderText(_translate("MainForm", "Enter your voters id number"))
        self.lblIdNumber.setText(_translate("MainForm", "ID Number"))
        self.lblGender.setText(_translate("MainForm", "Gender"))
        self.btnSubmit.setText(_translate("MainForm", "Submit"))
        self.lineEditPassword.setPlaceholderText(_translate("MainForm", "Enter your voters id number name"))
        self.lblPassword.setText(_translate("MainForm", "Password"))

    def goToLogin(self):
        firstname = self.lineEditFirstName.text().strip()
        middlename = self.lineEditMiddleName.text().strip()
        lastname = self.lineEditLastName.text().strip()
        idnumber = self.lineEditIdNumber.text().strip()
        gender = self.cbGender.currentIndex()
        password = self.lineEditPassword.text().strip()

        validGender = 1<=gender<=2
        validInput = firstname and lastname and idnumber and password and validGender

        if validInput:
            result = DataAccess.insertUser(firstname,middlename,lastname,idnumber,gender,password)
            if result:
                Dialog.information_message(self.Form,'Registration successful')
                goToLogin(self)
            else:
                Dialog.error_message(self.Form,'Data insertion error. Try again\nId numbers should be unique')
        else:
            Dialog.warning_message(self.Form,"A valid gender is required and All fields requires save middle name.")


