

#  _________      .__                 _________                __                .__   
# /   _____/ ____ |  | _____ _______  \_   ___ \  ____   _____/  |________  ____ |  |  
# \_____  \ /  _ \|  | \__  \\_  __ \ /    \  \/ /  _ \ /    \   __\_  __ \/  _ \|  |  
# /        (  <_> )  |__/ __ \|  | \/ \     \___(  <_> )   |  \  |  |  | \(  <_> )  |__
#/_______  /\____/|____(____  /__|     \______  /\____/|___|  /__|  |__|   \____/|____/
#        \/                 \/                \/            \/                         



import sys
import control
from db_handler import SqliteDB
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

session_id = None
session_name = None
session_login = None
session_binary_avatar = None
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #logotype = QtGui.QIcon("C:\\Solar Control\\Solar-Control\\images\\backgrounds\\PsLYIQ01.svg")
        #self.setWindowIcon(logotype)
        self.controller = control.ControlWindow()

        self.setFixedSize(555,425)
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.51, y1:0, x2:0.508, y2:1, stop:0 rgba(54, 53, 93, 255), stop:1 rgba(73, 50, 93, 255));")
        self.setWindowOpacity(0.97)
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        


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
        central_widget.setLayout(self.all_layout)
        self.all_layout.setAlignment(QtCore.Qt.AlignTop)
        #self.title_bar_layout.setGeometry(QtCore.QRect(0,0,20,400))
        self.start = QtCore.QPoint(0, 0)
        self.pressing = False


        #Logo name(SOLAR CONTROL)
        self.logo_name_lab = QtWidgets.QLabel(self)
        self.logo_name_lab.setGeometry(QtCore.QRect(190, 95, 180, 31))
        self.logo_name_lab.setToolTip("")
        self.logo_name_lab.setAutoFillBackground(False)
        self.logo_name_lab.setStyleSheet("color: white; border: 0px; background-color:rgba(0,0,0,0%);")
        self.logo_name_lab.setObjectName("logo_name_lab")
        self.logo_name_lab.setFont(self.logo_font)
        self.logo_name_lab.setText("SOLAR CONTROL")



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
        self.logo_Login.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n" "image: url(C:/Solar Control/Solar-Control/images/backgrounds/PsLYIQ01.svg);")

        self.logo_Login.setObjectName("logo_Login")
        self.logo_Login.setText("<html><head/><body><p align=\"center\"><br/></p></body></html>")

        
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
        self.password_edit.setToolTip("Your password")
        self.password_edit.setPlaceholderText("")
        self.password_edit.setObjectName("password_edit")
        self.password_edit.setFont(self.edit_font)
        self.password_edit.setWhatsThis("Edit for Password")
        self.password_edit.setPlaceholderText("Password")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.eye_file_open = QtGui.QIcon("C:\\Solar Control\\Solar-Control\\images\\opened_eye.png")
        
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
        


        #Link lable to register window
        self.link_reg = QtWidgets.QLabel(self)
        self.link_reg.setGeometry(QtCore.QRect(170, 370, 171, 31))
        self.link_reg.setToolTip("")
        self.link_reg.setAutoFillBackground(False)
        self.link_reg.setStyleSheet("border: 0px; background-color:rgba(0,0,0,0%);")
        self.link_reg.setObjectName("link_reg")
        self.link_reg.setFont(self.label_font)
        self.link_reg.setText("<html><head/><body><p style=\" color:#FFFFFF;\" align=\"center\">Don`t have an account?</p></body></html>")

        self.link_reg_2 = QtWidgets.QLabel(self)
        self.link_reg_2.setGeometry(QtCore.QRect(275, 370, 171, 31))
        self.link_reg_2.setToolTip("")
        self.link_reg_2.setAutoFillBackground(False)
        self.link_reg_2.setStyleSheet("border: 0px; background-color:rgba(0,0,0,0%);")
        self.link_reg_2.setObjectName("link_reg_2")
        self.link_reg_2.setFont(self.label_font)
        self.link_reg_2.setText("<html><head/><body><p style=\" color:#FF8C00;\" align=\"center\">Sign in </p></body></html>")
        self.link_reg_2.mousePressEvent = self.show_sign_in



        #Link lable to register window
        self.link_forg = QtWidgets.QLabel(self)
        self.link_forg.setGeometry(QtCore.QRect(190, 350, 171, 31))
        self.link_forg.setToolTip("")
        self.link_forg.setAutoFillBackground(False)
        self.link_forg.setStyleSheet("border: 0px; background-color:rgba(0,0,0,0%);")
        self.link_forg.setObjectName("link_forg")
        self.link_forg.setFont(self.label_font)
        self.link_forg.setText("<html><head/><body><p style=\" color:#FF8C00;\" align=\"center\">Forgot password?</p></body></html>")
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
        self.log_in_But.setObjectName("Log_in_But")
        self.log_in_But.setText("Log in")
        self.log_in_But.setFont(self.button_font)
        self.log_in_But.clicked.connect(self.log_check)


#show password
    def show_password(self):
        eye_file_close = QtGui.QIcon("C:\\Solar Control\\Solar-Control\\images\\closed_eye.png")
        if self.password_edit.echoMode() == QtWidgets.QLineEdit.Password:
            self.password_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.show_pass_button.setIcon(eye_file_close)
        else:
            self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_pass_button.setIcon(self.eye_file_open)


    def resizeEvent(self, QResizeEvent):
        super(LoginWindow, self).resizeEvent(QResizeEvent)
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




    def log_check(self):
        if not self.login_edit.text() or not self.password_edit.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Fill every fields please!")
        else:
                user_name = str(self.login_edit.text())
                password = str(self.password_edit.text())
                result = SqliteDB.authenticate_user(user_name, password)

                if result[0]:
                    User_data, Binary_avatar = SqliteDB.get_user_data(user_name,None)
                    

                    global session_id
                    global session_login
                    global session_name
                    global session_binary_avatar

                    session_id = result[1]
                    session_login = user_name
                    session_name = User_data["P_name"]
                    session_binary_avatar = Binary_avatar

                    self.controller = control.ControlWindow()
                    self.controller.show_profile()
                    self.close()
                else:
                    QtWidgets.QMessageBox.warning(self, "Error", "Something went wrong. Please, try again")


    def show_sign_in(self,event):
        self.login_edit.setText("")
        self.password_edit.setText("")

        
        self.controller.show_sign_in()
        self.close()

    def show_forgot_pass(self,event):
        self.login_edit.setText("")
        self.password_edit.setText("")
    
        self.controller.show_forgot_pass()
        self.close()

import Backgrounds
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
