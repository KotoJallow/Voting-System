import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets

def general_message(message):

    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QMainWindow()
    msg = QMessageBox(dialog)
    msg.setWindowTitle('Info')
    msg.setText(message)
    msg.setIcon(QMessageBox.Information)
    msg.exec_()
    sys.exit()

def error_message(message):

    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QMainWindow()
    msg = QMessageBox(dialog)
    msg.setWindowTitle('Error')
    msg.setText(message)
    msg.setIcon(QMessageBox.Critical)
    msg.exec_()
    sys.exit()

def warning_message(message):

    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QMainWindow()
    msg = QMessageBox(dialog)
    msg.setWindowTitle('Warning')
    msg.setText(message)
    msg.setIcon(QMessageBox.Warning)
    msg.exec_()
    sys.exit()

def question_message(message):

    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QMainWindow()
    msg = QMessageBox(dialog)
    msg.setWindowTitle('Question')
    msg.setText(message)
    msg.setIcon(QMessageBox.Question)
    msg.exec_()
    sys.exit()

