import sys
import random
import smtplib
import time
import control
from db_handler import SqliteDB
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
sec_code = None


class RegistrationWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registration")
        self.setFixedSize(555,440)
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.482198, y1:0.971, x2:0.497, y2:0.023, stop:0.0338983 rgba(46, 46, 46, 255), stop:1 rgba(168, 168, 168, 255));")


        comfortaa_font_id = QFontDatabase.addApplicationFont("C:\\Solar Control\\Solar-Control\\fonts\\Comfortaa-Bold.ttf")
        opensans_font_id = QFontDatabase.addApplicationFont("C:\\Solar Control\\Solar-Control\\fonts\\OpenSans-SemiBold.ttf")
        if comfortaa_font_id != -1 and opensans_font_id != -1:
            comfortaa_font_fam = QFontDatabase.applicationFontFamilies(comfortaa_font_id)
            opensans_font_fam = QFontDatabase.applicationFontFamilies(opensans_font_id)
            if comfortaa_font_fam and opensans_font_fam:

                self.comfortaa_font = comfortaa_font_fam[0]
                self.opensans_font = opensans_font_fam[0]
                self.logo_font = QFont(self.comfortaa_font, 15)
                self.button_font = QFont(self.comfortaa_font, 11)
                self.edit_font = QFont(self.comfortaa_font, 9)
                self.label_font = QFont(self.opensans_font, 10)



        #Register button
        self.reg_but = QtWidgets.QPushButton(self)
        self.reg_but.setGeometry(QtCore.QRect(210, 380, 141, 41))
        self.reg_but.setMinimumSize(QtCore.QSize(141, 41))
        self.reg_but.setMaximumSize(QtCore.QSize(145, 41))
        self.reg_but.setAutoFillBackground(False)
        self.reg_but.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
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
        self.reg_but.setObjectName("reg_but")
        self.reg_but.setFont(self.button_font)
        self.reg_but.setText("Sign up")
        self.reg_but.clicked.connect(self.reg_check)
        self.reg_but.setDisabled(True)




        #Edit for E-mail
        self.email_edit = QtWidgets.QLineEdit(self)
        self.email_edit.setGeometry(QtCore.QRect(155, 80, 241, 41))
        self.email_edit.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
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
        self.email_edit.setInputMask("")
        self.email_edit.setFont(self.edit_font)
        self.email_edit.setToolTip("Your E-mail adress")
        self.email_edit.setText("")
        self.email_edit.setObjectName("e_mail_edit")
        self.email_edit.setWhatsThis("Edit for email")
        self.email_edit.setPlaceholderText("Email")



#send code button 
        self.send_code_but = QtWidgets.QPushButton(self)
        self.send_code_but.setGeometry(QtCore.QRect(410, 85, 70, 31))
        self.send_code_but.setAutoFillBackground(False)
        self.send_code_but.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: outset;\n"
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
        self.send_code_but.setObjectName("send_code_but")
        self.send_code_but.setFont(self.button_font)
        self.send_code_but.setText("Send")
        self.send_code_but.clicked.connect(self.send_code)



        #Edit for login
        self.login_edit = QtWidgets.QLineEdit(self)
        self.login_edit.setGeometry(QtCore.QRect(155, 200, 241, 41))
        self.login_edit.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
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
        self.login_edit.setFont(self.edit_font)
        self.login_edit.setToolTip("Your name")
        self.login_edit.setText("")
        self.login_edit.setObjectName("login_edit")
        self.login_edit.setWhatsThis("Edit for Login")
        self.login_edit.setPlaceholderText("Name")
        self.login_edit.setReadOnly(True)



#Edit for security code
        self.email_key_edit = QtWidgets.QLineEdit(self)
        self.email_key_edit.setGeometry(QtCore.QRect(155, 140, 241, 41))
        self.email_key_edit.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
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
        self.email_key_edit.setInputMask("")
        self.email_key_edit.setToolTip("Security code")
        self.email_key_edit.setText("")
        self.email_key_edit.setObjectName("email_key_edit")
        self.email_key_edit.setFont(self.edit_font)
        self.email_key_edit.setWhatsThis("Edit for security code")
        self.email_key_edit.setPlaceholderText("Code")
        self.email_key_edit.setReadOnly(True)



        #Edit for Adress
        self.adress_edit = QtWidgets.QLineEdit(self)
        self.adress_edit.setGeometry(QtCore.QRect(155, 260, 241, 41))
        self.adress_edit.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
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
        self.adress_edit.setInputMask("")
        self.adress_edit.setToolTip("Your adress")
        self.adress_edit.setText("")
        self.adress_edit.setPlaceholderText("")
        self.adress_edit.setObjectName("adress_edit")
        self.adress_edit.setFont(self.edit_font)
        self.adress_edit.setWhatsThis("Edit for adress")
        self.adress_edit.setPlaceholderText("Adress")
        self.adress_edit.setReadOnly(True)



