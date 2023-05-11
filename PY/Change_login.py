import sys
import random
import smtplib
import control
from db_handler import SqliteDB
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
sec_code = None

class ChangeLoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Change login")
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



#Edit for old login(email)
        self.old_login_edit = QtWidgets.QLineEdit(self)
        self.old_login_edit.setGeometry(QtCore.QRect(160, 110, 241, 41))
        self.old_login_edit.setStyleSheet("QLineEdit {\n"
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
        self.old_login_edit.setInputMask("")
        self.old_login_edit.setToolTip("Your old E-mail adress")
        self.old_login_edit.setText("")
        self.old_login_edit.setObjectName("old_login_edit")
        self.old_login_edit.setWhatsThis("Edit for e-mail")
        self.old_login_edit.setPlaceholderText("Old Email")


        #Logo image
        self.logo_Login = QtWidgets.QLabel(self)
        self.logo_Login.setGeometry(QtCore.QRect(130, 40, 91, 61))
        self.logo_Login.setMinimumSize(QtCore.QSize(82, 45))
        self.logo_Login.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                        "image: url(:/newPrefix/images/backgrounds/PsLYIQ01.svg);")
        self.logo_Login.setObjectName("logo_Login")
        self.logo_Login.setText("<html><head/><body><p align=\"center\"><br/></p></body></html>")




#send code button 
        self.send_code_but = QtWidgets.QPushButton(self)
        self.send_code_but.setGeometry(QtCore.QRect(410, 140, 70, 31))
        self.send_code_but.setAutoFillBackground(False)
        self.send_code_but.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: outset;\n"
                        "font: 11pt \"MS Shell Dlg 2\";\n"
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
        self.send_code_but.setObjectName("ch_pass_but")
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
        self.ch_pass_but.setObjectName("ch_pass_but")
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
        self.back_but.setObjectName("back_but")
        self.back_but.setText("<")
        self.back_but.clicked.connect(self.back_to_profile)



        
#Edit for new email
        self.new_email_edit = QtWidgets.QLineEdit(self)
        self.new_email_edit.setGeometry(QtCore.QRect(160, 165, 241, 41))
        self.new_email_edit.setStyleSheet("QLineEdit {\n"
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
        self.new_email_edit.setInputMask("")
        self.new_email_edit.setToolTip("New email")
        self.new_email_edit.setText("")
        self.new_email_edit.setObjectName("new_email_edit")
        self.new_email_edit.setWhatsThis("Edit for new password")
        self.new_email_edit.setPlaceholderText("New email")



#Edit for password
        self.password_edit = QtWidgets.QLineEdit(self)
        self.password_edit.setGeometry(QtCore.QRect(160, 220, 241, 41))
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
        self.password_edit.setObjectName("password_edit")
        self.password_edit.setWhatsThis("Edit for Password")
        self.password_edit.setPlaceholderText("Password")
        self.password_edit.setReadOnly(True)



#Edit for email key
        self.email_key = QtWidgets.QLineEdit(self)
        self.email_key.setGeometry(QtCore.QRect(160, 275, 241, 41))
        self.email_key.setStyleSheet("QLineEdit {\n"
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
        self.email_key.setInputMask("")
        self.email_key.setToolTip("Email key")
        self.email_key.setText("")
        self.email_key.setObjectName("email_key")
        self.email_key.setWhatsThis("Edit for Email key")
        self.email_key.setPlaceholderText("Email key")
        self.email_key.setReadOnly(True)

#change password and add data to database
    def change_pass(self):
        if not self.password_edit.text() or not self.email_key.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Fill every fields please!")
        else:
            print(f"sec_code in change_pass def: type = {type(sec_code)} value = {sec_code}")
            password = str(self.password_edit.text())
            old_login = str(self.old_login_edit.text())
            new_login = str(self.new_email_edit.text())

            code = int(self.email_key.text())
            if code == sec_code:
                User_data = SqliteDB.get_user_data(old_login)
                if User_data[0]:
                    Person_id = User_data[1]
                    if SqliteDB.update_user_data(Person_id, None, new_login, None, None):
                        QtWidgets.QMessageBox.information(self, "Succesful!", "Your login has been changed!")
                        self.old_login_edit.setReadOnly(False)
                        self.old_login_edit.setText("")

                        self.new_email_edit.setReadOnly(False)
                        self.new_email_edit.setText("")

                        self.email_key.setReadOnly(False)
                        self.email_key.setText("")

                        self.password_edit.setReadOnly(False)
                        self.password_edit.setText("")

                        self.send_code_but.setDisabled(False)
                        self.back_to_profile()

                    else:
                        QtWidgets.QMessageBox.warning(self, "Error!", "Something went wrong!")
                        self.old_login_edit.setText("")
                        self.password_edit.setText("")
                        self.new_email_edit.setText("")
                        self.email_key.setText("")
                        self.send_code_but.setDisabled(False)
                else:
                    QtWidgets.QMessageBox.warning(self, "Error!", "Incorrect security code!")
                    self.old_login_edit.setText("")
                    self.password_edit.setText("")
                    self.new_email_edit.setText("")
                    self.email_key.setText("")
                    self.send_code_but.setDisabled(False)

#tanasiychukkirill@gmail.com

#send security code to user`s email
    def send_code(self):
        if not self.old_login_edit.text() or not self.new_email_edit.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Fill E-mail`s fields!")
        else:
            self.old_login_edit.setReadOnly(True)
            self.new_email_edit.setReadOnly(True)
            self.send_code_but.setDisabled(True)
            self.email_key.setReadOnly(False)
            self.password_edit.setReadOnly(False)

            old_login = self.old_login_edit.text()
            password = self.password_edit.text()


            User_data = SqliteDB.authenticate_user(old_login, password)
            if User_data[0]:
                new_login = self.new_email_edit.text()
                global sec_code
                sec_code = int(self.generate_code(new_login))
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Incorrect Login or Password!")
                self.old_login_edit.setReadOnly(False)
                self.old_login_edit.setText("")

                self.new_email_edit.setReadOnly(False)
                self.new_email_edit.setText("")

                self.send_code_but.setDisabled(False)
                self.email_key.setReadOnly(True)
                self.password_edit.setReadOnly(True)


#generate security code
    def generate_code(self,login) -> int:
            
            code = int(random.randint(100000, 999999))
            
            from_address = 'work.tanasiichuk@gmail.com'
            to_address = login
            subject = 'Security Code'
            body = f'Your security code is: {code}'
            message = f'Subject: {subject}\n\n{body}'
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_address, 'wilgfdzekbdoboxp')
            server.sendmail(from_address, to_address, message)
            server.quit()

            QtWidgets.QMessageBox.information(self, "Security code", "Security code has been sendet on your email")
            print(f"sec_code in generate_code def: type = {type(code)} value = {code}")
            return code


#close window
    def back_to_profile(self):
        self.old_login_edit.setText("")
        self.password_edit.setText("")
        self.new_email_edit.setText("")
        self.email_key.setText("")
        self.send_code_but.setDisabled(False)

        self.controller = control.ControlWindow()
        self.controller.show_profile()
        self.close()

import Backgrounds
if __name__ == '__main__':
    app = QApplication(sys.argv)
    new_pass_window = ChangeLoginWindow()
    new_pass_window.show()
    sys.exit(app.exec_())
