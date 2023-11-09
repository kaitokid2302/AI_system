import sys
from PyQt6 import QtWidgets, uic
from module.alert import alert

class LoginWindow(QtWidgets.QWidget):
    def handleLogin(self):
        ok = False
        with open('source/data_of_user/data.txt') as data:
            for i in data:
                _data = i.split(' ')
                username, password = _data[0], _data[1]
                if(self.lineEditUsername.text == username and self.lineEditPassword.text==password):
                    alert('Successfully login')
                    ok = True
                    break
            if ok ==False:
                alert('We do not have this account, wanna create?')

    def __init__(self):
        super().__init__()
        uic.loadUi('source/widget_UI/login.ui', self)  # Thay 'login.ui' bằng đường dẫn đến file .ui của bạn

        self.buttonLogin = self.findChild(QtWidgets.QPushButton, 'login')
        self.lineEditUsername = self.findChild(QtWidgets.QLineEdit, 'username')
        self.lineEditPassword = self.findChild(QtWidgets.QLineEdit, 'password')

        self.buttonLogin.clicked.connect(self.handleLogin)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = LoginWindow()
    loginWindow.show()
    sys.exit(app.exec())