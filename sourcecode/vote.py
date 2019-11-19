# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/vote.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from utils import goToContestant, goToMain


class VoteUI(object):
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(631, 399)
        Form.setMinimumSize(QtCore.QSize(631, 399))
        Form.setMaximumSize(QtCore.QSize(631, 399))
        Form.setStyleSheet("background-color: #2898cc;")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: #b5e7ff;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnResult_2 = QtWidgets.QPushButton(self.frame)
        self.btnResult_2.setGeometry(QtCore.QRect(30, 10, 179, 179))
        self.btnResult_2.setMinimumSize(QtCore.QSize(179, 179))
        self.btnResult_2.setStyleSheet("font: 14pt \"Myanmar Text\";\n"
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
        self.btnResult_2.setObjectName("btnResult_2")
        self.btnResult_3 = QtWidgets.QPushButton(self.frame)
        self.btnResult_3.setGeometry(QtCore.QRect(30, 190, 179, 179))
        self.btnResult_3.setMinimumSize(QtCore.QSize(179, 179))
        self.btnResult_3.setStyleSheet("font: 14pt \"Myanmar Text\";\n"
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
        self.btnResult_3.setObjectName("btnResult_3")
        self.btnResult_4 = QtWidgets.QPushButton(self.frame)
        self.btnResult_4.setGeometry(QtCore.QRect(220, 10, 179, 179))
        self.btnResult_4.setMinimumSize(QtCore.QSize(179, 179))
        self.btnResult_4.setStyleSheet("font: 14pt \"Myanmar Text\";\n"
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
        self.btnResult_4.setObjectName("btnResult_4")
        self.btnResult_5 = QtWidgets.QPushButton(self.frame)
        self.btnResult_5.setGeometry(QtCore.QRect(410, 10, 179, 179))
        self.btnResult_5.setMinimumSize(QtCore.QSize(179, 179))
        self.btnResult_5.setStyleSheet("font: 14pt \"Myanmar Text\";\n"
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
        self.btnResult_5.setObjectName("btnResult_5")
        self.btnResult_6 = QtWidgets.QPushButton(self.frame)
        self.btnResult_6.setGeometry(QtCore.QRect(220, 190, 179, 179))
        self.btnResult_6.setMinimumSize(QtCore.QSize(179, 179))
        self.btnResult_6.setStyleSheet("font: 14pt \"Myanmar Text\";\n"
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
        self.btnResult_6.setObjectName("btnResult_6")
        self.btnResult_7 = QtWidgets.QPushButton(self.frame)
        self.btnResult_7.setGeometry(QtCore.QRect(420, 190, 179, 179))
        self.btnResult_7.setMinimumSize(QtCore.QSize(179, 179))
        self.btnResult_7.setStyleSheet("font: 14pt \"Myanmar Text\";\n"
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
        self.btnResult_7.setObjectName("btnResult_7")
        self.btnVote0 = QtWidgets.QPushButton(self.frame)
        self.btnVote0.setGeometry(QtCore.QRect(70, 130, 111, 41))
        self.btnVote0.setStyleSheet("background-color:#b5e7ff;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"padding: 4px;\n"
"text-align: center;\n"
"border-color:white;")
        self.btnVote0.setObjectName("btnVote0")
        self.btnVote1 = QtWidgets.QPushButton(self.frame)
        self.btnVote1.setGeometry(QtCore.QRect(260, 130, 111, 41))
        self.btnVote1.setToolTipDuration(-1)
        self.btnVote1.setStyleSheet("background-color:#b5e7ff;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"padding: 4px;\n"
"text-align: center;\n"
"border-color:white;")
        self.btnVote1.setObjectName("btnVote1")
        self.btnVote2 = QtWidgets.QPushButton(self.frame)
        self.btnVote2.setGeometry(QtCore.QRect(450, 130, 111, 41))
        self.btnVote2.setStyleSheet("background-color:#b5e7ff;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"padding: 4px;\n"
"text-align: center;\n"
"border-color:white;")
        self.btnVote2.setObjectName("btnVote2")
        self.btnVote3 = QtWidgets.QPushButton(self.frame)
        self.btnVote3.setGeometry(QtCore.QRect(70, 310, 111, 41))
        self.btnVote3.setStyleSheet("background-color:#b5e7ff;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"padding: 4px;\n"
"text-align: center;\n"
"border-color:white;")
        self.btnVote3.setObjectName("btnVote3")
        self.btnVote4 = QtWidgets.QPushButton(self.frame)
        self.btnVote4.setGeometry(QtCore.QRect(260, 310, 111, 41))
        self.btnVote4.setStyleSheet("background-color:#b5e7ff;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"padding: 4px;\n"
"text-align: center;\n"
"border-color:white;")
        self.btnVote4.setObjectName("btnVote4")
        self.btnVote5 = QtWidgets.QPushButton(self.frame)
        self.btnVote5.setGeometry(QtCore.QRect(460, 310, 111, 41))
        self.btnVote5.setStyleSheet("background-color:#b5e7ff;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"padding: 4px;\n"
"text-align: center;\n"
"border-color:white;")
        self.btnVote5.setObjectName("btnVote5")
        self.btnView0 = QtWidgets.QPushButton(self.frame)
        self.btnView0.setGeometry(QtCore.QRect(60, 30, 111, 41))
        self.btnView0.setStyleSheet("background-color:#b5e7ff;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"padding: 4px;\n"
"text-align: center;\n"
"border-color:white;")
        self.btnView0.setObjectName("btnView0")


        self.btnView1 = QtWidgets.QPushButton(self.frame)
        self.btnView1.setGeometry(QtCore.QRect(260, 30, 111, 41))
        self.btnView1.setStyleSheet("background-color:#b5e7ff;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"padding: 4px;\n"
"text-align: center;\n"
"border-color:white;")
        self.btnView1.setObjectName("btnView1")
        self.btnView2 = QtWidgets.QPushButton(self.frame)
        self.btnView2.setGeometry(QtCore.QRect(450, 30, 111, 41))
        self.btnView2.setStyleSheet("background-color:#b5e7ff;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"padding: 4px;\n"
"text-align: center;\n"
"border-color:white;")
        self.btnView2.setObjectName("btnView2")
        self.btnView3 = QtWidgets.QPushButton(self.frame)
        self.btnView3.setGeometry(QtCore.QRect(60, 210, 111, 41))
        self.btnView3.setStyleSheet("background-color:#b5e7ff;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"padding: 4px;\n"
"text-align: center;\n"
"border-color:white;")
        self.btnView3.setObjectName("btnView3")
        self.btnView4 = QtWidgets.QPushButton(self.frame)
        self.btnView4.setGeometry(QtCore.QRect(260, 210, 111, 41))
        self.btnView4.setStyleSheet("background-color:#b5e7ff;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"padding: 4px;\n"
"text-align: center;\n"
"border-color:white;")
        self.btnView4.setObjectName("btnView4")
        self.btnView5 = QtWidgets.QPushButton(self.frame)
        self.btnView5.setGeometry(QtCore.QRect(460, 210, 111, 41))
        self.btnView5.setStyleSheet("background-color:#b5e7ff;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"padding: 4px;\n"
"text-align: center;\n"
"border-color:white;")
        self.btnView5.setObjectName("btnView5")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.btnView0.clicked.connect(lambda: self.goToContestant(0))
        self.btnView1.clicked.connect(lambda: self.goToContestant(1))
        self.btnView2.clicked.connect(lambda: self.goToContestant(2))
        self.btnView3.clicked.connect(lambda: self.goToContestant(3))
        self.btnView4.clicked.connect(lambda: self.goToContestant(4))
        self.btnView5.clicked.connect(lambda: self.goToContestant(5))

        self.btnVote0.clicked.connect(self.goToMain)
        self.btnVote1.clicked.connect(self.goToMain)
        self.btnVote2.clicked.connect(self.goToMain)
        self.btnVote3.clicked.connect(self.goToMain)
        self.btnVote4.clicked.connect(self.goToMain)
        self.btnVote5.clicked.connect(self.goToMain)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Vote"))
        self.btnResult_2.setText(_translate("Form", "Mr X"))
        self.btnResult_3.setText(_translate("Form", "Mr S"))
        self.btnResult_4.setText(_translate("Form", "Mr Y"))
        self.btnResult_5.setText(_translate("Form", "Mr Z"))
        self.btnResult_6.setText(_translate("Form", "MR T"))
        self.btnResult_7.setText(_translate("Form", "MR U"))
        self.btnVote0.setToolTip(_translate("Form", "Vote Candidate"))
        self.btnVote0.setText(_translate("Form", "ABP"))
        self.btnVote1.setToolTip(_translate("Form", "Vote Candidate"))
        self.btnVote1.setText(_translate("Form", "PRP"))
        self.btnVote2.setToolTip(_translate("Form", "Vote Candidate"))
        self.btnVote2.setText(_translate("Form", "DOP"))
        self.btnVote3.setToolTip(_translate("Form", "Vote Candidate"))
        self.btnVote3.setText(_translate("Form", "ZXP"))
        self.btnVote4.setToolTip(_translate("Form", "Vote Candidate"))
        self.btnVote4.setText(_translate("Form", "AAP"))
        self.btnVote5.setToolTip(_translate("Form", "Vote Candidate"))
        self.btnVote5.setText(_translate("Form", "OOP"))
        self.btnView0.setToolTip(_translate("Form", "Vote Candidate"))
        self.btnView0.setText(_translate("Form", "View"))
        self.btnView1.setToolTip(_translate("Form", "Vote Candidate"))
        self.btnView1.setText(_translate("Form", "View"))
        self.btnView2.setToolTip(_translate("Form", "Vote Candidate"))
        self.btnView2.setText(_translate("Form", "View"))
        self.btnView3.setToolTip(_translate("Form", "Vote Candidate"))
        self.btnView3.setText(_translate("Form", "View"))
        self.btnView4.setToolTip(_translate("Form", "Vote Candidate"))
        self.btnView4.setText(_translate("Form", "View"))
        self.btnView5.setToolTip(_translate("Form", "Vote Candidate"))
        self.btnView5.setText(_translate("Form", "View"))

    def goToContestant(self,index):
        goToContestant(self,index)

    def goToMain(self):
        goToMain(self)

