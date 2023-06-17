import sys
import control
from db_handler import SqliteDB
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class ChangeNameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        logotype = QtGui.QIcon("C:\\Solar Control\\Solar-Control\\images\\backgrounds\\PsLYIQ01.svg")
        self.setWindowIcon(logotype)
        self.controller = control.ControlWindow()
        self.setWindowTitle("Change login")
        self.setFixedSize(455,300)
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
        self.logo_name_lab.setGeometry(QtCore.QRect(140, 60, 180, 31))
        self.logo_name_lab.setToolTip("")
        self.logo_name_lab.setAutoFillBackground(False)
        self.logo_name_lab.setStyleSheet("border: 0px; background-color:rgba(0,0,0,0%);")
        self.logo_name_lab.setObjectName("logo_name_lab")
        self.logo_name_lab.setFont(self.logo_font)
        self.logo_name_lab.setText("<html><head/><body><p align=\"center\">SOLAR CONTROL</p></body></html>")



#Edit for old login(email)
        self.new_name_edit = QtWidgets.QLineEdit(self)
        self.new_name_edit.setGeometry(QtCore.QRect(105, 110, 241, 41))
        self.new_name_edit.setStyleSheet("QLineEdit {\n"
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
        self.new_name_edit.setInputMask("")
        self.new_name_edit.setToolTip("Your new name")
        self.new_name_edit.setText("")
        self.new_name_edit.setObjectName("new_name_edit")
        self.new_name_edit.setFont(self.edit_font)
        self.new_name_edit.setWhatsThis("Edit for name")
        self.new_name_edit.setPlaceholderText("Нове Ім'я")


        #Logo image
        self.logo_Login = QtWidgets.QLabel(self)
        self.logo_Login.setGeometry(QtCore.QRect(45, 40, 91, 61))
        self.logo_Login.setMinimumSize(QtCore.QSize(82, 45))
        self.logo_Login.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                        "image: url(:/newPrefix/images/backgrounds/PsLYIQ01.svg);")
        self.logo_Login.setObjectName("logo_Login")
        self.logo_Login.setText("<html><head/><body><p align=\"center\"><br/></p></body></html>")

        


#change name button 
        self.ch_name_but = QtWidgets.QPushButton(self)
        self.ch_name_but.setGeometry(QtCore.QRect(160, 175, 131, 41))
        self.ch_name_but.setMinimumSize(QtCore.QSize(131, 41))
        self.ch_name_but.setMaximumSize(QtCore.QSize(145, 41))
        self.ch_name_but.setAutoFillBackground(False)
        self.ch_name_but.setStyleSheet("QPushButton {\n"
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
        self.ch_name_but.setObjectName("ch_name_but")
        self.ch_name_but.setFont(self.button_font)
        self.ch_name_but.setText("Змінити")
        self.ch_name_but.clicked.connect(self.change_name)





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



#change password and add data to database
    def change_name(self):
        if not self.new_name_edit.text():
            QtWidgets.QMessageBox.warning(self, "Увага", "Заповніть всі поля!")
        else:
            
            new_name = str(self.new_name_edit.text())
            if SqliteDB.update_user_data(self.controller.session_id, new_name, None, None, None, None):
                QtWidgets.QMessageBox.information(self, "Успішно!", "Ваше ім'я було змінено!")
                self.back_to_profile()
            else:
                QtWidgets.QMessageBox.warning(self, "Помилка!", "Щось пішло не так!")        
                self.back_to_profile()

#close window
    def back_to_profile(self):
        self.new_name_edit.setText("")
        
        self.controller.show_profile()
        self.close()

import Backgrounds
if __name__ == '__main__':
    app = QApplication(sys.argv)
    new_pass_window = ChangeNameWindow()
    new_pass_window.show()
    sys.exit(app.exec_())
