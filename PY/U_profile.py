import typing
from PyQt5.QtWidgets import QWidget
import control
from PyQt5 import QtCore, QtGui, QtWidgets


class ProfileWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SOLAR CONTROL")
        self.resize(1180, 727)
        self.setMinimumSize(QtCore.QSize(1180, 727))
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.482198, y1:0.971, x2:0.497, y2:0.023, stop:0.0338983 rgba(46, 46, 46, 255), stop:1 rgba(168, 168, 168, 255));")


#create  Tab Widget
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(9, 9, 1162, 709))
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-style: outset;\n"
                        "font: 10pt \"MS Shell Dlg 2\";\n"
                        "background: qradialgradient(\n"
                        "cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                        "radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
                        "box-shadow: 25px 25px 20px #888888;\n"
                        "min-width: 100px; min-height: 17px;\n"
                        "border-top-left-radius: 15px;\n"
                        "border-top-right-radius: 15px;\n"
                        "padding: 5px;}\n"
                        "\n"
                        "QTabBar::tab:hover {\n"
                        "background: qradialgradient(\n"
                        "cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                        "radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                        ");\n"
                        "}\n"
                        "\n"
                        "QTabBar::tab:pressed {\n"
                        "border-style: inset;\n"
                        "background: qradialgradient(\n"
                        "cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                        "radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                        ");\n"
                        "}")
        self.tabWidget.setObjectName("tabWidget")


#create Tab for profile
        self.U_profile_tab = QtWidgets.QWidget()
        self.U_profile_tab.setObjectName("U_profile_tab")


#creating layouts
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.U_profile_tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Check_lay_prof = QtWidgets.QGridLayout()
        self.Check_lay_prof.setObjectName("Check_lay_prof")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Check_lay_prof.addItem(spacerItem, 2, 0, 1, 1)


#create listView for support information 
        self.Support_data_prof = QtWidgets.QListView(self.U_profile_tab)
        self.Support_data_prof.setMinimumSize(QtCore.QSize(250, 135))
        self.Support_data_prof.setMaximumSize(QtCore.QSize(250, 135))
        self.Support_data_prof.setStyleSheet("background-color: rgb(168, 168, 168);\n""")
        self.Support_data_prof.setObjectName("Support_data_prof")
        self.Check_lay_prof.addWidget(self.Support_data_prof, 2, 1, 1, 1)


#Edit for finding information about solar panels group (Profile)
        self.Search_ed_prof = QtWidgets.QLineEdit(self.U_profile_tab)
        self.Search_ed_prof.setMinimumSize(QtCore.QSize(150, 41))
        self.Search_ed_prof.setMaximumSize(QtCore.QSize(220, 41))



#Colors
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(166, 166, 166))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(166, 166, 166))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(166, 166, 166))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(166, 166, 166))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(166, 166, 166))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(166, 166, 166))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(166, 166, 166))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(166, 166, 166))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(166, 166, 166))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)




#set styleSheet for searching edit
        self.Search_ed_prof.setPalette(palette)
        self.Search_ed_prof.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
                        "font: 12pt \"MS Shell Dlg 2\";\n"
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
        self.Search_ed_prof.setObjectName("Search_ed_prof")
#add to layout
        self.Check_lay_prof.addWidget(self.Search_ed_prof, 1, 0, 1, 1)


#Button for finding data about group of solar panels(profile)
        self.Search_but_prof = QtWidgets.QPushButton(self.U_profile_tab)
        self.Search_but_prof.setMinimumSize(QtCore.QSize(150, 41))
        self.Search_but_prof.setMaximumSize(QtCore.QSize(131, 41))
        self.Search_but_prof.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
                        "font: 12pt \"MS Shell Dlg 2\";\n"
                        "min-width: 8em;\n"
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
        self.Search_but_prof.setObjectName("Search_but_prof")
        self.Search_but_prof.setText("Search")
#add to layout
        self.Check_lay_prof.addWidget(self.Search_but_prof, 1, 1, 1, 1)


