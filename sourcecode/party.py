# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/party.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from utils import goToContestant

class PartyUI(object):
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
        self.frame.setStyleSheet("background-color: #b5e7ff;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(30, 20, 551, 80))
        self.frame_2.setStyleSheet("background-color:#377896;\n"
"border-color: #b9daea;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"padding: 4px;\n"
"text-align: center;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 201, 31))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 491, 31))
        self.label_2.setObjectName("label_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(30, 110, 551, 191))
        self.frame_3.setMinimumSize(QtCore.QSize(551, 191))
        self.frame_3.setMaximumSize(QtCore.QSize(551, 191))
        self.frame_3.setStyleSheet("background-color:white;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setGeometry(QtCore.QRect(10, 32, 531, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame_3)
        self.line_2.setGeometry(QtCore.QRect(10, 94, 531, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame_3)
        self.line_3.setGeometry(QtCore.QRect(10, 63, 531, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame_3)
        self.line_4.setGeometry(QtCore.QRect(10, 156, 531, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.frame_3)
        self.line_5.setGeometry(QtCore.QRect(10, 125, 531, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(20, 80, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(20, 110, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(20, 140, 81, 16))
        self.label_7.setObjectName("label_7")
        self.lblLeader = QtWidgets.QLabel(self.frame_3)
        self.lblLeader.setGeometry(QtCore.QRect(190, 20, 351, 16))
        self.lblLeader.setObjectName("lblLeader")
        self.lblYearEstablished = QtWidgets.QLabel(self.frame_3)
        self.lblYearEstablished.setGeometry(QtCore.QRect(190, 50, 351, 16))
        self.lblYearEstablished.setObjectName("lblYearEstablished")
        self.lblMotto = QtWidgets.QLabel(self.frame_3)
        self.lblMotto.setGeometry(QtCore.QRect(190, 80, 351, 16))
        self.lblMotto.setObjectName("lblMotto")
        self.lblPhoneNumber = QtWidgets.QLabel(self.frame_3)
        self.lblPhoneNumber.setGeometry(QtCore.QRect(190, 140, 351, 16))
        self.lblPhoneNumber.setObjectName("lblPhoneNumber")
        self.lblAddress = QtWidgets.QLabel(self.frame_3)
        self.lblAddress.setGeometry(QtCore.QRect(190, 110, 351, 16))
        self.lblAddress.setObjectName("lblAddress")
        self.btnClose = QtWidgets.QPushButton(self.frame)
        self.btnClose.setGeometry(QtCore.QRect(220, 310, 171, 61))
        self.btnClose.setStyleSheet("background-color:#377896;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:30px;\n"
" border-color: white;\n"
"color:white;")
        self.btnClose.setObjectName("btnClose")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.btnClose.clicked.connect(self.goToContestant)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Party"))
        self.label.setText(_translate("Form", "ABP"))
        self.label_2.setText(_translate("Form", "Action Business Party"))
        self.label_3.setText(_translate("Form", "LEADER"))
        self.label_4.setText(_translate("Form", "YEAR ESTABLISHED"))
        self.label_5.setText(_translate("Form", "MOTTO"))
        self.label_6.setText(_translate("Form", "ADDRESS"))
        self.label_7.setText(_translate("Form", "PHONE NUMBER"))
        self.lblLeader.setText(_translate("Form", "MR X"))
        self.lblYearEstablished.setText(_translate("Form", "1900"))
        self.lblMotto.setText(_translate("Form", "Live or Die"))
        self.lblPhoneNumber.setText(_translate("Form", "0000011111"))
        self.lblAddress.setText(_translate("Form", "Somewhere on Earth"))
        self.btnClose.setToolTip(_translate("Form", "Go to Contestant"))
        self.btnClose.setText(_translate("Form", "CLOSE"))

    def goToContestant(self):
        goToContestant(self)

