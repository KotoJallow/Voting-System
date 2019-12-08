# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/announcement.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from utils import goToMain

class AnnouncementUI(object):

    def __init__(self,userId, ui_data):
        self.userId = userId
        self.ui_data = ui_data

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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.card0 = QtWidgets.QFrame(self.frame)
        self.card0.setMinimumSize(QtCore.QSize(201, 178))
        self.card0.setMaximumSize(QtCore.QSize(201, 178))
        self.card0.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card0.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card0.setObjectName("card0")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.card0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblAvatar0 = QtWidgets.QLabel(self.card0)
        self.lblAvatar0.setMinimumSize(QtCore.QSize(181, 106))
        self.lblAvatar0.setMaximumSize(QtCore.QSize(181, 106))
        self.lblAvatar0.setText("")
        self.lblAvatar0.setPixmap(QtGui.QPixmap(":/loginBackgroundImage/images/avatar.png"))
        self.lblAvatar0.setScaledContents(True)
        self.lblAvatar0.setObjectName("lblAvatar0")
        self.verticalLayout.addWidget(self.lblAvatar0)
        self.lblName0 = QtWidgets.QLabel(self.card0)
        self.lblName0.setMinimumSize(QtCore.QSize(181, 20))
        self.lblName0.setMaximumSize(QtCore.QSize(181, 20))
        self.lblName0.setAlignment(QtCore.Qt.AlignCenter)
        self.lblName0.setObjectName("lblName0")
        self.verticalLayout.addWidget(self.lblName0)

        self.lblPercentage0 = QtWidgets.QLabel(self.card0)
        self.lblPercentage0.setMinimumSize(QtCore.QSize(171, 20))
        self.lblPercentage0.setMaximumSize(QtCore.QSize(171, 20))
        self.lblPercentage0.setStyleSheet("")
        self.lblPercentage0.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPercentage0.setObjectName("lblPercentage0")

        self.verticalLayout.addWidget(self.lblPercentage0)
        self.gridLayout_2.addWidget(self.card0, 0, 0, 1, 1)



        self.card1 = QtWidgets.QFrame(self.frame)
        self.card1.setMinimumSize(QtCore.QSize(201, 178))
        self.card1.setMaximumSize(QtCore.QSize(201, 178))
        self.card1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card1.setObjectName("card1")
        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.card1)
        self.verticalLayout1.setObjectName("verticalLayout1")
        self.lblAvatar1 = QtWidgets.QLabel(self.card1)
        self.lblAvatar1.setMinimumSize(QtCore.QSize(181, 106))
        self.lblAvatar1.setMaximumSize(QtCore.QSize(181, 106))
        self.lblAvatar1.setText("")
        self.lblAvatar1.setPixmap(QtGui.QPixmap(":/loginBackgroundImage/images/avatar.png"))
        self.lblAvatar1.setScaledContents(True)
        self.lblAvatar1.setObjectName("lblAvatar1")
        self.verticalLayout1.addWidget(self.lblAvatar1)
        self.lblName1 = QtWidgets.QLabel(self.card1)
        self.lblName1.setMinimumSize(QtCore.QSize(181, 20))
        self.lblName1.setMaximumSize(QtCore.QSize(181, 20))
        self.lblName1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblName1.setObjectName("lblName1")
        self.verticalLayout1.addWidget(self.lblName1)
        self.lblPercentage1 = QtWidgets.QLabel(self.card1)
        self.lblPercentage1.setMinimumSize(QtCore.QSize(171, 20))
        self.lblPercentage1.setMaximumSize(QtCore.QSize(171, 20))
        self.lblPercentage1.setStyleSheet("")
        self.lblPercentage1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPercentage1.setObjectName("lblPercentage1")
        self.verticalLayout1.addWidget(self.lblPercentage1)
        self.gridLayout_2.addWidget(self.card1, 0, 1, 1, 1)
        self.card2 = QtWidgets.QFrame(self.frame)
        self.card2.setMinimumSize(QtCore.QSize(201, 178))
        self.card2.setMaximumSize(QtCore.QSize(201, 178))
        self.card2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card2.setObjectName("card2")
        self.verticalLayout2 = QtWidgets.QVBoxLayout(self.card2)
        self.verticalLayout2.setObjectName("verticalLayout2")
        self.lblAvatar2 = QtWidgets.QLabel(self.card2)
        self.lblAvatar2.setMinimumSize(QtCore.QSize(181, 106))
        self.lblAvatar2.setMaximumSize(QtCore.QSize(181, 106))
        self.lblAvatar2.setText("")
        self.lblAvatar2.setPixmap(QtGui.QPixmap(":/loginBackgroundImage/images/avatar.png"))
        self.lblAvatar2.setScaledContents(True)
        self.lblAvatar2.setObjectName("lblAvatar2")
        self.verticalLayout2.addWidget(self.lblAvatar2)
        self.lblName2 = QtWidgets.QLabel(self.card2)
        self.lblName2.setMinimumSize(QtCore.QSize(181, 20))
        self.lblName2.setMaximumSize(QtCore.QSize(181, 20))
        self.lblName2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblName2.setObjectName("lblName2")
        self.verticalLayout2.addWidget(self.lblName2)
        self.lblPercentage2 = QtWidgets.QLabel(self.card2)
        self.lblPercentage2.setMinimumSize(QtCore.QSize(171, 20))
        self.lblPercentage2.setMaximumSize(QtCore.QSize(171, 20))
        self.lblPercentage2.setStyleSheet("")
        self.lblPercentage2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPercentage2.setObjectName("lblPercentage2")
        self.verticalLayout2.addWidget(self.lblPercentage2)
        self.gridLayout_2.addWidget(self.card2, 0, 2, 1, 1)
        self.card3 = QtWidgets.QFrame(self.frame)
        self.card3.setMinimumSize(QtCore.QSize(201, 178))
        self.card3.setMaximumSize(QtCore.QSize(201, 178))
        self.card3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card3.setObjectName("card3")
        self.verticalLayout3 = QtWidgets.QVBoxLayout(self.card3)
        self.verticalLayout3.setObjectName("verticalLayout3")
        self.lblAvatar3 = QtWidgets.QLabel(self.card3)
        self.lblAvatar3.setMinimumSize(QtCore.QSize(181, 106))
        self.lblAvatar3.setMaximumSize(QtCore.QSize(181, 106))
        self.lblAvatar3.setText("")
        self.lblAvatar3.setPixmap(QtGui.QPixmap(":/loginBackgroundImage/images/avatar.png"))
        self.lblAvatar3.setScaledContents(True)
        self.lblAvatar3.setObjectName("lblAvatar3")
        self.verticalLayout3.addWidget(self.lblAvatar3)
        self.lblName3 = QtWidgets.QLabel(self.card3)
        self.lblName3.setMinimumSize(QtCore.QSize(181, 20))
        self.lblName3.setMaximumSize(QtCore.QSize(181, 20))
        self.lblName3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblName3.setObjectName("lblName3")
        self.verticalLayout3.addWidget(self.lblName3)
        self.lblPercentage3 = QtWidgets.QLabel(self.card3)
        self.lblPercentage3.setMinimumSize(QtCore.QSize(171, 20))
        self.lblPercentage3.setMaximumSize(QtCore.QSize(171, 20))
        self.lblPercentage3.setStyleSheet("")
        self.lblPercentage3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPercentage3.setObjectName("lblPercentage3")
        self.verticalLayout3.addWidget(self.lblPercentage3)
        self.gridLayout_2.addWidget(self.card3, 1, 0, 1, 1)
        self.card4 = QtWidgets.QFrame(self.frame)
        self.card4.setMinimumSize(QtCore.QSize(201, 178))
        self.card4.setMaximumSize(QtCore.QSize(201, 178))
        self.card4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card4.setObjectName("card4")
        self.verticalLayout4 = QtWidgets.QVBoxLayout(self.card4)
        self.verticalLayout4.setObjectName("verticalLayout4")
        self.lblAvatar4 = QtWidgets.QLabel(self.card4)
        self.lblAvatar4.setMinimumSize(QtCore.QSize(181, 106))
        self.lblAvatar4.setMaximumSize(QtCore.QSize(181, 106))
        self.lblAvatar4.setText("")
        self.lblAvatar4.setPixmap(QtGui.QPixmap(":/loginBackgroundImage/images/avatar.png"))
        self.lblAvatar4.setScaledContents(True)
        self.lblAvatar4.setObjectName("lblAvatar4")
        self.verticalLayout4.addWidget(self.lblAvatar4)
        self.lblName4 = QtWidgets.QLabel(self.card4)
        self.lblName4.setMinimumSize(QtCore.QSize(181, 20))
        self.lblName4.setMaximumSize(QtCore.QSize(181, 20))
        self.lblName4.setAlignment(QtCore.Qt.AlignCenter)
        self.lblName4.setObjectName("lblName4")
        self.verticalLayout4.addWidget(self.lblName4)
        self.lblPercentage4 = QtWidgets.QLabel(self.card4)
        self.lblPercentage4.setMinimumSize(QtCore.QSize(171, 20))
        self.lblPercentage4.setMaximumSize(QtCore.QSize(171, 20))
        self.lblPercentage4.setStyleSheet("")
        self.lblPercentage4.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPercentage4.setObjectName("lblPercentage4")
        self.verticalLayout4.addWidget(self.lblPercentage4)
        self.gridLayout_2.addWidget(self.card4, 1, 1, 1, 1)
        self.card5 = QtWidgets.QFrame(self.frame)
        self.card5.setMinimumSize(QtCore.QSize(201, 178))
        self.card5.setMaximumSize(QtCore.QSize(201, 178))
        self.card5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card5.setObjectName("card5")
        self.verticalLayout5 = QtWidgets.QVBoxLayout(self.card5)
        self.verticalLayout5.setObjectName("verticalLayout5")
        self.lblAvatar5 = QtWidgets.QLabel(self.card5)
        self.lblAvatar5.setMinimumSize(QtCore.QSize(181, 106))
        self.lblAvatar5.setMaximumSize(QtCore.QSize(181, 106))
        self.lblAvatar5.setText("")
        self.lblAvatar5.setPixmap(QtGui.QPixmap(":/loginBackgroundImage/images/avatar.png"))
        self.lblAvatar5.setScaledContents(True)
        self.lblAvatar5.setObjectName("lblAvatar5")
        self.verticalLayout5.addWidget(self.lblAvatar5)
        self.lblName5 = QtWidgets.QLabel(self.card5)
        self.lblName5.setMinimumSize(QtCore.QSize(181, 20))
        self.lblName5.setMaximumSize(QtCore.QSize(181, 20))
        self.lblName5.setAlignment(QtCore.Qt.AlignCenter)
        self.lblName5.setObjectName("lblName5")
        self.verticalLayout5.addWidget(self.lblName5)
        self.lblPercentage5 = QtWidgets.QLabel(self.card5)
        self.lblPercentage5.setMinimumSize(QtCore.QSize(171, 20))
        self.lblPercentage5.setMaximumSize(QtCore.QSize(171, 20))
        self.lblPercentage5.setStyleSheet("")
        self.lblPercentage5.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPercentage5.setObjectName("lblPercentage5")
        self.verticalLayout5.addWidget(self.lblPercentage5)

        self.btnClose = QtWidgets.QPushButton('CLOSE',self.frame)
        self.btnClose.setGeometry(QtCore.QRect(558, 335, 50, 40))
        self.btnClose.setStyleSheet("background-color:#377896;\n"
                                       "font-weight:bold;\n"
                                       "color: white;\n"
                                       "border-width: 2px;\n"
                                       "border-radius: 15px;\n"
                                       "padding: 4px;\n"
                                       "text-align: center;")
        self.btnClose.clicked.connect(self.goToMain)

        self.gridLayout_2.addWidget(self.card5, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)

        # Get data from database
        self.lblName0.setText(self.ui_data[0].get('Name'))
        self.lblPercentage0.setText(self.ui_data[0].get('Percentage'))
        self.lblName1.setText(self.ui_data[1].get('Name'))
        self.lblPercentage1.setText(self.ui_data[1].get('Percentage'))
        self.lblName2.setText(self.ui_data[2].get('Name'))
        self.lblPercentage2.setText(self.ui_data[2].get('Percentage'))
        self.lblName3.setText(self.ui_data[3].get('Name'))
        self.lblPercentage3.setText(self.ui_data[3].get('Percentage'))
        self.lblName4.setText(self.ui_data[4].get('Name'))
        self.lblPercentage4.setText(self.ui_data[4].get('Percentage'))
        self.lblName5.setText(self.ui_data[5].get('Name'))
        self.lblPercentage5.setText(self.ui_data[5].get('Percentage'))

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Announcement"))
        self.lblName0.setText(_translate("Form", "KOTO JALLOW"))
        self.lblPercentage0.setText(_translate("Form", "70%"))
        self.lblName1.setText(_translate("Form", "KOTO JALLOW"))
        self.lblPercentage1.setText(_translate("Form", "70%"))
        self.lblName2.setText(_translate("Form", "KOTO JALLOW"))
        self.lblPercentage2.setText(_translate("Form", "70%"))
        self.lblName3.setText(_translate("Form", "KOTO JALLOW"))
        self.lblPercentage3.setText(_translate("Form", "70%"))
        self.lblName4.setText(_translate("Form", "KOTO JALLOW"))
        self.lblPercentage4.setText(_translate("Form", "70%"))
        self.lblName5.setText(_translate("Form", "KOTO JALLOW"))
        self.lblPercentage5.setText(_translate("Form", "70%"))

    def goToMain(self):
        goToMain(self,self.userId)

from resources import resource_rc