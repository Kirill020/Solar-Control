import folium
from PyQt5.QtCore import QUrl
from geopy.geocoders import Nominatim

from PyQt5.QtGui import QFontDatabase, QFont
from db_handler import SqliteDB
import control
from datetime import datetime, timedelta
from PyQt5 import QtCore, QtGui, QtWidgets, QtChart, QtWebEngineWidgets

class ProfileWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        logotype = QtGui.QIcon("C:\\Solar Control\\Solar-Control\\images\\backgrounds\\PsLYIQ01.svg")
        self.setWindowIcon(logotype)
        self.controller = control.ControlWindow()
        self.controllerAPI = control.ControlAPI()

        self.support_info = QtCore.QStringListModel()
        support_data = ["                 Support info:"," "," "," ", "  work.tanasiichuk@gmail.com"]
        self.support_info.setStringList(support_data)
        
        comfortaa_font_id = QFontDatabase.addApplicationFont("C:\\Solar Control\\Solar-Control\\fonts\\Comfortaa-Bold.ttf")
        opensans_font_id = QFontDatabase.addApplicationFont("C:\\Solar Control\\Solar-Control\\fonts\\OpenSans-SemiBold.ttf")
        if comfortaa_font_id != -1 and opensans_font_id != -1:
            comfortaa_font_fam = QFontDatabase.applicationFontFamilies(comfortaa_font_id)
            opensans_font_fam = QFontDatabase.applicationFontFamilies(opensans_font_id)
            if comfortaa_font_fam and opensans_font_fam:
                self.comfortaa_font = comfortaa_font_fam[0]
                self.opensans_font = opensans_font_fam[0]
                self.tab_widget_font = QFont(self.comfortaa_font, 10)
                self.button_font = QFont(self.comfortaa_font, 11)
                self.button_font_2 = QFont(self.comfortaa_font, 10)

                self.edit_font = QFont(self.comfortaa_font, 10)
                self.label_font = QFont(self.opensans_font, 13)
                self.support = QFont(self.opensans_font, 12)
                self.label_font_2 = QFont(self.opensans_font, 19)

                self.table_widget_font = QFont(self.comfortaa_font, 10)



        self.setWindowTitle("SOLAR CONTROL")
        self.resize(1180, 727)
        self.setMinimumSize(QtCore.QSize(1180, 727))
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.482198, y1:0.971, x2:0.497, y2:0.023, stop:0.0338983 rgba(46, 46, 46, 255), stop:1 rgba(168, 168, 168, 255));")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(self.horizontalLayout)
        self.setCentralWidget(central_widget)

#create  Tab Widget
        self.tabWidget = QtWidgets.QTabWidget(central_widget)
        self.tabWidget.setGeometry(QtCore.QRect(9, 9, 1162, 709))
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-style: outset;\n"
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
        self.tabWidget.setFont(self.tab_widget_font)
        self.horizontalLayout.addWidget(self.tabWidget)


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
        self.Support_data_prof.setFont(self.support)

        self.Support_data_prof.setModel(self.support_info)

        self.Check_lay_prof.addWidget(self.Support_data_prof, 2, 2, 1, 1)


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
        self.Search_ed_prof.setPlaceholderText("№")
        self.Search_ed_prof.setFont(self.edit_font)
        
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
        self.Search_but_prof.clicked.connect(self.find_data_prof)
        self.Search_but_prof.setFont(self.button_font)

#add to layout
        self.Check_lay_prof.addWidget(self.Search_but_prof, 1, 2, 1, 1)


#Label for username(profile)
        self.gridLayout.addLayout(self.Check_lay_prof, 4, 2, 1, 1)
        self.U_name_prof = QtWidgets.QLabel(self.U_profile_tab)
        self.U_name_prof.setMinimumSize(QtCore.QSize(250, 41))
        self.U_name_prof.setText(f"<html><head/><body><p align=\"center\">{self.controller.session_name}</p></body></html>")
        self.U_name_prof.setFont(self.label_font)



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
        self.U_name_prof.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.U_name_prof.setObjectName("U_name_prof")
        

#Table Widget for main information about solar panel`s group
        self.Objects_info_prof = QtWidgets.QTableWidget(self.U_profile_tab)
        self.Objects_info_prof.setMinimumSize(QtCore.QSize(835, 391))
        self.Objects_info_prof.setMaximumSize(QtCore.QSize(1234, 391))
        self.Objects_info_prof.setStyleSheet("background-color: rgb(168, 168, 168);\n""")
        self.Objects_info_prof.setColumnCount(5)
        self.Objects_info_prof.setObjectName("Objects_info_prof")
        self.Objects_info_prof.setFont(self.table_widget_font)
        self.Objects_info_prof.setHorizontalHeaderLabels(["№", "Amount", "Panel`s adress", "Performance", "Weather"])

        data = SqliteDB.get_panel_group_data(self.controller.session_id, None, None)
        
        weather_data = []
        
        for row in range(len(data)):    
            weather_data.extend(SqliteDB.get_weather(data[row][0], data[row][6]))
            



        self.Objects_info_prof.setRowCount(len(data))
        for row in range(len(data)):
            for col in range(5):
                if col == 4:
                    item = QtWidgets.QTableWidgetItem(str(weather_data[row][1]))
                else:
                    item = QtWidgets.QTableWidgetItem(str(data[row][col]))
                self.Objects_info_prof.setItem(row, col, item)


        self.Objects_info_prof.horizontalHeader().setFont(self.table_widget_font)
        self.Objects_info_prof.setColumnWidth(0, 30)
        self.Objects_info_prof.setColumnWidth(1, 67)
        self.Objects_info_prof.setColumnWidth(4, 120)
        self.Objects_info_prof.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        self.Objects_info_prof.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        self.Objects_info_prof.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.Objects_info_prof.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.Objects_info_prof.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Fixed)
        
        header = self.Objects_info_prof.verticalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        
#add to layout
        self.gridLayout.addWidget(self.Objects_info_prof, 1, 2, 1, 1)


