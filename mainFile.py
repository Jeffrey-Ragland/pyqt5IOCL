from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog
from PyQt5.uic import loadUi
import sys

class LoginUI(QMainWindow):
    def __init__(self):
        super(LoginUI, self).__init__()

        loadUi("newLogin.ui",self)

        self.loginButton.clicked.connect(self.check_credentials)

        self.correct_email = "admin@xyma.in"
        self.correct_password = "admin"

        self.showFullScreen()

    def check_credentials(self):
        email = self.emailInput.text() 
        password = self.passwordInput.text()  

        if email == self.correct_email and password == self.correct_password:
            self.open_mainPage() 
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid email or password. Please try again.")

    def open_mainPage(self):
        self.newWindow = MainPageUI()
        self.newWindow.show()  
        self.close()

class MainPageUI(QMainWindow):
    def __init__(self):
        super(MainPageUI, self).__init__()
        loadUi("mainPage.ui", self) 

        self.showFullScreen()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = LoginUI()
    app.exec()
