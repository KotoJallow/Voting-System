# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\register.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(565, 379)
        MainForm.setMinimumSize(QtCore.QSize(565, 379))
        MainForm.setMaximumSize(QtCore.QSize(565, 379))
        MainForm.setStyleSheet(" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #fa709a, stop:1 #fee140);")
        self.gridLayout = QtWidgets.QGridLayout(MainForm)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.Mainframe = QtWidgets.QFrame(MainForm)
        self.Mainframe.setMinimumSize(QtCore.QSize(547, 361))
        self.Mainframe.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #84fab0, stop:1 #8fd3f4);")
        self.Mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Mainframe.setObjectName("Mainframe")
        self.lblMiddleName = QtWidgets.QLabel(self.Mainframe)
        self.lblMiddleName.setGeometry(QtCore.QRect(100, 60, 111, 31))
        self.lblMiddleName.setStyleSheet("border-style: outset;\n"
"font: 25 12pt \"Malgun Gothic Semilight\";\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #333;\n"
"color: rgb(0, 0, 0);\n"
"padding: 1px;")
        self.lblMiddleName.setObjectName("lblMiddleName")
        self.cbGender = QtWidgets.QComboBox(self.Mainframe)
        self.cbGender.setGeometry(QtCore.QRect(230, 180, 211, 31))
        self.cbGender.setStyleSheet("border-style: outset;\n"
"font: 25 12pt \"Malgun Gothic Semilight\";\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #333;\n"
"color: rgb(0, 0, 0);\n"
"padding: 1px;")
        self.cbGender.setObjectName("cbGender")
        self.cbGender.addItem("")
        self.cbGender.addItem("")
        self.lineEditMiddleName = QtWidgets.QLineEdit(self.Mainframe)
        self.lineEditMiddleName.setGeometry(QtCore.QRect(230, 60, 211, 31))
        self.lineEditMiddleName.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #333;\n"
"padding: 4px;\n"
"")
        self.lineEditMiddleName.setObjectName("lineEditMiddleName")
        self.lineEditLastName = QtWidgets.QLineEdit(self.Mainframe)
        self.lineEditLastName.setGeometry(QtCore.QRect(230, 100, 211, 31))
        self.lineEditLastName.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #333;\n"
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
"border-color: #333;\n"
"color: rgb(0, 0, 0);\n"
"padding: 1px;")
        self.lblLastName.setObjectName("lblLastName")
        self.lineEditFirstName = QtWidgets.QLineEdit(self.Mainframe)
        self.lineEditFirstName.setGeometry(QtCore.QRect(230, 20, 211, 31))
        self.lineEditFirstName.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #c2e9fb, stop:1 #96e6a1);\n"
"padding: 4px;\n"
"")
        self.lineEditFirstName.setObjectName("lineEditFirstName")
        self.lblFirstName = QtWidgets.QLabel(self.Mainframe)
        self.lblFirstName.setGeometry(QtCore.QRect(100, 20, 111, 31))
        self.lblFirstName.setStyleSheet("border-style: outset;\n"
"font: 25 12pt \"Malgun Gothic Semilight\";\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #333;\n"
"color: rgb(0, 0, 0);\n"
"padding: 1px;")
        self.lblFirstName.setObjectName("lblFirstName")
        self.lineEditIdNumber = QtWidgets.QLineEdit(self.Mainframe)
        self.lineEditIdNumber.setGeometry(QtCore.QRect(230, 140, 211, 31))
        self.lineEditIdNumber.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #333;\n"
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
"border-color: #333;\n"
"color: rgb(0, 0, 0);\n"
"padding: 1px;")
        self.lblIdNumber.setObjectName("lblIdNumber")
        self.lblGender = QtWidgets.QLabel(self.Mainframe)
        self.lblGender.setGeometry(QtCore.QRect(100, 180, 111, 31))
        self.lblGender.setStyleSheet("border-style: outset;\n"
"font: 25 12pt \"Malgun Gothic Semilight\";\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #333;\n"
"color: rgb(0, 0, 0);\n"
"padding: 1px;")
        self.lblGender.setObjectName("lblGender")
        self.leftSideBarFrame = QtWidgets.QFrame(self.Mainframe)
        self.leftSideBarFrame.setGeometry(QtCore.QRect(0, -1, 91, 351))
        self.leftSideBarFrame.setMinimumSize(QtCore.QSize(81, 341))
        self.leftSideBarFrame.setStyleSheet(" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4facfe, stop:1 #00f2fe);")
        self.leftSideBarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftSideBarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftSideBarFrame.setObjectName("leftSideBarFrame")
        self.rightSideBarFrame = QtWidgets.QFrame(self.Mainframe)
        self.rightSideBarFrame.setGeometry(QtCore.QRect(450, 0, 101, 351))
        self.rightSideBarFrame.setMinimumSize(QtCore.QSize(101, 341))
        self.rightSideBarFrame.setStyleSheet(" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4facfe, stop:1 #00f2fe);")
        self.rightSideBarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightSideBarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightSideBarFrame.setObjectName("rightSideBarFrame")
        self.mainContentFrame = QtWidgets.QFrame(self.Mainframe)
        self.mainContentFrame.setGeometry(QtCore.QRect(89, -1, 361, 351))
        self.mainContentFrame.setStyleSheet("")
        self.mainContentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainContentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainContentFrame.setObjectName("mainContentFrame")
        self.btnSubmit = QtWidgets.QPushButton(self.mainContentFrame)
        self.btnSubmit.setGeometry(QtCore.QRect(100, 270, 171, 61))
        self.btnSubmit.setStyleSheet(" background-color: green;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:30px;\n"
" border-color: red;")
        self.btnSubmit.setObjectName("btnSubmit")
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
        self.cbGender.setItemText(0, _translate("MainForm", "Male"))
        self.cbGender.setItemText(1, _translate("MainForm", "Female"))
        self.lineEditMiddleName.setPlaceholderText(_translate("MainForm", "Enter your middle name"))
        self.lineEditLastName.setPlaceholderText(_translate("MainForm", "Enter your last name"))
        self.lblLastName.setText(_translate("MainForm", "Last Name"))
        self.lineEditFirstName.setPlaceholderText(_translate("MainForm", "Enter your first name"))
        self.lblFirstName.setText(_translate("MainForm", "First Name"))
        self.lineEditIdNumber.setPlaceholderText(_translate("MainForm", "Enter your voters id number name"))
        self.lblIdNumber.setText(_translate("MainForm", "ID Number"))
        self.lblGender.setText(_translate("MainForm", "Gender"))
        self.btnSubmit.setText(_translate("MainForm", "Submit"))


from resources import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QWidget()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())
