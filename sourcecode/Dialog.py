import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets

def information_message(dialog,message):
    msg = QMessageBox(dialog)
    msg.setWindowTitle('Info')
    msg.setStyleSheet("background-color: #fff;")
    msg.setText(message)
    msg.setIcon(QMessageBox.Information)
    msg.exec_()

def error_message(dialog,message):
    msg = QMessageBox(dialog)
    msg.setWindowTitle('Error')
    msg.setStyleSheet("background-color: #fff;")
    msg.setText(message)
    msg.setIcon(QMessageBox.Critical)
    msg.exec_()

def warning_message(dialog,message):
    msg = QMessageBox(dialog)
    msg.setWindowTitle('Warning')
    msg.setStyleSheet("background-color: #fff;")
    msg.setText(message)
    msg.setIcon(QMessageBox.Warning)
    msg.exec_()

def question_message(dialog,message):
    msg = QMessageBox(dialog)
    msg.setWindowTitle('Question')
    msg.setStyleSheet("background-color: #fff;")
    msg.setText(message)
    msg.setIcon(QMessageBox.Question)
    msg.exec_()

