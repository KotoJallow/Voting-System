from PyQt5 import QtWidgets


def navigate(source):
    source.destinationUI = QtWidgets.QWidget()
    source.destination.setupUi(source.destinationUI)
    source.destinationUI.show()
    source.Form.close()
