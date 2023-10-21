
#  _________      .__                 _________                __                .__   
# /   _____/ ____ |  | _____ _______  \_   ___ \  ____   _____/  |________  ____ |  |  
# \_____  \ /  _ \|  | \__  \\_  __ \ /    \  \/ /  _ \ /    \   __\_  __ \/  _ \|  |  
# /        (  <_> )  |__/ __ \|  | \/ \     \___(  <_> )   |  \  |  |  | \(  <_> )  |__
#/_______  /\____/|____(____  /__|     \______  /\____/|___|  /__|  |__|   \____/|____/
#        \/                 \/                \/            \/                         




import sys
import random
import smtplib
import control
from db_handler import SqliteDB
from PyQt5.QtGui import QFontDatabase, QFont, QRegion
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
sec_code = None

class ForgotPassWindow(QtWidgets.QWidget):
    def __init__(self):
        super(ForgotPassWindow, self).__init__()
        #logotype = QtGui.QIcon("C:\\Solar Control\\Solar-Control\\images\\backgrounds\\PsLYIQ01.svg")
        #self.setWindowIcon(logotype)
        #self.setWindowTitle("New password")
        
        self.setFixedSize(555,425)
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.51, y1:0, x2:0.508, y2:1, stop:0 rgba(54, 53, 93, 255), stop:1 rgba(73, 50, 93, 255));")
        self.setWindowOpacity(0.97)
        


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

        
        
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.all_layout = QtWidgets.QVBoxLayout()
        
        self.title = QtWidgets.QLabel("Solar Control")
        btn_size = 20

        self.btn_close = QtWidgets.QPushButton("✕")
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_close.setFixedSize(btn_size,24)
        self.btn_close.setStyleSheet("QPushButton {\n"
                                     "background-color: transparent;\n"
                                     "padding: 0;\n"
                                     "font-size: 14px\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "background-color: red;\n"
                                     "padding: 0;\n"
                                     "border: none\n"
                                     "}\n")

        self.btn_min = QtWidgets.QPushButton("─")
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.btn_min.setFixedSize(btn_size, 24)
        self.btn_min.setStyleSheet("QPushButton {\n"
                                   "background-color: transparent;\n"
                                   "padding: 0;\n"
                                   "font-size: 14px\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "background-color: #bfbfbf;\n"
                                   "padding: 0;\n"
                                   "border: none\n"
                                   "}\n")

        self.btn_max = QtWidgets.QPushButton("❐")
        #self.btn_max.clicked.connect(self.btn_max_clicked)
        self.btn_max.setFixedSize(btn_size, 24)
        self.btn_max.setStyleSheet("QPushButton {\n"
                                   "background-color: transparent;\n"
                                   "padding: 0;\n"
                                   "font-size: 14px\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "background-color: #bfbfbf;\n"
                                   "padding: 0;\n"
                                   "border: none\n"
                                   "}\n")

        self.title.setFixedWidth(555)
        self.title.setFixedHeight(24)
        self.title.setAlignment(QtCore.Qt.AlignTop)
        

        self.title_bar_layout = QtWidgets.QHBoxLayout()
        self.title_bar_layout.setContentsMargins(0,0,0,0)
        self.title_bar_layout.addStretch()
        self.title_bar_layout.addWidget(self.title)
        self.title_bar_layout.addWidget(self.btn_min)
        self.title_bar_layout.addWidget(self.btn_max)
        self.title_bar_layout.addWidget(self.btn_close)

        self.title.setStyleSheet("""
            background-color: white;
            color: white;
        """)
        
        self.all_layout.addLayout(self.title_bar_layout)
        self.all_layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.all_layout)
        self.all_layout.setAlignment(QtCore.Qt.AlignTop)
        #self.title_bar_layout.setGeometry(QtCore.QRect(0,0,20,400))
        self.start = QtCore.QPoint(0, 0)
        self.pressing = False


        #Logo name(SOLAR CONTROL)
        self.logo_name_lab = QtWidgets.QLabel(self)
        self.logo_name_lab.setGeometry(QtCore.QRect(190, 95, 180, 31))
        self.logo_name_lab.setToolTip("")
        self.logo_name_lab.setAutoFillBackground(False)
        self.logo_name_lab.setStyleSheet("border: 0px; background-color:rgba(0,0,0,0%);")
        self.logo_name_lab.setObjectName("logo_name_lab")
        self.logo_name_lab.setFont(self.logo_font)
        self.logo_name_lab.setText("<html><head/><body><p align=\"center\">SOLAR CONTROL</p></body></html>")



        #Edit for login(email)
        self.login_edit = QtWidgets.QLineEdit(self)
        self.login_edit.setGeometry(QtCore.QRect(160, 145, 241, 41))
        self.login_edit.setStyleSheet("QLineEdit {\n"
                        "color: white;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
                        "min-width: 8em;\n"
                        "background-color: rgb(35, 36, 64);\n"
                        "padding: 5px;\n"
                        "}\n"
                        "\n"
                        "QLineEdit:hover {\n"
                        "background-color: rgb(25, 26, 54);\n"
                        "}\n"
                        "\n"
                        "QLineEdit:pressed {\n"
                        "border-style: inset;\n"
                        "background-color: rgb(25, 26, 54);\n"
                        "}")
        self.login_edit.setInputMask("")
        self.login_edit.setToolTip("Your E-mail adress")
        self.login_edit.setObjectName("login_edit")
        self.login_edit.setFont(self.edit_font)
        self.login_edit.setWhatsThis("Edit for e-mail")
        self.login_edit.setPlaceholderText("Email")


        #Logo image
        self.logo_Login = QtWidgets.QLabel(self)
        self.logo_Login.setGeometry(QtCore.QRect(100, 75, 91, 61))
        self.logo_Login.setMinimumSize(QtCore.QSize(82, 45))
        self.logo_Login.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                        "image: url(:/newPrefix/images/backgrounds/PsLYIQ01.svg);")
        self.logo_Login.setObjectName("logo_Login")
        self.logo_Login.setText("<html><head/><body><p align=\"center\"><br/></p></body></html>")




