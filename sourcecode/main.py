# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from utils import goToWinner, goToAnnouncements, goToVote
import DataAccess,BusinessLogic, Dialog

class MainUI(object):

    def __init__(self,userId):
        self.userId = userId
        print("UserId is: ", userId)

    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(545, 418)
        Form.setMinimumSize(QtCore.QSize(545, 418))
        Form.setMaximumSize(QtCore.QSize(545, 418))
        Form.setStyleSheet("background-color: #2898cc;")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setMinimumSize(QtCore.QSize(527, 400))
        self.frame.setStyleSheet("background-color: #b5e7ff;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnResult = QtWidgets.QPushButton(self.frame)
        self.btnResult.setGeometry(QtCore.QRect(40, 40, 179, 179))
        self.btnResult.setMinimumSize(QtCore.QSize(179, 179))
        self.btnResult.setStyleSheet("font: 14pt \"Myanmar Text\";\n"
"background-color:#377896;\n"
"color:  white;\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:70px;\n"
"border-color: #fff;\n"
" max-width:175px;\n"
" max-height:175px;\n"
" min-width:175px;\n"
" min-height:175px;")
        self.btnResult.setObjectName("btnResult")
        self.btnResult.clicked.connect(self.goToAnnouncements)

        self.btnVote = QtWidgets.QPushButton(self.frame)
        self.btnVote.setGeometry(QtCore.QRect(310, 40, 179, 179))
        self.btnVote.setMinimumSize(QtCore.QSize(179, 179))
        self.btnVote.setStyleSheet("font: 14pt \"Myanmar Text\";\n"
"background-color:#377896;\n"
"color:  white;\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:70px;\n"
" border-color: white;\n"
" max-width:175px;\n"
" max-height:175px;\n"
" min-width:175px;\n"
" min-height:175px;")
        self.btnVote.setObjectName("btnVote")
        self.btnVote.clicked.connect(self.goToVote)

        self.btnWinner = QtWidgets.QPushButton(self.frame)
        self.btnWinner.setGeometry(QtCore.QRect(170, 220, 179, 179))
        self.btnWinner.setMinimumSize(QtCore.QSize(179, 179))
        self.btnWinner.setStyleSheet("background-color:#377896;\n"
"font: 14pt \"Myanmar Text\";\n"
"color:  white;\n"
" border-style: solid;\n"
" border-width:2px;\n"
" border-radius:70px;\n"
" border-color: white;\n"
" max-width:175px;\n"
" max-height:175px;\n"
" min-width:175px;\n"
" min-height:175px;")
        self.btnWinner.setObjectName("btnWinner")
        self.btnWinner.clicked.connect(self.goToWinner)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dashboard"))
        self.btnResult.setText(_translate("Form", "Result"))
        self.btnVote.setText(_translate("Form", "Vote"))
        self.btnWinner.setText(_translate("Form", "Winner"))

    def goToWinner(self):
        userVoted = DataAccess.getUserVoteStatus(self.userId)
        if not userVoted:
            Dialog.information_message(self.Form, 'You have to vote first to view it')
            return

        result = BusinessLogic.winnerUI()
        if result:
            name = result.get('Name')
            party = result.get('Party')
            percentage = result.get('Percentage')
            goToWinner(self, self.userId,name,party,percentage)
        else:
            Dialog.error_message(self.Form,'Data access error. Try again')

    def goToVote(self):
        result = BusinessLogic.getNamePartyPercentage()
        if result:
            goToVote(self, self.userId, result)
        else:
            Dialog.error_message(self.Form, 'Data access error. Try again')

    def goToAnnouncements(self):
        userVoted = DataAccess.getUserVoteStatus(self.userId)
        if not userVoted:
            Dialog.information_message(self.Form, 'You have to vote first to view it')
            return

        result = BusinessLogic.getNamePartyPercentage()
        if result:
            goToAnnouncements(self, self.userId,result)
        else:
            Dialog.error_message(self.Form, 'Data access error. Try again')