#update data button (profile)
        self.update_but_prof = QtWidgets.QPushButton(self.U_profile_tab)
        self.update_but_prof.setMinimumSize(QtCore.QSize(30, 30))
        self.update_but_prof.setMaximumSize(QtCore.QSize(30, 30))
        self.update_but_prof.setStyleSheet("QPushButton {\n"
                        "alignment: right;\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
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
        self.update_but_prof.setObjectName("update_but_prof")
        self.update_but_prof.setFont(self.button_font)
        self.update_but_prof.setText("↻")
        self.update_but_prof.clicked.connect(self.update_data_prof)
        self.Check_lay_prof.addWidget(self.update_but_prof, 1, 1, 1, 1)




#layout for user photo(profile)
        self.Photo_lay_prof = QtWidgets.QGridLayout()
        self.Photo_lay_prof.setObjectName("Photo_lay_prof")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Photo_lay_prof.addItem(spacerItem1, 0, 2, 1, 1)

#label for user photo(profile)
        self.U_photo_prof = QtWidgets.QLabel(self.U_profile_tab)
        self.U_photo_prof.setMinimumSize(QtCore.QSize(169, 169))
        self.U_photo_prof.setMaximumSize(QtCore.QSize(169, 169))
        self.U_photo_prof.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.U_photo_prof.setObjectName("U_photo_prof")
        self.U_photo_prof.setPixmap(self.set_avatar(self.controller.session_binary_avatar))
        self.U_photo_prof.repaint()
#add to layout
        self.Photo_lay_prof.addWidget(self.U_photo_prof, 0, 0, 2, 2, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Photo_lay_prof.addItem(spacerItem2, 3, 0, 1, 1)
        self.gridLayout.addLayout(self.Photo_lay_prof, 0, 0, 3, 2)
        self.Photo_lay_prof.addWidget(self.U_name_prof, 2, 1, 1, 1)


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
        self.Log_out_but_prof.setFont(self.button_font)
        self.Log_out_but_prof.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
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
        self.Search_ed_perf.setFont(self.edit_font)
        self.Search_ed_perf.setPlaceholderText("yyyy-mm-dd or №")


#add to layout
        self.U_perf_lay.addWidget(self.Search_ed_perf, 1, 0, 1, 1)

#listView for support data(Performance)
        self.Support_data_cap = QtWidgets.QListView(self.U_Performance)
        self.Support_data_cap.setMinimumSize(QtCore.QSize(250, 135))
        self.Support_data_cap.setMaximumSize(QtCore.QSize(250, 135))
        self.Support_data_cap.setStyleSheet("background-color: rgb(168, 168, 168);\n""")
        self.Support_data_cap.setObjectName("Support_data_cap")
        self.Support_data_cap.setFont(self.support)

        self.Support_data_cap.setModel(self.support_info)

#add to layout
        self.U_perf_lay.addWidget(self.Support_data_cap, 2, 4, 1, 1)

#Table widget for all information about solar panels group
        self.Objects_info_cap = QtWidgets.QTableWidget(self.U_Performance)
        self.Objects_info_cap.setMinimumSize(QtCore.QSize(1115, 421))
        self.Objects_info_cap.setMaximumSize(QtCore.QSize(12345, 421))
        self.Objects_info_cap.setStyleSheet("background-color: rgb(168, 168, 168);")
        self.Objects_info_cap.setColumnCount(10)
        self.Objects_info_cap.setFont(self.tab_widget_font)
        self.Objects_info_cap.setObjectName("Objects_info_cap")
        self.Objects_info_cap.setHorizontalHeaderLabels(["№", "Amount", "Panel`s adress", "Performance", "Voltage", "Power", "Date", "Weather", "°C", "Wind speed"])

        
        panels_data = SqliteDB.get_panel_group_data(self.controller.session_id, None, None)
        weather_data = []
        
        for row in range(len(panels_data)):
            weather_data.extend(SqliteDB.get_weather(panels_data[row][0], panels_data[row][6]))
            
        
        self.Objects_info_cap.setRowCount(len(panels_data))
        for row in range(len(panels_data)):
            for col in range(len(panels_data[row])+3):
                if col == 7:
                    item = QtWidgets.QTableWidgetItem(str(weather_data[row][1]))
                elif col == 8:
                    item = QtWidgets.QTableWidgetItem(str(weather_data[row][3]))
                elif col == 9:
                    item = QtWidgets.QTableWidgetItem(str(weather_data[row][4]))
                else:
                    item = QtWidgets.QTableWidgetItem(str(panels_data[row][col]))

                self.Objects_info_cap.setItem(row, col, item)

        self.Objects_info_cap.horizontalHeader().setFont(self.tab_widget_font)
        self.Objects_info_cap.setColumnWidth(0, 20)
        self.Objects_info_cap.setColumnWidth(1, 67)
        self.Objects_info_cap.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        self.Objects_info_cap.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)

        header = self.Objects_info_cap.verticalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        self.Objects_info_cap.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.Objects_info_cap.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.Objects_info_cap.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.Objects_info_cap.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.Objects_info_cap.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        self.Objects_info_cap.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        self.Objects_info_cap.setColumnWidth(8, 40)
        self.Objects_info_cap.horizontalHeader().setSectionResizeMode(8, QtWidgets.QHeaderView.Fixed)
        self.Objects_info_cap.horizontalHeader().setSectionResizeMode(9, QtWidgets.QHeaderView.Stretch)
        
#add to layout
        self.U_perf_lay.addWidget(self.Objects_info_cap, 0, 0, 1, 5)

#button for finding all information about solar panels group
        self.Search_but_perf = QtWidgets.QPushButton(self.U_Performance)
        self.Search_but_perf.setMinimumSize(QtCore.QSize(150, 41))
        self.Search_but_perf.setMaximumSize(QtCore.QSize(131, 41))
        self.Search_but_perf.setStyleSheet("QPushButton {\n"
                        "alignment: right;\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
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
        self.Search_but_perf.setFont(self.button_font)
        self.Search_but_perf.setText("Search")
        self.Search_but_perf.clicked.connect(self.find_data_perf)

#add to layout
        self.U_perf_lay.addWidget(self.Search_but_perf, 1, 4, 1, 1)


#update button
        self.update_but_perf = QtWidgets.QPushButton(self.U_Performance)
        self.update_but_perf.setMinimumSize(QtCore.QSize(30, 30))
        self.update_but_perf.setMaximumSize(QtCore.QSize(30, 30))
        self.update_but_perf.setStyleSheet("QPushButton {\n"
                        "alignment: left;\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
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
        self.update_but_perf.setObjectName("update_but_perf")
        self.update_but_perf.setText("↻")
        self.update_but_perf.setFont(self.button_font)
        self.update_but_perf.clicked.connect(self.update_data_perf)
        self.U_perf_lay.addWidget(self.update_but_perf, 1, 3, 1, 1)



#layouts
        self.Perf_logo_lay = QtWidgets.QGridLayout()
        self.Perf_logo_lay.setObjectName("Perf_logo_lay")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Perf_logo_lay.addItem(spacerItem6, 1, 1, 1, 1)

#logout button(performance)
        self.Log_out_but_perf = QtWidgets.QPushButton(self.U_Performance)
        self.Log_out_but_perf.setMinimumSize(QtCore.QSize(145, 41))
        self.Log_out_but_perf.setMaximumSize(QtCore.QSize(145, 41))
        self.Log_out_but_perf.setFont(self.button_font)
        self.Log_out_but_perf.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
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



#-------------------------------------------------------------------------------
#Tab Widget about User chart 
        self.U_chart = QtWidgets.QWidget()
        self.U_chart.setObjectName("U_chart")
#layouts
        self.u_chart_lay = QtWidgets.QHBoxLayout(self.U_chart)
        self.gridLayout_5 = QtWidgets.QGridLayout() 
        self.gridLayout_5.setObjectName("gridLayout_5")


        base_group = SqliteDB.get_panel_group_data(self.controller.session_id, None, None)[0][0]

        #edit for finding all information about solar panels group
        self.Search_ed_chart = QtWidgets.QLineEdit(self.U_chart)
        self.Search_ed_chart.setMinimumSize(QtCore.QSize(90, 41))
        self.Search_ed_chart.setMaximumSize(QtCore.QSize(90, 41))
        self.Search_ed_chart.setPalette(palette)
        self.Search_ed_chart.setStyleSheet("QLineEdit {\n"
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
        self.Search_ed_chart.setObjectName("Search_ed_chart")
        self.Search_ed_chart.setFont(self.edit_font)
        self.Search_ed_chart.setPlaceholderText("№")

#chart

        self.group_id = self.Search_ed_chart.text()
        self.chart = QtChart.QChart()
        self.series = QtChart.QLineSeries()
        self.chart.addSeries(self.series)
        
        self.chart.setTitle("Panels performance for all time")

        self.axisX = QtChart.QDateTimeAxis()
        self.axisX.setTitleText("Time") 

        self.chart.addAxis(self.axisX, QtCore.Qt.AlignBottom)
        self.series.attachAxis(self.axisX)

        self.axisY = QtChart.QValueAxis()
        self.axisY.setLabelFormat("%f")
        self.axisY.setTitleText("Performance")
        self.axisY.setTickCount(10)
        self.chart.addAxis(self.axisY, QtCore.Qt.AlignLeft)
        self.series.attachAxis(self.axisY)
        
        now_axis = datetime.now()
        data = SqliteDB.get_panel_group_data(self.controller.session_id,base_group,None)
        
        oldest_row = min(data, key=lambda x: datetime.strptime(x[-1], '%Y-%m-%d-%H'))
        oldest_date = datetime.strptime(oldest_row[-1], '%Y-%m-%d-%H')
        date_difference = now_axis - oldest_date
        days_difference = date_difference.days
        
        if days_difference >= 1:
            self.axisX.setTickCount(days_difference)
            self.axisX.setFormat("yyyy/MM/dd")  
            self.axisX.setRange(oldest_date, now_axis)  
        else:
            self.axisX.setTickCount(24)  
            self.axisX.setFormat("HH")  
            self.axisX.setRange(oldest_date, now_axis)  


        now = QtCore.QDateTime.currentDateTime()
        start_time = now.addSecs(-(days_difference*24) * 3600)
        self.series.clear()  
        self.chart.removeSeries(self.series)  
        #get data for axis_y
        max_y = 0
        for i in range((days_difference * 24)+1):
            
            hour_ago = start_time.addSecs(i * 3600)
            data_row = SqliteDB.get_panel_group_data(self.controller.session_id, base_group, hour_ago.toPyDateTime().strftime('%Y-%m-%d-%H'))
            performance = 0
            if data_row is not None:
                data = []
                data.extend(data_row)
                for row in data:
                    performance = float(row[3])
                    max_y = max(max_y, performance)
            else:
                performance = float(0)
            self.series.append(hour_ago.toMSecsSinceEpoch(), performance)
        
        self.axisY.setRange(0, max_y)  

        self.chart.addSeries(self.series)
        

        
        self.chartView = QtChart.QChartView(self.chart)
        self.chartView.setRenderHint(QtGui.QPainter.Antialiasing)
        self.chartView.setMinimumSize(QtCore.QSize(750, 625))



        self.chart_time_combobox = QtWidgets.QComboBox(self.U_chart)
        self.chart_time_combobox.addItem("Last 24 hours")
        self.chart_time_combobox.addItem("Last 30 days")
        self.chart_time_combobox.addItem("All the time")
        self.chart_time_combobox.setStyleSheet("QComboBox {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: outset;\n"
                        "min-width: 8em;\n"
                        "background: qradialgradient(\n"
                        "    cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                        "    radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                        ");\n"
                        "padding: 5px;\n"
                        "}\n"
                        "\n"
                        "QComboBox:hover {\n"
                        "    background: qradialgradient(\n"
                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                        "    );\n"
                        "}\n"
                        "\n"
                        "QComboBox:pressed {\n"
                        "    border-style: inset;\n"
                        "    background: qradialgradient(\n"
                        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                        "    );\n"
                        "}\n"
                        "\n"
                        "QComboBox QAbstractItemView {\n"
                        "    background-color: #fff;\n"
                        "    border: 2px solid #555;\n"
                        "    selection-background-color: #bbb;\n"
                        "    outline: none;\n"
                        "}")

        self.chart_time_combobox.setFont(self.label_font)
        self.chart_time_combobox.setCurrentIndex(2)

        self.check_chart_but = QtWidgets.QPushButton(self.U_chart)
        self.check_chart_but.setMinimumSize(QtCore.QSize(90, 41))
        self.check_chart_but.setMaximumSize(QtCore.QSize(90, 41))
        self.check_chart_but.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
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
        self.check_chart_but.setObjectName("check_chart_but")
        self.check_chart_but.setText("Check")
        self.check_chart_but.setFont(self.button_font)
        self.check_chart_but.clicked.connect(self.chart_time_change)

        

        
        
        self.gridLayout_5.addWidget(self.chartView, 0, 0, 3, 1)
        self.gridLayout_5.addWidget(self.Search_ed_chart, 0, 2, 1, 1)
        self.gridLayout_5.addWidget(self.chart_time_combobox, 1, 2, 1, 1)
        self.gridLayout_5.addWidget(self.check_chart_but, 2, 2, 1, 1)
        self.u_chart_lay.addLayout(self.gridLayout_5)
        
        
        

#add tab to tab widget
        self.tabWidget.addTab(self.U_chart, "")
#-------------------------------------------------------------------------------

        self.U_panels_map = QtWidgets.QWidget()
        self.U_panels_map.setObjectName("U_panels_map")
#layouts
        self.u_map_lay = QtWidgets.QVBoxLayout(self.U_panels_map)

        m = folium.Map(location=[0, 0], zoom_start=2)
        geolocator = Nominatim(user_agent="my_app")
        

        addresses = []
        data = SqliteDB.get_panel_group_data(self.controller.session_id, None, None)
        
        if data is not None:
            existing_addresses = set(addresses)
            for row in data:
                group_number = row[0]
                panel_count = row[1]
                address = row[2]
                
                if address not in existing_addresses:
                    addresses.append(address)
                    existing_addresses.add(address)
                
                    location = geolocator.geocode(address)
                    if location is not None:
                        popup_text = f"Address: {address}<br>Group Number: {group_number}<br>Panel Count: {panel_count}"
                        folium.Marker([location.latitude, location.longitude], popup=popup_text).add_to(m)





        map_file = "C:\Solar Control\Solar-Control\map.html"
        m.save(map_file)


        self.webview = QtWebEngineWidgets.QWebEngineView(self)
        self.webview.load(QUrl.fromLocalFile(map_file)) 
        self.u_map_lay.addWidget(self.webview)

        self.tabWidget.addTab(self.U_panels_map, "")
#-------------------------------------------------------------------------------

#user settings widget
        self.U_settings = QtWidgets.QWidget()
        self.U_settings.setObjectName("U_settings")

#layouts
        self.gridLayout_3 = QtWidgets.QGridLayout(self.U_settings)
        self.gridLayout_3.setObjectName("gridLayout_3")



        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)

#labels for add panels label(panels data)
        self.add_pan_dat_lab = QtWidgets.QLabel(self.U_settings)
        self.add_pan_dat_lab.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.add_pan_dat_lab.setObjectName("add_pan_dat_lab")
        self.add_pan_dat_lab.setFont(self.label_font)
        self.add_pan_dat_lab.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#f5f5dc;\">Panels data</span></p></body></html>")


        self.verticalLayout_4.addWidget(self.add_pan_dat_lab)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)

#new panels adress edit
        self.U_new_panels_adress = QtWidgets.QLineEdit(self.U_settings)
        self.U_new_panels_adress.setMinimumSize(QtCore.QSize(234, 41))
        self.U_new_panels_adress.setMaximumSize(QtCore.QSize(220, 41))
        self.U_new_panels_adress.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
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
        self.U_new_panels_adress.setFont(self.button_font)
        self.U_new_panels_adress.setObjectName("U_new_panels_adress")
        self.U_new_panels_adress.setWhatsThis("New Adress")
        self.U_new_panels_adress.setPlaceholderText("Adress")

        self.verticalLayout_4.addWidget(self.U_new_panels_adress, 0, QtCore.Qt.AlignHCenter)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)



#U_settings add panels - new panels amount
        self.U_panels_amount = QtWidgets.QLineEdit(self.U_settings)
        self.U_panels_amount.setMinimumSize(QtCore.QSize(234, 41))
        self.U_panels_amount.setMaximumSize(QtCore.QSize(220, 41))
        self.U_panels_amount.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
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
        self.U_panels_amount.setFont(self.edit_font)
        self.U_panels_amount.setObjectName("U_panels_amount")
        self.U_panels_amount.setWhatsThis("Amount")
        self.U_panels_amount.setPlaceholderText("Amount")


        self.verticalLayout_4.addWidget(self.U_panels_amount, 0, QtCore.Qt.AlignHCenter)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)


