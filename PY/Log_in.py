import sys
import control
from db_handler import SqliteDB
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorisation")
        self.setFixedSize(555,440)
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.482198, y1:0.971, x2:0.497, y2:0.023, stop:0.0338983 rgba(46, 46, 46, 255), stop:1 rgba(168, 168, 168, 255));")



        #Logo name(SOLAR CONTROL)
        self.logo_name_lab = QtWidgets.QLabel(self)
        self.logo_name_lab.setGeometry(QtCore.QRect(230, 60, 101, 31))
        self.logo_name_lab.setToolTip("")
        self.logo_name_lab.setAutoFillBackground(False)
        self.logo_name_lab.setStyleSheet("border: 0px; background-color:rgba(0,0,0,0%);")
        self.logo_name_lab.setObjectName("logo_name_lab")
        self.logo_name_lab.setText("<html><head/><body><p align=\"center\">SOLAR CONTROL</p></body></html>")



        #Edit for login(email)
        self.login_edit = QtWidgets.QLineEdit(self)
        self.login_edit.setGeometry(QtCore.QRect(160, 140, 241, 41))
        self.login_edit.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
                        "font: 9pt \"MS Shell Dlg 2\";\n"
                        "min-width: 8em;\n"
                        "background: qradialgradient(\n"
                        "cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                        "radius: 1.35, stop: 0 #fff, stop: 1 #a6a6a6\n"
                        ");\n"
                        "padding: 5px;\n"
                        "}\n"
                        "\n"
                        "QLineEdit:hover {\n"
                        "background: qradialgradient(\n"
                        "cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                        "radius: 1.35, stop: 0 #b4b4b4, stop: 1 #969696\n"
                        ");\n"
                        "}\n"
                        "\n"
                        "QLineEdit:pressed {\n"
                        "border-style: inset;\n"
                        "background: qradialgradient(\n"
                        "cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                        "radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                        ");\n"
                        "}")
        self.login_edit.setInputMask("")
        self.login_edit.setToolTip("Your E-mail adress")
        self.login_edit.setText("")
        self.login_edit.setPlaceholderText("")
        self.login_edit.setObjectName("login_edit")
        self.login_edit.setWhatsThis("Edit for e-mail")
        self.login_edit.setPlaceholderText("Email")


        #Logo image
        self.logo_Login = QtWidgets.QLabel(self)
        self.logo_Login.setGeometry(QtCore.QRect(130, 40, 91, 61))
        self.logo_Login.setMinimumSize(QtCore.QSize(82, 45))
        self.logo_Login.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                        "image: url(:/newPrefix/images/backgrounds/PsLYIQ01.svg);")
        self.logo_Login.setObjectName("logo_Login")
        self.logo_Login.setText("<html><head/><body><p align=\"center\"><br/></p></body></html>")


        #Link lable to register window
        self.link_reg = QtWidgets.QLabel(self)
        self.link_reg.setGeometry(QtCore.QRect(170, 370, 171, 31))
        self.link_reg.setToolTip("")
        self.link_reg.setAutoFillBackground(False)
        self.link_reg.setStyleSheet("border: 0px; background-color:rgba(0,0,0,0%);")
        self.link_reg.setObjectName("link_reg")
        self.link_reg.setText("<html><head/><body><p align=\"center\">Don`t have an account?</p></body></html>")

        self.link_reg_2 = QtWidgets.QLabel(self)
        self.link_reg_2.setGeometry(QtCore.QRect(253, 370, 171, 31))
        self.link_reg_2.setToolTip("")
        self.link_reg_2.setAutoFillBackground(False)
        self.link_reg_2.setStyleSheet("border: 0px; background-color:rgba(0,0,0,0%);")
        self.link_reg_2.setObjectName("link_reg_2")
        self.link_reg_2.setText("<html><head/><body><p style=\" color:#FFFFFF;\" align=\"center\">Sign in </p></body></html>")
        self.link_reg_2.mousePressEvent = self.show_sign_in



        #Link lable to register window
        self.link_forg = QtWidgets.QLabel(self)
        self.link_forg.setGeometry(QtCore.QRect(190, 350, 171, 31))
        self.link_forg.setToolTip("")
        self.link_forg.setAutoFillBackground(False)
        self.link_forg.setStyleSheet("border: 0px; background-color:rgba(0,0,0,0%);")
        self.link_forg.setObjectName("link_forg")
        self.link_forg.setText("<html><head/><body><p style=\" color:#FFFFFF;\" align=\"center\">Forgot password?</p></body></html>")
        self.link_forg.mousePressEvent = self.show_forgot_pass


        #Log in button 
        self.log_in_But = QtWidgets.QPushButton(self)
        self.log_in_But.setGeometry(QtCore.QRect(215, 290, 131, 41))
        self.log_in_But.setMinimumSize(QtCore.QSize(131, 41))
        self.log_in_But.setMaximumSize(QtCore.QSize(145, 41))
        self.log_in_But.setAutoFillBackground(False)
        self.log_in_But.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
                        "font: 12pt \"MS Shell Dlg 2\";\n"
                        "max-width: 131px;\n"
                        "background: qradialgradient(\n"
                        "cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                        "radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                        ");\n"
                        "padding: 5px;\n"
                        "}\n"
                        "\n"
                        "QPushButton:hover {\n"
                        "background: qradialgradient(\n"
                        "cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                        "radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                        ");\n"
                        "}\n"
                        "\n"
                        "QPushButton:pressed {\n"
                        "border-style: inset;\n"
                        "background: qradialgradient(\n"
                        "cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                        "radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                        ");\n"
                        "}")
        self.log_in_But.setObjectName("Log_in_But")
        self.log_in_But.setText("Log in")
        self.log_in_But.clicked.connect(self.log_check)

        
        #Edit for password
        self.password_edit = QtWidgets.QLineEdit(self)
        self.password_edit.setGeometry(QtCore.QRect(160, 210, 241, 41))
        self.password_edit.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
                        "font: 10pt \"MS Shell Dlg 2\";\n"
                        "min-width: 8em;\n"
                        "background: qradialgradient(\n"
                        "cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                        "radius: 1.35, stop: 0 #fff, stop: 1 #a6a6a6\n"
                        ");\n"
                        "padding: 5px;\n"
                        "}\n"
                        "\n"
                        "QLineEdit:hover {\n"
                        "background: qradialgradient(\n"
                        "cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                        "radius: 1.35, stop: 0 #b4b4b4, stop: 1 #969696\n"
                        ");\n"
                        "}\n"
                        "\n"
                        "QLineEdit:pressed {\n"
                        "border-style: inset;\n"
                        "background: qradialgradient(\n"
                        "cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                        "radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                        ");\n"
                        "}")
        self.password_edit.setInputMask("")
        self.password_edit.setToolTip("Your password")
        self.password_edit.setText("")
        self.password_edit.setPlaceholderText("")
        self.password_edit.setObjectName("password_edit")
        self.password_edit.setWhatsThis("Edit for Password")
        self.password_edit.setPlaceholderText("Password")

        
    def log_check(self):
        if not self.login_edit.text() or not self.password_edit.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Fill every fields please!")
        else:
                user_name = str(self.login_edit.text())
                password = str(self.password_edit.text())
                result = SqliteDB.authenticate_user(user_name, password)

                if result[0]:
                    self.controller = control.ControlWindow()
                    self.controller.show_profile()
                    self.close()
                else:
                    QtWidgets.QMessageBox.warning(self, "Error", "Something went wrong. Please, try again")


    def show_sign_in(self,event):
        self.login_edit.setText("")
        self.password_edit.setText("")

        self.controller = control.ControlWindow()
        self.controller.show_sign_in()
        self.close()

    def show_forgot_pass(self,event):
        self.login_edit.setText("")
        self.password_edit.setText("")
        
        self.controller = control.ControlWindow()
        self.controller.show_forgot_pass()
        self.close()
import Backgrounds
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
