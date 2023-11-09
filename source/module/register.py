from PyQt6.QtWidgets import *
from PyQt6 import uic

window = None

def register():
    # set text
    global window
    window = uic.loadUi('source/widget_UI/register.ui')
    window.findChild(QPushButton, 'pushButton').clicked.connect(success_register)
    window.show()

def success_register():

    with open('source/data_of_user/data.txt') as f:
        username = window.findChild(QLineEdit, 'lineEdit').text()
        password = window.findChild(QLineEdit, 'lineEdit_2').text()

        with open('source/data_of_user/data.txt', 'a') as f:
            f.write(f'{username} {password}\n')
    alert = QMessageBox()
    alert.setText('You registered successfully')
    alert.exec()