#edit for panels group key
        self.U_panels_key = QtWidgets.QLineEdit(self.U_settings)
        self.U_panels_key.setMinimumSize(QtCore.QSize(234, 41))
        self.U_panels_key.setMaximumSize(QtCore.QSize(220, 41))
        self.U_panels_key.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
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
        self.U_panels_key.setFont(self.edit_font)
        self.U_panels_key.setObjectName("U_panels_key")
        self.U_panels_key.setWhatsThis("Key")
        self.U_panels_key.setPlaceholderText("Panels key")


        self.verticalLayout_4.addWidget(self.U_panels_key, 0, QtCore.Qt.AlignHCenter)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem12)


#button for clearing fields
        self.U_clear_panels_but = QtWidgets.QPushButton(self.U_settings)
        self.U_clear_panels_but.setMinimumSize(QtCore.QSize(145, 41))
        self.U_clear_panels_but.setMaximumSize(QtCore.QSize(145, 41))
        self.U_clear_panels_but.setFont(self.button_font)
        self.U_clear_panels_but.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
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

        self.verticalLayout_4.addWidget(self.U_clear_panels_but, 0, QtCore.Qt.AlignHCenter)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem13)

        self.gridLayout_3.addLayout(self.verticalLayout_4, 1, 4, 1, 1)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem14)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem15)


