from PyQt6.QtWidgets import *
from PyQt6 import uic
from module.register import register

def alert(text):
    _alert = QMessageBox()
    _alert.setText(text)
    _alert.addButton(QMessageBox.StandardButton.Ok)
    _alert.buttonClicked.connect(register)
    _alert.exec()