#Label for username(profile)
        self.gridLayout.addLayout(self.Check_lay_prof, 4, 2, 1, 1)
        self.U_name_prof = QtWidgets.QLabel(self.U_profile_tab)
        self.U_name_prof.setMinimumSize(QtCore.QSize(250, 41))
        self.U_name_prof.setText("<html><head/><body><p align=\"center\">Name</p></body></html>")



#Colors
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)



        self.U_name_prof.setPalette(palette)
        self.U_name_prof.setStyleSheet("background-color: rgba(255, 255, 255, 10);")
        self.U_name_prof.setObjectName("U_name_prof")
#add to layout
        self.gridLayout.addWidget(self.U_name_prof, 3, 0, 1, 1)

#Table Widget for main information about solar panel`s group
        self.Objects_info_prof = QtWidgets.QTableWidget(self.U_profile_tab)
        self.Objects_info_prof.setMinimumSize(QtCore.QSize(850, 391))
        self.Objects_info_prof.setMaximumSize(QtCore.QSize(850, 391))
        self.Objects_info_prof.setStyleSheet("background-color: rgb(168, 168, 168);\n""")
        self.Objects_info_prof.setColumnCount(4)
        self.Objects_info_prof.setObjectName("Objects_info_prof")
        self.Objects_info_prof.setRowCount(0)
#add to layout
        self.gridLayout.addWidget(self.Objects_info_prof, 1, 2, 1, 1)


#layout for user photo(profile)
        self.Photo_lay_prof = QtWidgets.QGridLayout()
        self.Photo_lay_prof.setObjectName("Photo_lay_prof")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Photo_lay_prof.addItem(spacerItem1, 1, 2, 1, 1)

#label for user photo(profile)
        self.U_photo_prof = QtWidgets.QLabel(self.U_profile_tab)
        self.U_photo_prof.setMinimumSize(QtCore.QSize(169, 169))
        self.U_photo_prof.setMaximumSize(QtCore.QSize(169, 169))
        self.U_photo_prof.setStyleSheet("border: 3px solid black;\n"
                        "border-radius: 80px;\n"
                        "background-color: rgba(255, 255, 255, 10);")
        self.U_photo_prof.setObjectName("U_photo_prof")
        self.U_photo_prof.setText("<html><head/><body><p align=\"center\">Photo</p></body></html>")
#add to layout
        self.Photo_lay_prof.addWidget(self.U_photo_prof, 0, 0, 2, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Photo_lay_prof.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Photo_lay_prof.addItem(spacerItem3, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.Photo_lay_prof, 0, 0, 3, 2)


#layout for logo(profile)
        self.Prof_logo_lay = QtWidgets.QGridLayout()
        self.Prof_logo_lay.setObjectName("Prof_logo_lay")

#Logo lable(profile)
        self.Logo_prof = QtWidgets.QLabel(self.U_profile_tab)
        self.Logo_prof.setMinimumSize(QtCore.QSize(82, 45))
        self.Logo_prof.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                        "image: url(:/newPrefix/images/backgrounds/PsLYIQ01.svg);")
        self.Logo_prof.setObjectName("Logo_prof")
        self.Logo_prof.setText("<html><head/><body><p align=\"center\"><br/></p></body></html>")