#label for add new panels(user info)
        self.add_pan_us_lab = QtWidgets.QLabel(self.U_settings)
        self.add_pan_us_lab.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.add_pan_us_lab.setObjectName("add_pan_lab")
        self.add_pan_us_lab.setFont(self.label_font)
        self.add_pan_us_lab.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#f5f5dc;\">User data</span></p></body></html>")


        self.verticalLayout_2.addWidget(self.add_pan_us_lab)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem16)


#name edit for add new panels
        self.U_name_add_panels = QtWidgets.QLineEdit(self.U_settings)
        self.U_name_add_panels.setMinimumSize(QtCore.QSize(234, 41))
        self.U_name_add_panels.setMaximumSize(QtCore.QSize(220, 41))
        self.U_name_add_panels.setFont(self.edit_font)
        self.U_name_add_panels.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
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


        self.verticalLayout_2.addWidget(self.U_name_add_panels, 0, QtCore.Qt.AlignHCenter)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem17)


#email edit for add new panels
        self.U_email_add_panels = QtWidgets.QLineEdit(self.U_settings)
        self.U_email_add_panels.setMinimumSize(QtCore.QSize(234, 41))
        self.U_email_add_panels.setMaximumSize(QtCore.QSize(220, 41))
        self.U_email_add_panels.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
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
        self.U_email_add_panels.setFont(self.edit_font)
        self.U_email_add_panels.setObjectName("U_email_add_panels")
        self.U_email_add_panels.setWhatsThis("Email")
        self.U_email_add_panels.setPlaceholderText("E-mail")


        self.verticalLayout_2.addWidget(self.U_email_add_panels, 0, QtCore.Qt.AlignHCenter)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem18)


