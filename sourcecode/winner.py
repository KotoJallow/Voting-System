# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/winner.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
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
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(320, 361))
        self.frame_2.setMaximumSize(QtCore.QSize(320, 361))
        self.frame_2.setStyleSheet("background-color:#377896;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblAvatar = QtWidgets.QLabel(self.frame_2)
        self.lblAvatar.setText("")
        self.lblAvatar.setPixmap(QtGui.QPixmap(":/loginBackgroundImage/images/assets_president.png"))
        self.lblAvatar.setScaledContents(True)
        self.lblAvatar.setObjectName("lblAvatar")
        self.gridLayout_2.addWidget(self.lblAvatar, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("background-color:#377896;\n"
"color:white;\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setGeometry(QtCore.QRect(10, 101, 247, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.frame_3)
        self.line_3.setGeometry(QtCore.QRect(10, 180, 247, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_5 = QtWidgets.QFrame(self.frame_3)
        self.line_5.setGeometry(QtCore.QRect(10, 260, 247, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 251, 16))
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lblName = QtWidgets.QLabel(self.frame_3)
        self.lblName.setGeometry(QtCore.QRect(10, 80, 251, 16))
        self.lblName.setStyleSheet("font-weight:bold;")
        self.lblName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblName.setObjectName("lblName")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 251, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lblParty = QtWidgets.QLabel(self.frame_3)
        self.lblParty.setGeometry(QtCore.QRect(10, 150, 251, 20))
        self.lblParty.setStyleSheet("font-weight:bold;")
        self.lblParty.setAlignment(QtCore.Qt.AlignCenter)
        self.lblParty.setObjectName("lblParty")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(10, 200, 251, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.lblPercentage = QtWidgets.QLabel(self.frame_3)
        self.lblPercentage.setGeometry(QtCore.QRect(0, 230, 261, 16))
        self.lblPercentage.setStyleSheet("font-weight:bold;")
        self.lblPercentage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPercentage.setObjectName("lblPercentage")
        self.btnClose = QtWidgets.QPushButton(self.frame_3)
        self.btnClose.setGeometry(QtCore.QRect(100, 280, 75, 31))
        self.btnClose.setStyleSheet("background-color:#b5e7ff;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color:white;\n"
"padding: 4px;\n"
"text-align: center;\n"
"color:black;")
        self.btnClose.setObjectName("btnClose")
        self.btnClose_2 = QtWidgets.QPushButton(self.frame_3)
        self.btnClose_2.setGeometry(QtCore.QRect(90, 10, 75, 31))
        self.btnClose_2.setToolTip("")
        self.btnClose_2.setStyleSheet("background-color:#b5e7ff;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color:white;\n"
"padding: 4px;\n"
"text-align: center;\n"
"font-weight:bold;\n"
"color:black;")
        self.btnClose_2.setObjectName("btnClose_2")
        self.horizontalLayout.addWidget(self.frame_3)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Winner"))
        self.label_2.setText(_translate("Form", "NAME"))
        self.lblName.setText(_translate("Form", "koto Jallow"))
        self.label_4.setText(_translate("Form", "PARTY"))
        self.lblParty.setText(_translate("Form", "ABP"))
        self.label_6.setText(_translate("Form", "PERCENTAGE"))
        self.lblPercentage.setText(_translate("Form", "70%"))
        self.btnClose.setText(_translate("Form", "Close"))
        self.btnClose_2.setText(_translate("Form", "Results"))


from resources import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
