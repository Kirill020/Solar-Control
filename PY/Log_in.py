import sys
import U_profile
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
        self.logo_name_lab.setGeometry(QtCore.QRect(240, 60, 101, 31))
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
        self.link_lab = QtWidgets.QLabel(self)
        self.link_lab.setGeometry(QtCore.QRect(200, 370, 171, 31))
        self.link_lab.setToolTip("")
        self.link_lab.setAutoFillBackground(False)
        self.link_lab.setStyleSheet("border: 0px; background-color:rgba(0,0,0,0%);")
        self.link_lab.setObjectName("link_lab")
        self.link_lab.setText("<html><head/><body><p align=\"center\">Don`t have an account? <span style=\" color:#882a2a;\">Sign up</span></p></body></html>")


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

        self.log_in_But.clicked.connect(self.log_check)

    def log_check(self):
        if not self.login_edit.text() or not self.password_edit.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Fill every fields please!")
        else:
                user_name = str(self.login_edit.text())
                password = str(self.password_edit.text())
                result = SqliteDB.authenticate_user(user_name, password)

                if result[0]:
                     QtWidgets.QMessageBox.warning(self, "Welcome!", "Succesfuly!")
                     self.u_profile_window = QtWidgets.QWidget()
                     self.u_profile = U_profile.Ui_Form()
                     self.u_profile.setupUi(self.u_profile_window)
                     self.u_profile_window.show()
                     self.hide()
                else:
                     QtWidgets.QMessageBox.warning(self, "Error", "Something went wrong. Please, try again")

import Backgrounds
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