#user password edit for add new panels
        self.U_pass_add_panels = QtWidgets.QLineEdit(self.U_settings)
        self.U_pass_add_panels.setMinimumSize(QtCore.QSize(234, 41))
        self.U_pass_add_panels.setMaximumSize(QtCore.QSize(220, 41))
        self.U_pass_add_panels.setStyleSheet("QLineEdit {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 10px;\n"
                        "border-style: inset;\n"
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
        self.U_pass_add_panels.setFont(self.edit_font)
        self.U_pass_add_panels.setObjectName("U_pass_add_panels")
        self.U_pass_add_panels.setWhatsThis("Password")
        self.U_pass_add_panels.setPlaceholderText("Password")
        self.U_pass_add_panels.setEchoMode(QtWidgets.QLineEdit.Password)


        self.verticalLayout_2.addWidget(self.U_pass_add_panels, 0, QtCore.Qt.AlignHCenter)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem19)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem20)



#button add panels
        self.U_add_panels_but = QtWidgets.QPushButton(self.U_settings)
        self.U_add_panels_but.setMinimumSize(QtCore.QSize(145, 41))
        self.U_add_panels_but.setMaximumSize(QtCore.QSize(145, 41))
        self.U_add_panels_but.setFont(self.button_font)
        self.U_add_panels_but.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
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
        self.U_add_panels_but.clicked.connect(self.add_panels)


        self.verticalLayout_2.addWidget(self.U_add_panels_but, 0, QtCore.Qt.AlignHCenter)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem21)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 2, 3, 1)





#add panels label
        self.add_pan_lab = QtWidgets.QLabel(self.U_settings)
        self.add_pan_lab.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.add_pan_lab.setObjectName("add_pan_lab")
        self.add_pan_lab.setFont(self.label_font_2)
        self.add_pan_lab.setText("<html><head/><body><p align=\"center\"><span style=\" color:#f5f5dc;\">Add Panels</span></p></body></html>")


        self.gridLayout_3.addWidget(self.add_pan_lab, 0, 3, 1, 1)

        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")



#change photo button
        self.Ch_photo_but = QtWidgets.QPushButton(self.U_settings)
        self.Ch_photo_but.setMinimumSize(QtCore.QSize(145, 41))
        self.Ch_photo_but.setMaximumSize(QtCore.QSize(145, 41))
        self.Ch_photo_but.setStyleSheet("QPushButton {\n"
                        "color: #333;\n"
                        "border: 2px solid #555;\n"
                        "border-radius: 20px;\n"
                        "border-style: outset;\n"
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
        self.Ch_photo_but.setFont(self.button_font)
        self.Ch_photo_but.setText("Change")
        self.Ch_photo_but.clicked.connect(self.select_avatar)

        self.gridLayout_2.addWidget(self.Ch_photo_but, 1, 3, 1, 1)

#logo lable
        self.Logo_set = QtWidgets.QLabel(self.U_settings)
        self.Logo_set.setMinimumSize(QtCore.QSize(82, 45))
        self.Logo_set.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                        "image: url(:/newPrefix/images/backgrounds/PsLYIQ01.svg);\n""")
        self.Logo_set.setObjectName("Logo_set")
        self.Logo_set.setText("<html><head/><body><p align=\"center\"><br/></p></body></html>")
#add to layout        
        self.gridLayout_2.addWidget(self.Logo_set, 9, 1, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem22, 0, 1, 1, 1)


#Username label(settings)
        self.U_name_set = QtWidgets.QLabel(self.U_settings)
        self.U_name_set.setMinimumSize(QtCore.QSize(147, 41))
        self.U_name_set.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.U_name_set.setObjectName("U_name_set")
        self.U_name_set.setText(f"<html><head/><body><p align=\"center\">{self.controller.session_name}</p></body></html>")
        self.U_name_set.setFont(self.label_font)
#add to layout
        self.gridLayout_2.addWidget(self.U_name_set, 2, 1, 1, 2)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem23, 3, 2, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem24, 7, 2, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem25, 1, 0, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem26, 5, 2, 1, 1)



#label for user photo(settings)
        self.U_photo_set = QtWidgets.QLabel(self.U_settings)
        self.U_photo_set.setMinimumSize(QtCore.QSize(169, 169))
        self.U_photo_set.setMaximumSize(QtCore.QSize(169, 169))
        self.U_photo_set.setStyleSheet("border-radius: 80px;\n"
                        "background-color: rgba(255, 255, 255, 0);\n"
                        )
        self.U_photo_set.setObjectName("U_photo_set")

        self.U_photo_set.setPixmap(self.set_avatar(self.controller.session_binary_avatar))
        self.U_photo_set.repaint()

        self.gridLayout_2.addWidget(self.U_photo_set, 1, 1, 1, 2, QtCore.Qt.AlignHCenter)


