# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/contestant.ui'
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
        self.lblImage = QtWidgets.QLabel(self.frame)
        self.lblImage.setGeometry(QtCore.QRect(180, 10, 231, 151))
        self.lblImage.setStyleSheet("")
        self.lblImage.setText("")
        self.lblImage.setPixmap(QtGui.QPixmap(":/loginBackgroundImage/images/assets_mayor2.png"))
        self.lblImage.setScaledContents(True)
        self.lblImage.setObjectName("lblImage")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(40, 170, 541, 131))
        self.frame_2.setMinimumSize(QtCore.QSize(541, 131))
        self.frame_2.setMaximumSize(QtCore.QSize(541, 131))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(10, 26, 521, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setGeometry(QtCore.QRect(10, 51, 521, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame_2)
        self.line_3.setGeometry(QtCore.QRect(10, 76, 521, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame_2)
        self.line_4.setGeometry(QtCore.QRect(10, 101, 521, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 47, 13))
        self.label_4.setObjectName("label_4")
        self.lblName = QtWidgets.QLabel(self.frame_2)
        self.lblName.setGeometry(QtCore.QRect(140, 10, 391, 16))
        self.lblName.setObjectName("lblName")
        self.lblAge = QtWidgets.QLabel(self.frame_2)
        self.lblAge.setGeometry(QtCore.QRect(140, 40, 391, 16))
        self.lblAge.setObjectName("lblAge")
        self.lblMaritalStatus = QtWidgets.QLabel(self.frame_2)
        self.lblMaritalStatus.setGeometry(QtCore.QRect(140, 60, 391, 16))
        self.lblMaritalStatus.setObjectName("lblMaritalStatus")
        self.lblParty = QtWidgets.QLabel(self.frame_2)
        self.lblParty.setGeometry(QtCore.QRect(140, 90, 391, 16))
        self.lblParty.setObjectName("lblParty")
        self.btnClose = QtWidgets.QPushButton(self.frame)
        self.btnClose.setGeometry(QtCore.QRect(90, 310, 171, 61))
        self.btnClose.setStyleSheet("background-color:#377896;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:30px;\n"
" border-color: white;\n"
"color:white;")
        self.btnClose.setObjectName("btnClose")
        self.btnParty = QtWidgets.QPushButton(self.frame)
        self.btnParty.setGeometry(QtCore.QRect(350, 310, 171, 61))
        self.btnParty.setStyleSheet("background-color:#377896;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:30px;\n"
" border-color: white;\n"
"color:white;")
        self.btnParty.setObjectName("btnParty")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Contestant"))
        self.label.setText(_translate("Form", "NAME"))
        self.label_2.setText(_translate("Form", "AGE"))
        self.label_3.setText(_translate("Form", "MARITAL STATUS"))
        self.label_4.setText(_translate("Form", "PARTY"))
        self.lblName.setText(_translate("Form", "MR X"))
        self.lblAge.setText(_translate("Form", "45"))
        self.lblMaritalStatus.setText(_translate("Form", "MARRIED"))
        self.lblParty.setText(_translate("Form", "ABP"))
        self.btnClose.setToolTip(_translate("Form", "Go to Vote"))
        self.btnClose.setText(_translate("Form", "CLOSE"))
        self.btnParty.setToolTip(_translate("Form", "View Party"))
        self.btnParty.setText(_translate("Form", "PARTY"))


from resources import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
