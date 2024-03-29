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

class ChangePassWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        logotype = QtGui.QIcon("C:\\Solar Control\\Solar-Control\\images\\backgrounds\\PsLYIQ01.svg")
        self.setWindowIcon(logotype)
        self.setWindowTitle("Change password")
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


        #Logo name(SOLAR CONTROL)
        self.logo_name_lab = QtWidgets.QLabel(self)
        self.logo_name_lab.setGeometry(QtCore.QRect(190, 60, 180, 31))
        self.logo_name_lab.setToolTip("")
        self.logo_name_lab.setAutoFillBackground(False)
        self.logo_name_lab.setStyleSheet("border: 0px; background-color:rgba(0,0,0,0%);")
        self.logo_name_lab.setObjectName("logo_name_lab")
        self.logo_name_lab.setFont(self.logo_font)
        self.logo_name_lab.setText("<html><head/><body><p align=\"center\">SOLAR CONTROL</p></body></html>")



        #Edit for login(email)
        self.login_edit = QtWidgets.QLineEdit(self)
        self.login_edit.setGeometry(QtCore.QRect(160, 110, 241, 41))
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
        self.login_edit.setToolTip("Your E-mail adress")
        self.login_edit.setText("")
        self.login_edit.setPlaceholderText("")
        self.login_edit.setObjectName("login_edit")
        self.login_edit.setFont(self.edit_font)
        self.login_edit.setWhatsThis("Edit for e-mail")
        self.login_edit.setPlaceholderText("Email")


        #Logo image
        self.logo_Login = QtWidgets.QLabel(self)
        self.logo_Login.setGeometry(QtCore.QRect(100, 40, 91, 61))
        self.logo_Login.setMinimumSize(QtCore.QSize(82, 45))
        self.logo_Login.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                        "image: url(:/newPrefix/images/backgrounds/PsLYIQ01.svg);")
        self.logo_Login.setObjectName("logo_Login")
        self.logo_Login.setText("<html><head/><body><p align=\"center\"><br/></p></body></html>")




#send code button 
        self.send_code_but = QtWidgets.QPushButton(self)
        self.send_code_but.setGeometry(QtCore.QRect(410, 114, 70, 31))
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


        