#logout button(settings)
        self.Log_out_but_set = QtWidgets.QPushButton(self.U_settings)
        self.Log_out_but_set.setMinimumSize(QtCore.QSize(0, 41))
        self.Log_out_but_set.setMaximumSize(QtCore.QSize(145, 41))
        self.Log_out_but_set.setFont(self.button_font)
        self.Log_out_but_set.setStyleSheet("QPushButton {\n"
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
        self.Log_out_but_set.setObjectName("Log_out_but_set")
        self.Log_out_but_set.setText("Log out")
        self.Log_out_but_set.clicked.connect(self.log_out)
#add to layout
        self.gridLayout_2.addWidget(self.Log_out_but_set, 9, 2, 1, 1)

#change login button
        self.Ch_log_but = QtWidgets.QPushButton(self.U_settings)
        self.Ch_log_but.setMinimumSize(QtCore.QSize(145, 41))
        self.Ch_log_but.setMaximumSize(QtCore.QSize(145, 41))
        self.Ch_log_but.setStyleSheet("QPushButton {\n"
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
        self.Ch_log_but.setObjectName("Ch_log_but")
        self.Ch_log_but.setFont(self.button_font)
        self.Ch_log_but.setText("Change Login")
        self.Ch_log_but.clicked.connect(self.show_change_login)

#add to layout
        self.gridLayout_2.addWidget(self.Ch_log_but, 4, 3, 1, 1)



#change password button
        self.Ch_pass_butt = QtWidgets.QPushButton(self.U_settings)
        self.Ch_pass_butt.setMinimumSize(QtCore.QSize(145, 41))
        self.Ch_pass_butt.setMaximumSize(QtCore.QSize(145, 41))
        self.Ch_pass_butt.setFont(self.button_font_2)
        self.Ch_pass_butt.setStyleSheet("QPushButton {\n"
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
        self.Ch_pass_butt.setObjectName("Ch_pass_butt")
        self.Ch_pass_butt.setText("Change Password")
        self.Ch_pass_butt.clicked.connect(self.show_change_pass)
#add to layout
        self.gridLayout_2.addWidget(self.Ch_pass_butt, 6, 3, 1, 1)


#change name button
        self.Ch_name_but = QtWidgets.QPushButton(self.U_settings)
        self.Ch_name_but.setMinimumSize(QtCore.QSize(145, 41))
        self.Ch_name_but.setMaximumSize(QtCore.QSize(145, 41))
        self.Ch_name_but.setStyleSheet("QPushButton {\n"
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
        self.Ch_name_but.setObjectName("Ch_name_but")
        self.Ch_name_but.setFont(self.button_font)
        self.Ch_name_but.setText("Change")
        self.Ch_name_but.clicked.connect(self.show_change_name)


#add to layout
        self.gridLayout_2.addWidget(self.Ch_name_but, 2, 3, 1, 1)


#User login(email) label
        self.U_login_set = QtWidgets.QLabel(self.U_settings)
        self.U_login_set.setMinimumSize(QtCore.QSize(147, 41))
        self.U_login_set.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.U_login_set.setObjectName("U_login_set")
        self.U_login_set.setText(f"<html><head/><body><p align=\"center\">{self.controller.session_login}</p></body></html>")
        self.U_login_set.setFont(self.label_font)
#add to layout
        self.gridLayout_2.addWidget(self.U_login_set, 4, 1, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 4, 1)
        self.line_separator_set = QtWidgets.QFrame(self.U_settings)
        self.line_separator_set.setMinimumSize(QtCore.QSize(5, 0))
        self.line_separator_set.setMaximumSize(QtCore.QSize(5, 1000))
        self.line_separator_set.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0.495, y1:0.573864, x2:0.497, y2:0, stop:0 rgba(11, 11, 11, 255), stop:1 rgba(168, 168, 168, 255));\n"
"\n"
"\n"
"")
        self.line_separator_set.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.line_separator_set.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_separator_set.setObjectName("line_separator_set")
        self.gridLayout_3.addWidget(self.line_separator_set, 1, 1, 1, 1)


        self.tabWidget.addTab(self.U_settings, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.U_profile_tab), "Profile")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.U_Performance), "Performance")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.U_chart), "Chart")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.U_panels_map), "Map")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.U_settings), "Settings")



    def select_avatar(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open Image", ".", "Image Files (*.png *.jpg *.bmp)"
        )
        if file_name:
            pixmap = QtGui.QPixmap(file_name)
            if pixmap.width() > 400 or pixmap.height() > 400:
                pixmap = pixmap.scaled(500, 500, QtCore.Qt.AspectRatioMode.KeepAspectRatio)

            mask = QtGui.QPixmap(pixmap.size())
            mask.fill(QtCore.Qt.transparent)
            painter = QtGui.QPainter(mask)
            path = QtGui.QPainterPath()
            path.addRoundedRect(0, 0, mask.width(), mask.height(), 90, 90)
            painter.setBrush(QtGui.QBrush(QtCore.Qt.white))
            painter.drawPath(path)
            painter.end()
            pixmap.setMask(mask.createMaskFromColor(QtCore.Qt.transparent))
            pixmap.scaled(169,169)

            buffer = QtCore.QBuffer()
            buffer.open(QtCore.QIODevice.ReadWrite)
            pixmap.toImage().save(buffer, "PNG")
            image_bytes = buffer.data()
            SqliteDB.update_user_data(self.controller.session_id, None, None, None, None, image_bytes)
            


    def set_avatar(self, binary_avatar):
        qimg = QtGui.QImage.fromData(binary_avatar)
        qpic = QtGui.QPixmap.fromImage(qimg)

        mask = QtGui.QPixmap(qpic.size())
        mask.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter(mask)
        path = QtGui.QPainterPath()
        path.addRoundedRect(0, 0, mask.width(), mask.height(), 45, 45)
        painter.setBrush(QtGui.QBrush(QtCore.Qt.white))
        painter.drawPath(path)
        painter.end()
        qpic.setMask(mask.createMaskFromColor(QtCore.Qt.transparent))
        return qpic.scaled(169,169)


    def add_panels(self):
        if not self.U_name_add_panels.text() or not self.U_email_add_panels.text() or not self.U_pass_add_panels.text() or not self.U_new_panels_adress.text() or not self.U_panels_amount.text() or not self.U_panels_amount.text().isdigit() or not self.U_panels_key.text():
            QtWidgets.QMessageBox.warning(self, "Warning", "Fill every fields please!")
        else:
            user_email = str(self.U_email_add_panels.text())
            password = str(self.U_pass_add_panels.text())
            new_panels_amount = int(self.U_panels_amount.text())
            new_panels_adress = str(self.U_new_panels_adress.text())
            result = SqliteDB.authenticate_user(user_email, password)


            if result[0] is True and result[1] == self.controller.session_id:
                if self.U_name_add_panels.text() == self.controller.session_name:
                    panels_key = int(self.U_panels_key.text())
                    print(f"Panels key = {panels_key}")

                    #get panels_key from file and check it with for i...
                    new_group_data = []
                    if self.controllerAPI.new_group:
                        for i in range(len(self.controllerAPI.new_group)): 
                            if self.controllerAPI.new_group[i]["id"] == panels_key:
                                new_group_data.append(self.controllerAPI.new_group[i])
                    if new_group_data:
                        for i in range(len(new_group_data)):
                            SqliteDB.add_panels_group(self.controller.session_id, new_panels_amount, new_panels_adress, new_group_data[i]["performance"], new_group_data[i]["voltage"], new_group_data[i]["power"], new_group_data[i]["id"])
                        self.controllerAPI.update_new_data(panels_key)
                        QtWidgets.QMessageBox.information(self, "Succesful", "Data has been added")
                        self.U_name_add_panels.setText("")
                        self.U_email_add_panels.setText("") 
                        self.U_pass_add_panels.setText("")
                        self.U_new_panels_adress.setText("")
                        self.U_panels_amount.setText("")
                        self.U_panels_key.setText("")


                        #delete added data from file txt
                    else:
                        QtWidgets.QMessageBox.warning(self, "Error", "The panels group does not exist! Try later")
                        self.U_name_add_panels.setText("")
                        self.U_email_add_panels.setText("") 
                        self.U_pass_add_panels.setText("")
                        self.U_new_panels_adress.setText("")
                        self.U_panels_amount.setText("")
                        self.U_panels_key.setText("")
                else:
                    QtWidgets.QMessageBox.warning(self, "Warning", "Write correct name!")
            else:
                QtWidgets.QMessageBox.warning(self, "Warning", "Incorrect login or password!")
        

    def find_data_perf(self):
        if self.Search_ed_perf.text():
            text = self.Search_ed_perf.text()
            if text.isdigit():
                
                panels_data = SqliteDB.get_panel_group_data(self.controller.session_id, text, None)
                if panels_data is not None:    
                    
                    weather_data = SqliteDB.get_weather(panels_data[0][0], None)
                    self.Objects_info_cap.setRowCount(len(panels_data))
                    for row in range(len(panels_data)):
                        for col in range(len(panels_data[row])+3):
                            if col == 7:
                                item = QtWidgets.QTableWidgetItem(str(weather_data[row][1]))
                            elif col == 8:
                                item = QtWidgets.QTableWidgetItem(str(weather_data[row][3]))
                            elif col == 9:
                                item = QtWidgets.QTableWidgetItem(str(weather_data[row][4]))
                            else:
                                item = QtWidgets.QTableWidgetItem(str(panels_data[row][col]))
                            self.Objects_info_cap.setItem(row, col, item)
                    header = self.Objects_info_cap.verticalHeader()
                    header.setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
                else:
                    QtWidgets.QMessageBox.warning(self, "Error", "Something went wrong")
                self.Search_ed_perf.setText("")
            else:
                try:
                    
                    date_ch = datetime.strptime(text, '%Y-%m-%d')
                    date = date_ch.date()
                    panels_data = SqliteDB.get_panel_group_data(self.controller.session_id, None, date)
                    if panels_data is not None:   
                        weather_data = []

                        #get weather
                        for row in range(len(panels_data)):
                            for row in range(len(panels_data)):
                                weather_data.extend(SqliteDB.get_weather(panels_data[row][0], panels_data[row][6]))
                        
                        
                        #fill tabwidget
                        self.Objects_info_cap.setRowCount(len(panels_data))
                        for row in range(len(panels_data)):
                            for col in range(len(panels_data[row])+3):
                                if col == 7:
                                    item = QtWidgets.QTableWidgetItem(str(weather_data[row][1]))
                                elif col == 8:
                                    item = QtWidgets.QTableWidgetItem(str(weather_data[row][3]))
                                elif col == 9:
                                    item = QtWidgets.QTableWidgetItem(str(weather_data[row][4]))
                                else:
                                    item = QtWidgets.QTableWidgetItem(str(panels_data[row][col]))
                                self.Objects_info_cap.setItem(row, col, item)
                        header = self.Objects_info_cap.verticalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
                    else:
                        QtWidgets.QMessageBox.warning(self, "Error", "Something went wrong")

                except ValueError:
                    QtWidgets.QMessageBox.warning(self, "Error", "Input right date format")
                self.Search_ed_perf.setText("")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Fill every fields please")


    def update_data_perf(self):
        panels_data = SqliteDB.get_panel_group_data(self.controller.session_id, None, None)
        weather_data = []
        
        for row in range(len(panels_data)):
            weather_data.extend(SqliteDB.get_weather(panels_data[row][0], panels_data[row][6]))
            
        self.Objects_info_cap.setRowCount(len(panels_data))
        for row in range(len(panels_data)):
            for col in range(len(panels_data[row])+3):
                if col == 7:
                    item = QtWidgets.QTableWidgetItem(str(weather_data[row][1]))
                elif col == 8:
                    item = QtWidgets.QTableWidgetItem(str(weather_data[row][3]))
                elif col == 9:
                    item = QtWidgets.QTableWidgetItem(str(weather_data[row][4]))
                else:
                    item = QtWidgets.QTableWidgetItem(str(panels_data[row][col]))

                self.Objects_info_cap.setItem(row, col, item)
        header = self.Objects_info_cap.verticalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.Search_ed_perf.setText("")


    def find_data_prof(self):
        if self.Search_ed_prof.text():
            text = self.Search_ed_prof.text()
            if text.isdigit():
                
                panels_data = SqliteDB.get_panel_group_data(self.controller.session_id, text, None)
                if panels_data is not None:    
                    
                    weather_data = SqliteDB.get_weather(panels_data[0][0], None)
                    self.Objects_info_prof.setRowCount(len(panels_data))
                    for row in range(len(panels_data)):
                        for col in range(5):
                            if col == 4:
                                item = QtWidgets.QTableWidgetItem(str(weather_data[row][1]))
                            else:
                                item = QtWidgets.QTableWidgetItem(str(panels_data[row][col]))
                            self.Objects_info_prof.setItem(row, col, item)
                    header = self.Objects_info_prof.verticalHeader()
                    header.setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
                else:
                    QtWidgets.QMessageBox.warning(self, "Error", "Something went wrong")
                self.Search_ed_prof.setText("")
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Input correct value")
                self.Search_ed_prof.setText("")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Fill every fields please")


    def update_data_prof(self):
        data = SqliteDB.get_panel_group_data(self.controller.session_id, None, None)
        
        weather_data = []
        
        for row in range(len(data)):
            weather_data.extend(SqliteDB.get_weather(data[row][0], data[row][6]))
        
        self.Objects_info_prof.setRowCount(len(data))
        for row in range(len(data)):
            for col in range(5):
                if col == 4:
                    item = QtWidgets.QTableWidgetItem(str(weather_data[row][1]))
                else:
                    item = QtWidgets.QTableWidgetItem(str(data[row][col]))
                self.Objects_info_prof.setItem(row, col, item)
        self.Search_ed_prof.setText("")
        header = self.Objects_info_prof.verticalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Fixed)


    def chart_time_change(self):
        index = self.chart_time_combobox.currentIndex()
        if self.Search_ed_chart.text() is not None:
            group_id_ed = SqliteDB.get_panel_group_data(self.controller.session_id,self.Search_ed_chart.text(), None)
            if group_id_ed is not None:
                group_id = int(self.Search_ed_chart.text())
            
                if index == 0:
                    self.chart.setTitle("Panels performance for last day")
                    now = QtCore.QDateTime.currentDateTime()
                    start_time = now.addSecs(-24 * 3600)
                    self.series.clear()  
                    self.chart.removeSeries(self.series) 
                    self.axisX.setTickCount(24)
                    self.axisX.setFormat("HH")
                    #get data for axis_y
                    max_y = 0
                    for i in range(25):
                        
                        hour_ago = start_time.addSecs(i * 3600)
                        data_row = SqliteDB.get_panel_group_data(self.controller.session_id, group_id, hour_ago.toPyDateTime().strftime('%Y-%m-%d-%H'))
                        
                        performance = 0
                        if data_row is not None:
                            data = []
                            data.extend(data_row)
                            for row in data:
                                performance = float(row[3])
                                max_y = max(max_y, performance)
                        else:
                            performance = float(0)
                        self.series.append(hour_ago.toMSecsSinceEpoch(), performance)
                    
                    self.axisY.setRange(0, max_y)
                    self.axisX.setRange(start_time, now)


                    self.chart.addSeries(self.series)


                elif index == 1:
                    self.chart.setTitle("Panels performance for last month")
                    now = QtCore.QDateTime.currentDateTime()
                    start_time = now.addSecs(-(30*24) * 3600)
                    self.series.clear()  
                    self.chart.removeSeries(self.series)  
                    self.axisX.setTickCount(30)
                    self.axisX.setFormat("MM/dd")
                    #get data for axis_y
                    max_y = 0
                    for i in range((30*24)+1):
                        
                        hour_ago = start_time.addSecs(i * 3600)
                        data_row = SqliteDB.get_panel_group_data(self.controller.session_id, group_id, hour_ago.toPyDateTime().strftime('%Y-%m-%d-%H'))
                        
                
                        performance = 0
                        if data_row is not None:
                            data = []
                            data.extend(data_row)
                            for row in data:
                                performance = float(row[3])
                                max_y = max(max_y, performance)
                        else:
                            performance = float(0)
                        self.series.append(hour_ago.toMSecsSinceEpoch(), performance)
                    
                    self.axisY.setRange(0, max_y)  
                    self.axisX.setRange(start_time, now)
                    self.chart.addSeries(self.series)

                
                elif index == 2:
                    self.chart.setTitle("Panels performance for all time")
                    now_axis = datetime.now()
                    data = SqliteDB.get_panel_group_data(self.controller.session_id,group_id,None)
                    
                    oldest_row = min(data, key=lambda x: datetime.strptime(x[-1], '%Y-%m-%d-%H'))
                    oldest_date = datetime.strptime(oldest_row[-1], '%Y-%m-%d-%H')
                    date_difference = now_axis - oldest_date
                    days_difference = date_difference.days
                    
                    if days_difference >= 1:
                        self.axisX.setTickCount(days_difference)
                        self.axisX.setFormat("yyyy/MM/dd")  
                        self.axisX.setRange(oldest_date, now_axis)  
                    else:
                        self.axisX.setTickCount(24)  
                        self.axisX.setFormat("HH")  
                        self.axisX.setRange(oldest_date, now_axis)  

                        
                    now = QtCore.QDateTime.currentDateTime()
                    start_time = now.addSecs(-(days_difference * 24) * 3600)
                    self.series.clear()  
                    self.chart.removeSeries(self.series)  
                    #get data for axis_y
                    max_y = 0
                    for i in range((days_difference * 24)+1):
                        
                        hour_ago = start_time.addSecs(i * 3600)
                        data_row = SqliteDB.get_panel_group_data(self.controller.session_id, group_id, hour_ago.toPyDateTime().strftime('%Y-%m-%d-%H'))
                        
                        performance = 0
                        if data_row is not None:
                            data = []
                            data.extend(data_row)
                            for row in data:
                                performance = float(row[3])
                                max_y = max(max_y, performance)
                        else:
                            performance = float(0)
                        self.series.append(hour_ago.toMSecsSinceEpoch(), performance)
                    
                    self.axisY.setRange(0, max_y)  

                    self.chart.addSeries(self.series)

            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Input correct group number")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Input the group number")

        


    def show_change_name(self):
        self.controller.show_change_name()
        self.close()


    def show_change_login(self):
        self.controller.show_change_login()
        self.close()

    def show_change_pass(self):
        self.controller.show_change_pass()
        self.close()

    
    def log_out(self):
        self.controller.show_login()
        self.close()


        
import Backgrounds
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    profile_window = ProfileWindow()
    profile_window.show()
    sys.exit(app.exec_())