#add to layout
        self.Prof_logo_lay.addWidget(self.Logo_prof, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Prof_logo_lay.addItem(spacerItem4, 0, 1, 1, 1)


#logout button(profile)
        self.Log_out_but_prof = QtWidgets.QPushButton(self.U_profile_tab)
        self.Log_out_but_prof.setMinimumSize(QtCore.QSize(145, 41))
        self.Log_out_but_prof.setMaximumSize(QtCore.QSize(145, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.Log_out_but_prof.setFont(font)
        self.Log_out_but_prof.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
                        "font: 12pt \"MS Shell Dlg 2\";\n"
                        "min-width:131px;\n"
                        "max-width:131px;\n"
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
        self.Log_out_but_prof.setObjectName("Log_out_but_prof")
        self.Log_out_but_prof.setText("Log out")
        self.Log_out_but_prof.clicked.connect(self.log_out)


#add to layout
        self.Prof_logo_lay.addWidget(self.Log_out_but_prof, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Prof_logo_lay.addItem(spacerItem5, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.Prof_logo_lay, 4, 0, 2, 2)
        self.horizontalLayout_3.addLayout(self.gridLayout)

#add U_profile_tab to TabWidget
        self.tabWidget.addTab(self.U_profile_tab, "")


#User performance tab
        self.U_Performance = QtWidgets.QWidget()
        self.U_Performance.setObjectName("U_Performance")

#layouts
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.U_Performance)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.U_perf_lay = QtWidgets.QGridLayout()
        self.U_perf_lay.setObjectName("U_perf_lay")

#edit for finding all information about solar panels group
        self.Search_ed_perf = QtWidgets.QLineEdit(self.U_Performance)
        self.Search_ed_perf.setMinimumSize(QtCore.QSize(150, 41))
        self.Search_ed_perf.setMaximumSize(QtCore.QSize(220, 41))

#colors
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(166, 166, 166))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(166, 166, 166))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(166, 166, 166))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(166, 166, 166))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(166, 166, 166))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(166, 166, 166))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(166, 166, 166))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(166, 166, 166))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.3, -0.4, 1.35, 0.3, -0.4)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(166, 166, 166))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)

#set style sheet for searching edit
        self.Search_ed_perf.setPalette(palette)
        self.Search_ed_perf.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
                        "font: 12pt \"MS Shell Dlg 2\";\n"
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
        self.Search_ed_perf.setObjectName("Search_ed_perf")

#add to layout
        self.U_perf_lay.addWidget(self.Search_ed_perf, 1, 1, 1, 1)

#listView for support data(Performance)
        self.Support_data_cap = QtWidgets.QListView(self.U_Performance)
        self.Support_data_cap.setMinimumSize(QtCore.QSize(250, 135))
        self.Support_data_cap.setMaximumSize(QtCore.QSize(250, 135))
        self.Support_data_cap.setStyleSheet("background-color: rgb(168, 168, 168);\n""")
        self.Support_data_cap.setObjectName("Support_data_cap")

#add to layout
        self.U_perf_lay.addWidget(self.Support_data_cap, 3, 4, 1, 1)

#Table widget for all information about solar panels group
        self.Objects_info_cap = QtWidgets.QTableWidget(self.U_Performance)
        self.Objects_info_cap.setMinimumSize(QtCore.QSize(1115, 421))
        self.Objects_info_cap.setMaximumSize(QtCore.QSize(1115, 421))
        self.Objects_info_cap.setStyleSheet("background-color: rgb(168, 168, 168);")
        self.Objects_info_cap.setColumnCount(5)
        self.Objects_info_cap.setObjectName("Objects_info_cap")
        self.Objects_info_cap.setRowCount(0)
#add to layout
        self.U_perf_lay.addWidget(self.Objects_info_cap, 0, 1, 1, 1)

#button for finding all information about solar panels group
        self.Search_but_perf = QtWidgets.QPushButton(self.U_Performance)
        self.Search_but_perf.setMinimumSize(QtCore.QSize(150, 41))
        self.Search_but_perf.setMaximumSize(QtCore.QSize(131, 41))
        self.Search_but_perf.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
                        "font: 12pt \"MS Shell Dlg 2\";\n"
                        "min-width: 8em;\n"
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
        self.Search_but_perf.setObjectName("Search_but_perf")
        self.Search_but_perf.setText("Search")

#add to layout
        self.U_perf_lay.addWidget(self.Search_but_perf, 1, 4, 1, 1)

#layouts
        self.Perf_logo_lay = QtWidgets.QGridLayout()
        self.Perf_logo_lay.setObjectName("Perf_logo_lay")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Perf_logo_lay.addItem(spacerItem6, 1, 1, 1, 1)

