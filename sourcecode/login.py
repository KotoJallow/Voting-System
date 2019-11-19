# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/login.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from utils import goToMain, goToRegister


class LoginUI(object):
    def setupUi(self, MainForm):
        self.Form = MainForm
        MainForm.setObjectName("MainForm")
        MainForm.resize(631, 399)
        MainForm.setMinimumSize(QtCore.QSize(631, 399))
        MainForm.setMaximumSize(QtCore.QSize(631, 399))
        MainForm.setStyleSheet("background-color: #2898cc;")
        self.gridLayout = QtWidgets.QGridLayout(MainForm)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.MainFrame = QtWidgets.QFrame(MainForm)
        self.MainFrame.setMinimumSize(QtCore.QSize(613, 0))
        self.MainFrame.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.MainFrame.setStyleSheet("background-color: #b5e7ff;")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.MainFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frameBody = QtWidgets.QFrame(self.MainFrame)
        self.frameBody.setMinimumSize(QtCore.QSize(391, 211))
        self.frameBody.setStyleSheet("border-style: outset;\n"
                                     "background-color:#377896;\n"
                                     "border-width: 2px;\n"
                                     "border-radius: 15px;\n"
                                     "border-color: #b9daea;\n"
                                     "padding: 4px;")
        self.frameBody.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBody.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBody.setObjectName("frameBody")
        self.lblUsername = QtWidgets.QLabel(self.frameBody)
        self.lblUsername.setGeometry(QtCore.QRect(20, 20, 81, 41))
        self.lblUsername.setStyleSheet("color:white;\n"
                                       "border-style: outset;\n"
                                       "border-width: 2px;\n"
                                       "border-radius: 15px;\n"
                                       "border-color: #b9daea;\n"
                                       "padding: 4px;\n"
                                       "")
        self.lblUsername.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUsername.setObjectName("lblUsername")
        self.lineEditUserName = QtWidgets.QLineEdit(self.frameBody)
        self.lineEditUserName.setGeometry(QtCore.QRect(130, 20, 241, 41))
        self.lineEditUserName.setStyleSheet("border-style: outset;\n"
                                            "border-width: 2px;\n"
                                            "border-radius: 15px;\n"
                                            "padding: 4px;\n"
                                            "background-color: #fff;")
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.lineEditPassword = QtWidgets.QLineEdit(self.frameBody)
        self.lineEditPassword.setGeometry(QtCore.QRect(130, 70, 241, 41))
        self.lineEditPassword.setStyleSheet("background-color: #fff;\n"
                                            "border-style: outset;\n"
                                            "border-width: 2px;\n"
                                            "border-radius: 15px;\n"
                                            "border-color: #b9daea;\n"
                                            "padding: 4px;")
        self.lineEditPassword.setText("")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.lblPassword = QtWidgets.QLabel(self.frameBody)
        self.lblPassword.setGeometry(QtCore.QRect(20, 70, 81, 41))
        self.lblPassword.setStyleSheet("color: white;\n"
                                       "border-style: outset;\n"
                                       "border-width: 2px;\n"
                                       "border-radius: 15px;\n"
                                       "border-color: #b9daea;\n"
                                       "padding: 4px;\n"
                                       "text-align: center;")
        self.lblPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPassword.setObjectName("lblPassword")
        self.btnLogIn = QtWidgets.QPushButton(self.frameBody)
        self.btnLogIn.setGeometry(QtCore.QRect(260, 120, 111, 41))
        self.btnLogIn.setStyleSheet("background-color:#b5e7ff;")
        self.btnLogIn.setObjectName("btnLogIn")
        self.btnLogIn.clicked.connect(self.goToMain)

        self.btnRegister = QtWidgets.QPushButton(self.frameBody)
        self.btnRegister.setGeometry(QtCore.QRect(130, 120, 111, 41))
        self.btnRegister.setStyleSheet("background-color:#b5e7ff;\n"
                                       "border-style: outset;\n"
                                       "border-width: 2px;\n"
                                       "border-radius: 15px;\n"
                                       "padding: 4px;\n"
                                       "text-align: center;")
        self.btnRegister.setObjectName("btnRegister")
        self.btnRegister.clicked.connect(self.goToRegister)

        self.lineEditUserName.raise_()
        self.lineEditPassword.raise_()
        self.lblPassword.raise_()
        self.btnLogIn.raise_()
        self.btnRegister.raise_()
        self.lblUsername.raise_()
        self.gridLayout_2.addWidget(self.frameBody, 1, 1, 1, 1)
        self.frameHeader = QtWidgets.QFrame(self.MainFrame)
        self.frameHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameHeader.setObjectName("frameHeader")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameHeader)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnTitle = QtWidgets.QPushButton(self.frameHeader)
        self.btnTitle.setMinimumSize(QtCore.QSize(571, 41))
        self.btnTitle.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnTitle.setStyleSheet("background-color:#377896;\n"
                                    "border-color: #b9daea;\n"
                                    "font: 16pt \"MS Shell Dlg 2\";\n"
                                    "color: white;\n"
                                    "border-style: outset;\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 15px;\n"
                                    "padding: 4px;\n"
                                    "text-align: center;")
        self.btnTitle.setObjectName("btnTitle")
        self.horizontalLayout.addWidget(self.btnTitle)
        self.gridLayout_2.addWidget(self.frameHeader, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(17, 74, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "E-Voting System"))
        self.lblUsername.setText(_translate("MainForm", "Username"))
        self.lineEditUserName.setPlaceholderText(_translate("MainForm", "Enter your voters id number"))
        self.lineEditPassword.setPlaceholderText(_translate("MainForm", "Enter your password"))
        self.lblPassword.setText(_translate("MainForm", "Password"))
        self.btnLogIn.setText(_translate("MainForm", "Log In"))
        self.btnRegister.setText(_translate("MainForm", "Register"))
        self.btnTitle.setText(_translate("MainForm", "Electronic Voting System"))

    def goToMain(self):
        goToMain(self)

    def goToRegister(self):
        goToRegister(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QWidget()
    ui = LoginUI()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())