#change pass button 
        self.ch_pass_but = QtWidgets.QPushButton(self)
        self.ch_pass_but.setGeometry(QtCore.QRect(215, 345, 131, 41))
        self.ch_pass_but.setMinimumSize(QtCore.QSize(131, 41))
        self.ch_pass_but.setMaximumSize(QtCore.QSize(145, 41))
        self.ch_pass_but.setAutoFillBackground(False)
        self.ch_pass_but.setStyleSheet("QPushButton {\n"
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
        self.ch_pass_but.setObjectName("ch_pass_but")
        self.ch_pass_but.setFont(self.button_font)
        self.ch_pass_but.setText("Change")
        self.ch_pass_but.clicked.connect(self.change_pass)





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
        self.back_but.clicked.connect(self.back_to_profile)



        
#Edit for old password
        self.old_password_edit = QtWidgets.QLineEdit(self)
        self.old_password_edit.setGeometry(QtCore.QRect(160, 165, 241, 41))
        self.old_password_edit.setStyleSheet("QLineEdit {\n"
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
        self.old_password_edit.setInputMask("")
        self.old_password_edit.setToolTip("Old password")
        self.old_password_edit.setText("")
        self.old_password_edit.setObjectName("password_edit")
        self.old_password_edit.setFont(self.edit_font)
        self.old_password_edit.setWhatsThis("Edit for Password")
        self.old_password_edit.setPlaceholderText("Old password")
        self.old_password_edit.setReadOnly(True)
        self.old_password_edit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.show_password_checkbox = QtWidgets.QCheckBox(self)
        self.show_password_checkbox.setText("Show")
        self.show_password_checkbox.setGeometry(420,197,57,30)
        self.show_password_checkbox.setFont(self.label_font)
        self.show_password_checkbox.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n")
        self.show_password_checkbox.clicked.connect(self.show_password)




#Edit for old password
        self.new_password_edit = QtWidgets.QLineEdit(self)
        self.new_password_edit.setGeometry(QtCore.QRect(160, 220, 241, 41))
        self.new_password_edit.setStyleSheet("QLineEdit {\n"
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
        self.new_password_edit.setInputMask("")
        self.new_password_edit.setToolTip("New password")
        self.new_password_edit.setText("")
        self.new_password_edit.setPlaceholderText("")
        self.new_password_edit.setObjectName("new_password_edit")
        self.new_password_edit.setFont(self.edit_font)
        self.new_password_edit.setWhatsThis("Edit for Password")
        self.new_password_edit.setPlaceholderText("New password")
        self.new_password_edit.setReadOnly(True)
        self.new_password_edit.setEchoMode(QtWidgets.QLineEdit.Password)



#Edit for email key
        self.email_key = QtWidgets.QLineEdit(self)
        self.email_key.setGeometry(QtCore.QRect(160, 275, 241, 41))
        self.email_key.setStyleSheet("QLineEdit {\n"
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
        self.email_key.setInputMask("")
        self.email_key.setToolTip("Email key")
        self.email_key.setText("")
        self.email_key.setPlaceholderText("")
        self.email_key.setObjectName("email_key")
        self.email_key.setFont(self.edit_font)
        self.email_key.setWhatsThis("Edit for Email key")
        self.email_key.setPlaceholderText("Email key")
        self.email_key.setReadOnly(True)

#change password and add data to database
    def change_pass(self):
        if not self.old_password_edit.text() or not self.email_key.text() or not self.new_password_edit.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Fill every fields please!")
        else:
            print(f"sec_code in change_pass def: type = {type(sec_code)} value = {sec_code}")
            old_password = str(self.old_password_edit.text())
            new_password = str(self.old_password_edit.text())
            login = str(self.login_edit.text())
            code = int(self.email_key.text())
            if code == sec_code["code"] and (time.time() - sec_code['timestamp']) < 180:
                User_data = SqliteDB.authenticate_user(login, old_password)
                if User_data[0]:
                    Person_id = User_data[1]
                    if SqliteDB.update_user_data(Person_id, None, None, None, new_password, None):
                        QtWidgets.QMessageBox.information(self, "Succesful!", "Your password has been changed!")
                        self.login_edit.setReadOnly(False)
                        self.login_edit.setText("")
                        self.email_key.setReadOnly(False)
                        self.email_key.setText("")
                        self.old_password_edit.setReadOnly(False)
                        self.old_password_edit.setText("")
                        self.new_password_edit.setReadOnly(False)
                        self.new_password_edit.setText("")

                        self.send_code_but.setDisabled(False)
                        self.back_to_profile()

                    else:
                        QtWidgets.QMessageBox.warning(self, "Error!", "Something went wrong!")
                        self.login_edit.setText("")
                        self.old_password_edit.setText("")
                        self.new_password_edit.setText("")
                        self.email_key.setText("")
                        self.send_code_but.setDisabled(False)
                else:
                    QtWidgets.QMessageBox.warning(self, "Error!", "Incorrect security code!")
                    self.login_edit.setText("")
                    self.old_password_edit.setText("")
                    self.new_password_edit.setText("")
                    self.email_key.setText("")
                    self.send_code_but.setDisabled(False)

#tanasiychukkirill@gmail.com

#send security code to user`s email
    def send_code(self):
        if not self.login_edit.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Write your E-mail!")
        else:
            self.login_edit.setReadOnly(True)
            self.send_code_but.setDisabled(True)
            self.email_key.setReadOnly(False)
            self.old_password_edit.setReadOnly(False)
            self.new_password_edit.setReadOnly(False)

            login = self.login_edit.text()
            global sec_code
            sec_code = self.generate_code(login)

#generate security code
    def generate_code(self,login) -> int:
        try:    
            code = int(random.randint(100000, 999999))
            
            from_address = 'email'
            to_address = login
            subject = 'Security Code'
            body = f'Your security code is: {code}'
            message = f'Subject: {subject}\n\n{body}'
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_address, '00000000')
            server.sendmail(from_address, to_address, message)
            server.quit()

            QtWidgets.QMessageBox.information(self, "Security code", "Security code has been sendet on your email")
            return {
            'code': code,
            'timestamp': time.time()
            }
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
            self.back_to_profile()


    def show_password(self):
        if self.show_password_checkbox.isChecked():
            self.old_password_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.new_password_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.old_password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.new_password_edit.setEchoMode(QtWidgets.QLineEdit.Normal)



#close window
    def back_to_profile(self):
        self.login_edit.setText("")
        self.old_password_edit.setText("")
        self.new_password_edit.setText("")
        self.email_key.setText("")


        self.controller = control.ControlWindow()
        self.controller.show_profile()
        self.close()

import Backgrounds
if __name__ == '__main__':
    app = QApplication(sys.argv)
    new_pass_window = ChangePassWindow()
    new_pass_window.show()
    sys.exit(app.exec_())