#logout button(performance)
        self.Log_out_but_perf = QtWidgets.QPushButton(self.U_Performance)
        self.Log_out_but_perf.setMinimumSize(QtCore.QSize(145, 41))
        self.Log_out_but_perf.setMaximumSize(QtCore.QSize(145, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.Log_out_but_perf.setFont(font)
        self.Log_out_but_perf.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
                        "font: 12pt \"MS Shell Dlg 2\";\n"
                        "min-width:131px;\n"
                        "max-width:131px;\n"
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
        self.Log_out_but_perf.setObjectName("Log_out_but_perf")
        self.Log_out_but_perf.setText("Log out")
        self.Log_out_but_perf.clicked.connect(self.log_out)

#logo and layouts
        self.Perf_logo_lay.addWidget(self.Log_out_but_perf, 3, 1, 1, 1)
        self.Logo_perf = QtWidgets.QLabel(self.U_Performance)
        self.Logo_perf.setMinimumSize(QtCore.QSize(82, 45))
        self.Logo_perf.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                        "image: url(:/newPrefix/images/backgrounds/PsLYIQ01.svg);")
        self.Logo_perf.setObjectName("Logo_perf")
        self.Logo_perf.setText("<html><head/><body><p align=\"center\"><br/></p></body></html>")

        self.Perf_logo_lay.addWidget(self.Logo_perf, 3, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Perf_logo_lay.addItem(spacerItem7, 2, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Perf_logo_lay.addItem(spacerItem8, 1, 2, 1, 1)


#layout for performance
        self.U_perf_lay.addLayout(self.Perf_logo_lay, 2, 0, 2, 2)
        self.horizontalLayout_4.addLayout(self.U_perf_lay)

#add U_performance to Tab Widget
        self.tabWidget.addTab(self.U_Performance, "")

#Tab Widget about User chart 
        self.U_chart = QtWidgets.QWidget()
        self.U_chart.setObjectName("U_chart")
#layouts
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.U_chart)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
#button
        self.pushButton = QtWidgets.QPushButton(self.U_chart)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Check chart")
        self.horizontalLayout_5.addWidget(self.pushButton)
#add tab to tab widget
        self.tabWidget.addTab(self.U_chart, "")


#user settings widget
        self.U_settings = QtWidgets.QWidget()
        self.U_settings.setObjectName("U_settings")

#layouts
        self.gridLayout_3 = QtWidgets.QGridLayout(self.U_settings)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

#logo lable
        self.Logo_set = QtWidgets.QLabel(self.U_settings)
        self.Logo_set.setMinimumSize(QtCore.QSize(82, 45))
        self.Logo_set.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                        "image: url(:/newPrefix/images/backgrounds/PsLYIQ01.svg);\n""")
        self.Logo_set.setObjectName("Logo_set")
        self.Logo_set.setText("<html><head/><body><p align=\"center\"><br/></p></body></html>")
#add to layout        
        self.gridLayout_2.addWidget(self.Logo_set, 8, 0, 1, 1)

#logout button(settings)
        self.Log_out_but_set = QtWidgets.QPushButton(self.U_settings)
        self.Log_out_but_set.setMinimumSize(QtCore.QSize(0, 41))
        self.Log_out_but_set.setMaximumSize(QtCore.QSize(145, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.Log_out_but_set.setFont(font)
        self.Log_out_but_set.setStyleSheet("QPushButton {\n"
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
        self.Log_out_but_set.setObjectName("Log_out_but_set")
        self.Log_out_but_set.setText("Log out")
        self.Log_out_but_set.clicked.connect(self.log_out)
#add to layout
        self.gridLayout_2.addWidget(self.Log_out_but_set, 8, 1, 1, 1)

#change photo button
        self.Ch_photo_but = QtWidgets.QPushButton(self.U_settings)
        self.Ch_photo_but.setMinimumSize(QtCore.QSize(145, 41))
        self.Ch_photo_but.setMaximumSize(QtCore.QSize(145, 41))
        self.Ch_photo_but.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
                        "font: 12pt \"MS Shell Dlg 2\";\n"
                        "min-width: 131px;\n"
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
        self.Ch_photo_but.setObjectName("Ch_photo_but")
        self.Ch_photo_but.setText("Change")
#add to layout
        self.gridLayout_2.addWidget(self.Ch_photo_but, 0, 2, 1, 1)

#change login button
        self.Ch_log_but = QtWidgets.QPushButton(self.U_settings)
        self.Ch_log_but.setMinimumSize(QtCore.QSize(145, 41))
        self.Ch_log_but.setMaximumSize(QtCore.QSize(145, 41))
        self.Ch_log_but.setStyleSheet("QPushButton {\n"
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
        self.Ch_log_but.setObjectName("Ch_log_but")
        self.Ch_log_but.setText("Change Login")
#add to layout
        self.gridLayout_2.addWidget(self.Ch_log_but, 3, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem9, 2, 1, 1, 1)

#Username label(settings)
        self.U_name_set = QtWidgets.QLabel(self.U_settings)
        self.U_name_set.setMinimumSize(QtCore.QSize(147, 41))
        self.U_name_set.setStyleSheet("background-color: rgba(255, 255, 255, 10);")
        self.U_name_set.setObjectName("U_name_set")
        self.U_name_set.setText("<html><head/><body><p align=\"center\">Name</p></body></html>")
#add to layout
        self.gridLayout_2.addWidget(self.U_name_set, 1, 0, 1, 2)

#change name button
        self.Ch_name_but = QtWidgets.QPushButton(self.U_settings)
        self.Ch_name_but.setMinimumSize(QtCore.QSize(145, 41))
        self.Ch_name_but.setMaximumSize(QtCore.QSize(145, 41))
        self.Ch_name_but.setStyleSheet("QPushButton {\n"
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
        self.Ch_name_but.setObjectName("Ch_name_but")
        self.Ch_name_but.setText("Change")
#add to layout
        self.gridLayout_2.addWidget(self.Ch_name_but, 1, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem10, 4, 1, 1, 1)

#change password button
        self.Ch_pass_butt = QtWidgets.QPushButton(self.U_settings)
        self.Ch_pass_butt.setMinimumSize(QtCore.QSize(145, 41))
        self.Ch_pass_butt.setMaximumSize(QtCore.QSize(145, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.Ch_pass_butt.setFont(font)
        self.Ch_pass_butt.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
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
        self.Ch_pass_butt.setObjectName("Ch_pass_butt")
        self.Ch_pass_butt.setText("Change Password")
#add to layout
        self.gridLayout_2.addWidget(self.Ch_pass_butt, 5, 1, 1, 3)

#label for user photo(settings)
        self.U_photo_set = QtWidgets.QLabel(self.U_settings)
        self.U_photo_set.setMinimumSize(QtCore.QSize(169, 169))
        self.U_photo_set.setMaximumSize(QtCore.QSize(169, 169))
        self.U_photo_set.setStyleSheet("border: 3px solid black;\n"
                        "border-radius: 80px;\n"
                        "background-color: rgba(255, 255, 255, 10);")
        self.U_photo_set.setObjectName("U_photo_set")
        self.U_photo_set.setText("<html><head/><body><p align=\"center\">Photo</p></body></html>")
#add to layout
        self.gridLayout_2.addWidget(self.U_photo_set, 0, 0, 1, 2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem11, 6, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 3, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem12)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem13)

#label for add new panels(user info)
        self.add_pan_us_lab = QtWidgets.QLabel(self.U_settings)
        self.add_pan_us_lab.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.add_pan_us_lab.setObjectName("add_pan_lab")
        self.add_pan_us_lab.setToolTip("<html><head/><body><p><br/></p></body></html>")
        self.add_pan_us_lab.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#f5f5dc;\">User data</span></p></body></html>")
#add to layout
        self.verticalLayout_2.addWidget(self.add_pan_us_lab)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem14)

#name edit for add new panels
        self.U_name_add_panels = QtWidgets.QLineEdit(self.U_settings)
        self.U_name_add_panels.setMinimumSize(QtCore.QSize(234, 41))
        self.U_name_add_panels.setMaximumSize(QtCore.QSize(220, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.U_name_add_panels.setFont(font)
        self.U_name_add_panels.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
                        "font: 12pt \"MS Shell Dlg 2\";\n"
                        "min-width: 220px;\n"
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
        self.U_name_add_panels.setInputMask("")
        self.U_name_add_panels.setText("")
        self.U_name_add_panels.setObjectName("U_name_add_panels")
        self.U_name_add_panels.setWhatsThis("Name")
        self.U_name_add_panels.setPlaceholderText("Name")
#add to layout
        self.verticalLayout_2.addWidget(self.U_name_add_panels, 0, QtCore.Qt.AlignHCenter)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem15)

#email edit for add new panels
        self.U_email_add_panels = QtWidgets.QLineEdit(self.U_settings)
        self.U_email_add_panels.setMinimumSize(QtCore.QSize(234, 41))
        self.U_email_add_panels.setMaximumSize(QtCore.QSize(220, 41))
        self.U_email_add_panels.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
                        "font: 12pt \"MS Shell Dlg 2\";\n"
                        "min-width: 220px;\n"
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
        self.U_email_add_panels.setInputMask("")
        self.U_email_add_panels.setText("")
        self.U_email_add_panels.setObjectName("U_email_add_panels")
        self.U_email_add_panels.setWhatsThis("Email")
        self.U_email_add_panels.setPlaceholderText("E-mail")
#add to layout
        self.verticalLayout_2.addWidget(self.U_email_add_panels, 0, QtCore.Qt.AlignHCenter)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem16)

#user password edit for add new panels
        self.U_pass_add_panels = QtWidgets.QLineEdit(self.U_settings)
        self.U_pass_add_panels.setMinimumSize(QtCore.QSize(234, 41))
        self.U_pass_add_panels.setMaximumSize(QtCore.QSize(220, 41))
        self.U_pass_add_panels.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
                        "font: 12pt \"MS Shell Dlg 2\";\n"
                        "min-width: 220px;\n"
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
        self.U_pass_add_panels.setInputMask("")
        self.U_pass_add_panels.setText("")
        self.U_pass_add_panels.setObjectName("U_pass_add_panels")
        self.U_pass_add_panels.setWhatsThis("Password")
        self.U_pass_add_panels.setPlaceholderText("Password")
#add to layout
        self.verticalLayout_2.addWidget(self.U_pass_add_panels, 0, QtCore.Qt.AlignHCenter)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem17)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem18)

#button add panels
        self.U_add_panels_but = QtWidgets.QPushButton(self.U_settings)
        self.U_add_panels_but.setMinimumSize(QtCore.QSize(145, 41))
        self.U_add_panels_but.setMaximumSize(QtCore.QSize(145, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.U_add_panels_but.setFont(font)
        self.U_add_panels_but.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
                        "font: 12pt \"MS Shell Dlg 2\";\n"
                        "min-width:131px;\n"
                        "max-width:131px;\n"
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
        self.U_add_panels_but.setObjectName("U_add_panels_but")
        self.U_add_panels_but.setText("Add Panels")
#add to layout
        self.verticalLayout_2.addWidget(self.U_add_panels_but, 0, QtCore.Qt.AlignHCenter)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem19)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 1, 2, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem20)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem21)

#labels for add panels label(panels data)
        self.add_pan_dat_lab = QtWidgets.QLabel(self.U_settings)
        self.add_pan_dat_lab.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.add_pan_dat_lab.setObjectName("add_pan_dat_lab")
        self.add_pan_dat_lab.setToolTip("<html><head/><body><p><br/></p></body></html>")
        self.add_pan_dat_lab.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#f5f5dc;\">Panels data</span></p></body></html>")
#add to layout
        self.verticalLayout_4.addWidget(self.add_pan_dat_lab)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem22)

#new panels adress edit
        self.U_new_panels_adress = QtWidgets.QLineEdit(self.U_settings)
        self.U_new_panels_adress.setMinimumSize(QtCore.QSize(234, 41))
        self.U_new_panels_adress.setMaximumSize(QtCore.QSize(220, 41))
        self.U_new_panels_adress.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
                        "font: 12pt \"MS Shell Dlg 2\";\n"
                        "min-width: 220px;\n"
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
        self.U_new_panels_adress.setInputMask("")
        self.U_new_panels_adress.setText("")
        self.U_new_panels_adress.setObjectName("U_new_panels_adress")
        self.U_new_panels_adress.setWhatsThis("New Adress")
        self.U_new_panels_adress.setPlaceholderText("Adress")
#add to layout
        self.verticalLayout_4.addWidget(self.U_new_panels_adress, 0, QtCore.Qt.AlignHCenter)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem23)


        self.U_panels_amount = QtWidgets.QLineEdit(self.U_settings)
        self.U_panels_amount.setMinimumSize(QtCore.QSize(234, 41))
        self.U_panels_amount.setMaximumSize(QtCore.QSize(220, 41))
        self.U_panels_amount.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
                        "font: 12pt \"MS Shell Dlg 2\";\n"
                        "min-width: 220px;\n"
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
        self.U_panels_amount.setInputMask("")
        self.U_panels_amount.setText("")
        self.U_panels_amount.setObjectName("U_panels_amount")
        self.U_panels_amount.setWhatsThis("Amount")
        self.U_panels_amount.setPlaceholderText("Amount")
        self.verticalLayout_4.addWidget(self.U_panels_amount, 0, QtCore.Qt.AlignHCenter)
#add to layout
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem24)

