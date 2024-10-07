from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QStackedWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import sys

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        self.stackedWidget = QStackedWidget(self)
        self.setCentralWidget(self.stackedWidget)

        self.loginPage = LoginUI(self)
        self.mainPage = MainPageUI(self)
        self.testingPage = TestingPageUI(self)
        self.calibrationPage = CalibrationPageUI(self)
        self.reportsPage = ReportsPageUI(self)

        self.stackedWidget.addWidget(self.loginPage)
        self.stackedWidget.addWidget(self.mainPage)
        self.stackedWidget.addWidget(self.testingPage)
        self.stackedWidget.addWidget(self.calibrationPage)
        self.stackedWidget.addWidget(self.reportsPage)
        
        self.stackedWidget.setCurrentWidget(self.loginPage)

        self.showMaximized()

        self.stackedWidget.currentChanged.connect(self.on_page_changed)

    def on_page_changed(self, index):
        current_page = self.stackedWidget.currentWidget()

        if isinstance(current_page, LoginUI):
            self.showMaximized()  
        else:
            self.showFullScreen() 

class LoginUI(QMainWindow):
    def __init__(self, mainUI):
        super(LoginUI, self).__init__()

        loadUi("newLogin.ui",self)

        self.setStyleSheet("QMainWindow {"
                           "background-image: url('loginCover.jpg');"  
                           "background-position: center;"
                           "}")

        self.loginButton.clicked.connect(self.check_credentials)
        self.mainUI = mainUI

        self.correct_email = "a"
        self.correct_password = "a"

        self.load_logo()

    def load_logo(self):
        pixmap = QPixmap('xymaLogoBlue.png')  

        resized_pixmap = pixmap.scaled(200, 100, aspectRatioMode=1) 
    
        self.loginPageXymaLogoLabel.setPixmap(resized_pixmap)
        self.loginPageXymaLogoLabel.setScaledContents(True)

    def check_credentials(self):
        email = self.emailInput.text() 
        password = self.passwordInput.text()  

        if email == self.correct_email and password == self.correct_password:
            self.emailInput.clear()
            self.passwordInput.clear()
            self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.mainPage) 
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid email or password. Please try again.")

class MainPageUI(QMainWindow):
    def __init__(self, mainUI):
        super(MainPageUI, self).__init__()
        loadUi("mainPage.ui", self) 

        self.setStyleSheet("QMainWindow {"
                           "background-image: url('homepage.png');"  
                           "background-position: center;"
                           "}")

        self.mainUI = mainUI
        self.logoutButton.clicked.connect(self.logout)
        self.testingButton.clicked.connect(self.GoToTestingPage)
        self.calibrationButton.clicked.connect(self.GoToCalibrationPage)
        self.reportsButton.clicked.connect(self.GoToReportsPage)

        self.load_logo()

    def load_logo(self):
        pixmap = QPixmap('xymaLogoWhite.png')  

        resized_pixmap = pixmap.scaled(100, 50, aspectRatioMode=1) 
    
        self.mainpageXymaLogoLabel.setPixmap(resized_pixmap)
        self.mainpageXymaLogoLabel.setScaledContents(True)

    def logout(self): 
       self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.loginPage)

    def GoToTestingPage(self):
        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.testingPage)

    def GoToCalibrationPage(self):
        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.calibrationPage)

    def GoToReportsPage(self):
       self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.reportsPage)

class TestingPageUI(QMainWindow):
    def __init__(self, mainUI):
        super(TestingPageUI, self).__init__()
        loadUi("testingPage.ui", self)

        self.mainUI = mainUI
        self.testingBackButton.clicked.connect(self.testingGoBack)

        self.load_logo()

    def load_logo(self):
        pixmap = QPixmap('xymaLogoBlue.png')  
        self.xymaLogoLabel.setPixmap(pixmap)
        self.xymaLogoLabel.setScaledContents(True) 

    def testingGoBack(self):
       self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.mainPage)

class CalibrationPageUI(QMainWindow):
    def __init__(self, mainUI):
        super(CalibrationPageUI, self).__init__()
        loadUi("calibrationPage.ui", self)

        self.mainUI = mainUI
        self.calibrationBackButton.clicked.connect(self.calibrationGoBack)

    def calibrationGoBack(self):
       self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.mainPage)

class ReportsPageUI(QMainWindow):
    def __init__(self, mainUI):
        super(ReportsPageUI, self).__init__()
        loadUi("reportsPage.ui", self)

        self.mainUI = mainUI
        self.reportsBackButton.clicked.connect(self.reportsGoBack)

    def reportsGoBack(self):
        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.mainPage)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI() 
    ui.show()
    sys.exit(app.exec_())
