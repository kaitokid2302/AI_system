import sys
from PyQt6 import QtWidgets, uic
from module.alert import alert
from module.register import register

class LoginWindow(QtWidgets.QWidget):
    def handleLogin(self):
        ok = False
        with open('source/data_of_user/data.txt') as data:
            for i in data:
                _data = i.split(' ')
                username, password = _data[0], _data[1]
                if(self.lineEditUsername.text() == username and self.lineEditPassword.text()==password):
                    login_success = QtWidgets.QMessageBox()
                    login_success.setText('Login successfully, we found your credentials!')
                    login_success.exec()
                    ok = True
                    break
            if ok ==False:
                alert('We do not have this account, wanna create?')

    def __init__(self):
        super().__init__()
        uic.loadUi('source/widget_UI/login.ui', self)

        self.buttonLogin = self.findChild(QtWidgets.QPushButton, 'login')
        self.lineEditUsername = self.findChild(QtWidgets.QLineEdit, 'username_text')
        self.lineEditPassword = self.findChild(QtWidgets.QLineEdit, 'password_text')
        self.buttonRegister = self.findChild(QtWidgets.QPushButton, 'register')

        self.buttonRegister.clicked.connect(register)

        self.buttonLogin.clicked.connect(self.handleLogin)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = LoginWindow()
    loginWindow.show()
    sys.exit(app.exec())