#send security code button 
        self.send_code_but = QtWidgets.QPushButton(self)
        self.send_code_but.setGeometry(QtCore.QRect(410, 149, 70, 31))
        self.send_code_but.setAutoFillBackground(False)
        self.send_code_but.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: outset;\n"
                        "max-width: 131px;\n"
                        "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(102, 224, 231, 255), stop:1 rgba(229, 135, 219, 255));\n"
                        "padding: 5px;\n"
                        "}\n"
                        "\n"
                        "QPushButton:hover {\n"
                        "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(122, 244, 251, 255), stop:1 rgba(249, 155, 239, 255));\n"
                        "}\n"
                        "\n"
                        "QPushButton:pressed {\n"
                        "border-style: inset;\n"
                        "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(137, 255, 255, 255), stop:1 rgba(255, 170, 254, 255));\n"
                        "}")
        self.send_code_but.setObjectName("send_code_but")
        self.send_code_but.setFont(self.button_font)
        self.send_code_but.setText("Send")
        self.send_code_but.clicked.connect(self.send_code)


        


        #change pass button 
        self.ch_pass_but = QtWidgets.QPushButton(self)
        self.ch_pass_but.setGeometry(QtCore.QRect(215, 325, 131, 41))
        self.ch_pass_but.setMinimumSize(QtCore.QSize(131, 41))
        self.ch_pass_but.setMaximumSize(QtCore.QSize(145, 41))
        self.ch_pass_but.setAutoFillBackground(False)
        self.ch_pass_but.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
                        "max-width: 131px;\n"
                        "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(102, 224, 231, 255), stop:1 rgba(229, 135, 219, 255));\n"
                        "padding: 5px;\n"
                        "}\n"
                        "\n"
                        "QPushButton:hover {\n"
                        "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(122, 244, 251, 255), stop:1 rgba(249, 155, 239, 255));\n"
                        "}\n"
                        "\n"
                        "QPushButton:pressed {\n"
                        "border-style: inset;\n"
                        "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(137, 255, 255, 255), stop:1 rgba(255, 170, 254, 255));\n"
                        "}")
        self.ch_pass_but.setObjectName("ch_pass_but")
        self.ch_pass_but.setFont(self.button_font)
        self.ch_pass_but.setText("Change")
        self.ch_pass_but.clicked.connect(self.change_pass)





        #Back button 
        self.back_but = QtWidgets.QPushButton(self)
        self.back_but.setGeometry(QtCore.QRect(0, 24, 30, 30))
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
        self.back_but.setText("<")
        self.back_but.setFont(self.button_font)
        self.back_but.clicked.connect(self.back_to_login)



        
        #Edit for password
        self.password_edit = QtWidgets.QLineEdit(self)
        self.password_edit.setGeometry(QtCore.QRect(160, 200, 241, 41))
        self.password_edit.setStyleSheet("QLineEdit {\n"
                        "color: white;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
                        "min-width: 8em;\n"
                        "background-color: rgb(35, 36, 64);\n"
                        "padding: 5px;\n"
                        "}\n"
                        "\n"
                        "QLineEdit:hover {\n"
                        "background-color: rgb(25, 26, 54);\n"
                        "}\n"
                        "\n"
                        "QLineEdit:pressed {\n"
                        "border-style: inset;\n"
                        "background-color: rgb(25, 26, 54);\n"
                        "}")
        self.password_edit.setInputMask("")
        self.password_edit.setToolTip("New password")
        self.password_edit.setText("")
        self.password_edit.setPlaceholderText("")
        self.password_edit.setObjectName("password_edit")
        self.password_edit.setFont(self.edit_font)
        self.password_edit.setWhatsThis("Edit for Password")
        self.password_edit.setPlaceholderText("New password")
        self.password_edit.setReadOnly(True)
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)



        
        self.eye_file_open = QtGui.QIcon("C:\\Users\\Admin\\Downloads\\icons8-показать-64.png")
        
        self.show_pass_button = QtWidgets.QPushButton(self)
        self.show_pass_button.setGeometry(QtCore.QRect(368, 207, 30, 30))
        self.show_pass_button.setAutoFillBackground(False)
        self.show_pass_button.setStyleSheet("QPushButton {\n"
                                            "background-color: transparent;\n"
                                            "padding: 0;\n"
                                            #"font-size: 14px\n"
                                            "}\n"
                                            )
        self.show_pass_button.setObjectName("back_but")
        self.show_pass_button.setIcon(self.eye_file_open)
        self.show_pass_button.setFont(self.button_font)
        self.show_pass_button.clicked.connect(self.show_password)



