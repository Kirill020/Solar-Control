from PyQt5 import QtWidgets
import Log_in
import Sign_in
import U_profile

class Control:
    def __init__(self):
        pass
    def show_login(self):
        self.login_window = Log_in.LoginWindow()
        self.login_window.show()
    
    def show_sign_in(self):
        self.sign_in_window = Sign_in.RegistrationWindow()
        self.sign_in_window.show()

    def show_profile(self):
        self.profile_window = U_profile.ProfileWindow()
        self.profile_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    control = Control()
    control.show_login()
    app.exec_()