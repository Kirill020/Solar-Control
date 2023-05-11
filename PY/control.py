from PyQt5 import QtWidgets
import Log_in
import Sign_in
import U_profile
import Forgot_pass
import Change_pass
import Change_login
from db_handler import SqliteDB


class ControlWindow:
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

    def show_forgot_pass(self):
        self.forgot_pass = Forgot_pass.ForgotPassWindow()
        self.forgot_pass.show()

    def show_change_pass(self):
        self.change_pass = Change_pass.ChangePassWindow()
        self.change_pass.show()

    def show_change_login(self):
        self.change_login = Change_login.ChangeLoginWindow()
        self.change_login.show()

class Main:
    def __init__(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    control = ControlWindow()
    control.show_login()
    app.exec_()