#Edit for email key
        self.email_key = QtWidgets.QLineEdit(self)
        self.email_key.setGeometry(QtCore.QRect(160, 255, 241, 41))
        self.email_key.setStyleSheet("QLineEdit {\n"
                        "color: white;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
                        "min-width: 8em;\n"
                        "background-color: rgb(35, 36, 64);\n"
                        "padding: 5px;\n"
                        "}\n"
                        "\n"
                        "QLineEdit:hover {\n"
                        "background-color: rgb(25, 26, 54);\n"
                        "}\n"
                        "\n"
                        "QLineEdit:pressed {\n"
                        "border-style: inset;\n"
                        "background-color: rgb(25, 26, 54);\n"
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
        if not self.password_edit.text() or not self.email_key.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Fill every fields please!")
        else:
            print(f"sec_code in change_pass def: type = {type(sec_code)} value = {sec_code}")
            password = str(self.password_edit.text())
            login = str(self.login_edit.text())
            code = int(self.email_key.text())
            if code == sec_code:
                User_data = SqliteDB.get_user_data(login, None)[0]
                Person_id = User_data["Person_id"]
                if SqliteDB.update_user_data(Person_id, None, None, None, password, None):
                    QtWidgets.QMessageBox.information(self, "Succesful!", "Your password has been changed!")
                    self.login_edit.setReadOnly(False)
                    self.login_edit.setText("")
                    self.email_key.setReadOnly(False)
                    self.email_key.setText("")
                    self.password_edit.setReadOnly(False)
                    self.password_edit.setText("")

                    self.send_code_but.setDisabled(False)
                    self.back_to_login()

                else:
                    QtWidgets.QMessageBox.warning(self, "Error!", "Something went wrong!")
                    self.login_edit.setText("")
                    self.password_edit.setText("")
                    self.email_key.setText("")
                    self.send_code_but.setDisabled(False)
            else:
                QtWidgets.QMessageBox.warning(self, "Error!", "Incorrect security code!")
                self.login_edit.setText("")
                self.password_edit.setText("")
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
            self.password_edit.setReadOnly(False)

            login = self.login_edit.text()
            global sec_code
            sec_code = int(self.generate_code(login))

#generate security code
    def generate_code(self,login) -> int:
        try:
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
            return code
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
            self.back_to_login()

#show password
    def show_password(self):
        eye_file_close = QtGui.QIcon("C:\\Users\\Admin\\Downloads\\icons8-показать-64 (1).png")
        if self.password_edit.echoMode() == QtWidgets.QLineEdit.Password:
            self.password_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.show_pass_button.setIcon(eye_file_close)
        else:
            self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_pass_button.setIcon(self.eye_file_open)



#close window
    def back_to_login(self):
        self.login_edit.setText("")
        self.password_edit.setText("")
        self.email_key.setText("")


        self.controller = control.ControlWindow()
        self.controller.show_login()
        self.close()




    def resizeEvent(self, QResizeEvent):
        super(ForgotPassWindow, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.width(),
                                self.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False


    def btn_close_clicked(self):
        self.close()

    def btn_max_clicked(self):
        self.showMaximized()

    def btn_min_clicked(self):
        self.showMinimized()
        
import Backgrounds
if __name__ == '__main__':
    app = QApplication(sys.argv)
    new_pass_window = ForgotPassWindow()
    new_pass_window.show()
    sys.exit(app.exec_())