#Edit for password
        self.password_edit = QtWidgets.QLineEdit(self)
        self.password_edit.setGeometry(QtCore.QRect(155, 320, 241, 41))
        self.password_edit.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
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
        
        self.password_edit.setObjectName("password_edit")
        self.password_edit.setFont(self.edit_font)
        self.password_edit.setWhatsThis("Edit for login")
        self.password_edit.setPlaceholderText("Password")
        self.password_edit.setReadOnly(True)
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.show_password_checkbox = QtWidgets.QCheckBox(self)
        self.show_password_checkbox.setText("Show")
        self.show_password_checkbox.setFont(self.label_font)
        self.show_password_checkbox.setGeometry(400,327,57,30)
        self.show_password_checkbox.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n")
        self.show_password_checkbox.clicked.connect(self.show_password)


        #Logo name(SOLAR CONTROL)
        self.logo_name_lab = QtWidgets.QLabel(self)
        self.logo_name_lab.setGeometry(QtCore.QRect(185, 30, 180, 31))
        self.logo_name_lab.setToolTip("")
        self.logo_name_lab.setFont(self.logo_font)
        self.logo_name_lab.setAutoFillBackground(False)
        self.logo_name_lab.setStyleSheet("border: 0px; background-color:rgba(0,0,0,0%);")
        self.logo_name_lab.setObjectName("logo_name_lab")
        self.logo_name_lab.setText("<html><head/><body><p align=\"center\">SOLAR CONTROL</p></body></html>")


        #Back button 
        self.back_but = QtWidgets.QPushButton(self)
        self.back_but.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.back_but.setAutoFillBackground(False)
        self.back_but.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
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
        self.back_but.setObjectName("back_but")
        self.back_but.setFont(self.button_font)
        self.back_but.setText("<")
        self.back_but.clicked.connect(self.show_login)




        #Logo image
        self.logo_sign_in = QtWidgets.QLabel(self)
        self.logo_sign_in.setGeometry(QtCore.QRect(100, 20, 91, 61))
        self.logo_sign_in.setMinimumSize(QtCore.QSize(82, 45))
        self.logo_sign_in.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                        "image: url(:/newPrefix/images/backgrounds/PsLYIQ01.svg);")
        self.logo_sign_in.setObjectName("logo_sign_in")
        self.logo_sign_in.setText("<html><head/><body><p align=\"center\"><br/></p></body></html>")



    def reg_check(self):
        if not self.login_edit.text() or not self.email_edit.text() or not self.password_edit.text() or not self.adress_edit.text() or not self.email_key_edit.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Fill every fields please!")
        else:
                user_name = self.login_edit.text()
                email = self.email_edit.text()
                password = self.password_edit.text()
                adress = self.adress_edit.text()
                code = self.email_key_edit.text()
                if code == sec_code["code"] and (time.time() - sec_code['timestamp']) < 180:
                    with open(r'C:\Solar Control\Solar-Control\images\empty_user.png', 'rb') as f:
                        image_binary = f.read()


                    if SqliteDB.add_user(user_name, email, adress, password, image_binary):
                        self.controller = control.ControlWindow()
                        self.controller.show_login()
                        self.close()
                    else:
                        QtWidgets.QMessageBox.warning(self, "Error", "Something went wrong. Please, try again")
                        self.email_edit.setReadOnly(False)
                        self.email_edit.setText("")
                        self.send_code_but.setDisabled(False)
                        self.email_key_edit.setReadOnly(True)
                        self.email_key_edit.setText("")
                        self.login_edit.setReadOnly(True)
                        self.login_edit.setText("")
                        self.password_edit.setReadOnly(True)
                        self.password_edit.setText("")
                        self.adress_edit.setReadOnly(True)
                        self.adress_edit.setText("")
                        self.reg_but.setDisabled(True)
                else:
                    QtWidgets.QMessageBox.warning(self, "Error", "Security code is not correct")
                    self.email_edit.setReadOnly(False)
                    self.email_edit.setText("")
                    self.send_code_but.setDisabled(False)
                    self.email_key_edit.setReadOnly(True)
                    self.email_key_edit.setText("")
                    self.login_edit.setReadOnly(True)
                    self.login_edit.setText("")
                    self.password_edit.setReadOnly(True)
                    self.password_edit.setText("")
                    self.adress_edit.setReadOnly(True)
                    self.adress_edit.setText("")
                    self.reg_but.setDisabled(True)



    def send_code(self):
        if not self.email_edit.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Write your E-mail!")
        else:
            self.email_edit.setReadOnly(True)
            self.send_code_but.setDisabled(True)
            self.email_key_edit.setReadOnly(False)
            self.login_edit.setReadOnly(False)
            self.password_edit.setReadOnly(False)
            self.adress_edit.setReadOnly(False)
            self.reg_but.setDisabled(False)

            email = self.email_edit.text()
            global sec_code
            sec_code = self.generate_code(email)

#generate security code
    def generate_code(self,email) -> int:
        try:
            code = int(random.randint(100000, 999999))
                
            from_address = 'work.tanasiichuk@gmail.com'
            to_address = email
            subject = 'Security Code'
            body = f'Your security code is: {code}'
            message = f'Subject: {subject}\n\n{body}'
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_address, 'wilgfdzekbdoboxp')
            server.sendmail(from_address, to_address, message)
            server.quit()

            QtWidgets.QMessageBox.information(self, "Security code", "Security code has been sendet on your email")
            return {
            'code': code,
            'timestamp': time.time()
            }
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
            self.show_login()
    
    def show_password(self):
        if self.show_password_checkbox.isChecked():
            self.password_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)


    def show_login(self,event):
        self.controller = control.ControlWindow()
        self.controller.show_login()
        self.close()

import Backgrounds
if __name__ == '__main__':
    app = QApplication(sys.argv)
    registration_window = RegistrationWindow()
    registration_window.show()
    sys.exit(app.exec_())