#edit for panels group key
        self.U_panels_key = QtWidgets.QLineEdit(self.U_settings)
        self.U_panels_key.setMinimumSize(QtCore.QSize(234, 41))
        self.U_panels_key.setMaximumSize(QtCore.QSize(220, 41))
        self.U_panels_key.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
                        "font: 12pt \"MS Shell Dlg 2\";\n"
                        "min-width: 220px;\n"
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
        self.U_panels_key.setInputMask("")
        self.U_panels_key.setText("")
        self.U_panels_key.setObjectName("U_panels_key")
        self.U_panels_key.setWhatsThis("Key")
        self.U_panels_key.setPlaceholderText("Panels key")
#add to layout
        self.verticalLayout_4.addWidget(self.U_panels_key, 0, QtCore.Qt.AlignHCenter)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem25)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem26)

#button for clearing fields
        self.U_clear_panels_but = QtWidgets.QPushButton(self.U_settings)
        self.U_clear_panels_but.setMinimumSize(QtCore.QSize(145, 41))
        self.U_clear_panels_but.setMaximumSize(QtCore.QSize(145, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.U_clear_panels_but.setFont(font)
        self.U_clear_panels_but.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
                        "font: 12pt \"MS Shell Dlg 2\";\n"
                        "min-width:131px;\n"
                        "max-width:131px;\n"
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
        self.U_clear_panels_but.setObjectName("U_clear_panels_but")
        self.U_clear_panels_but.setText("Clear data")
#add to layout
        self.verticalLayout_4.addWidget(self.U_clear_panels_but, 0, QtCore.Qt.AlignHCenter)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem27)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 1, 3, 1, 1)

#add panels label
        self.add_pan_lab = QtWidgets.QLabel(self.U_settings)
        self.add_pan_lab.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.add_pan_lab.setObjectName("add_pan_lab")
        self.add_pan_lab.setToolTip("<html><head/><body><p><br/></p></body></html>")
        self.add_pan_lab.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#f5f5dc;\">Add Panels</span></p></body></html>")
#add to layout
        self.gridLayout_3.addWidget(self.add_pan_lab, 0, 2, 1, 1)
        self.tabWidget.addTab(self.U_settings, "")

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.U_profile_tab), "Profile")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.U_Performance), "Performance")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.U_chart), "Chart")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.U_settings), "Settings")

    def log_out(self):
        self.controller = control.Control()
        self.controller.show_login()
        self.close()
        
import Backgrounds
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    profile_window = ProfileWindow()
    profile_window.show()
    sys.exit(app.exec_())
