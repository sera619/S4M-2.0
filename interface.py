# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'S4M-UI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
import iconset_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(766, 439)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"border:none;\n"
"border-radius: 30pt;\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"	font: 10pt \"Ethnocentric\";\n"
"}\n"
"*{\n"
"	background-color: rgb(2, 28, 35);\n"
"	color: rgb(0, 255, 255);\n"
"	border:none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border-radius: 20px;")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(12, 4, 12, 4)
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(0, 25))
        self.top_frame.setMaximumSize(QSize(16777215, 0))
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.top_left_frame = QFrame(self.top_frame)
        self.top_left_frame.setObjectName(u"top_left_frame")
        self.top_left_frame.setStyleSheet(u"border:none\n"
"")
        self.top_left_frame.setFrameShape(QFrame.StyledPanel)
        self.top_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.top_left_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.men_button = QPushButton(self.top_left_frame)
        self.men_button.setObjectName(u"men_button")

        self.horizontalLayout_4.addWidget(self.men_button, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.top_left_frame, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.top_mid_frame = QFrame(self.top_frame)
        self.top_mid_frame.setObjectName(u"top_mid_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_mid_frame.sizePolicy().hasHeightForWidth())
        self.top_mid_frame.setSizePolicy(sizePolicy)
        self.top_mid_frame.setFrameShape(QFrame.StyledPanel)
        self.top_mid_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.top_mid_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.top_mid_frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 22pt \"Ethnocentric\";")

        self.horizontalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_3.addWidget(self.top_mid_frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.top_right_frame = QFrame(self.top_frame)
        self.top_right_frame.setObjectName(u"top_right_frame")
        self.top_right_frame.setFrameShape(QFrame.StyledPanel)
        self.top_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.top_right_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.window_buttons = QFrame(self.top_right_frame)
        self.window_buttons.setObjectName(u"window_buttons")
        self.window_buttons.setLayoutDirection(Qt.LeftToRight)
        self.window_buttons.setStyleSheet(u"Border: none;\n"
"")
        self.window_buttons.setFrameShape(QFrame.StyledPanel)
        self.window_buttons.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout = QHBoxLayout(self.window_buttons)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mini_button = QPushButton(self.window_buttons)
        self.mini_button.setObjectName(u"mini_button")
        self.mini_button.setStyleSheet(u"QPushButton{\n"
"	padding: 2px 4px;\n"
"	color: rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 1px solid;\n"
"	border-radius: 10px;\n"
"	\n"
"	border-color: rgb(0, 255, 255);\n"
"	background-color: rgb(170, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 1px solid;\n"
"	border-radius: 10px;\n"
"	color: black;\n"
"	border-color: rgb(0, 255, 255);\n"
"	background-color: rgb(170, 255, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mini_button.setIcon(icon)
        self.mini_button.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.mini_button, 0, Qt.AlignRight|Qt.AlignTop)

        self.maxi_button = QPushButton(self.window_buttons)
        self.maxi_button.setObjectName(u"maxi_button")
        self.maxi_button.setStyleSheet(u"QPushButton{\n"
"	padding: 2px 4px;\n"
"	color: rgb(0, 255, 255);\n"
"}\n"
"QIcon{\n"
"color: rgb(0,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 1px solid;\n"
"	border-radius: 10px;\n"
"	\n"
"	border-color: rgb(0, 255, 255);\n"
"	background-color: rgb(170, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 1px solid;\n"
"	border-radius: 10px;\n"
"	color: black;\n"
"	border-color: rgb(0, 255, 255);\n"
"	background-color: rgb(170, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow-down-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maxi_button.setIcon(icon1)
        self.maxi_button.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.maxi_button, 0, Qt.AlignRight|Qt.AlignTop)

        self.x_button = QPushButton(self.window_buttons)
        self.x_button.setObjectName(u"x_button")
        self.x_button.setStyleSheet(u"QPushButton{\n"
"	padding: 2px 4px;\n"
"	color: rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 1px solid;\n"
"	border-radius: 10px;\n"
"	\n"
"	border-color: rgb(0, 255, 255);\n"
"	background-color: rgb(170, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 1px solid;\n"
"	border-radius: 10px;\n"
"	color: black;\n"
"	border-color: rgb(0, 255, 255);\n"
"	background-color: rgb(170, 255, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.x_button.setIcon(icon2)
        self.x_button.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.x_button, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.window_buttons, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.top_right_frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.top_frame, 0, Qt.AlignTop)

        self.mid_main_frame = QFrame(self.centralwidget)
        self.mid_main_frame.setObjectName(u"mid_main_frame")
        self.mid_main_frame.setFrameShape(QFrame.StyledPanel)
        self.mid_main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.mid_main_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 3, 0, 0)
        self.side_menu = QFrame(self.mid_main_frame)
        self.side_menu.setObjectName(u"side_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.side_menu.sizePolicy().hasHeightForWidth())
        self.side_menu.setSizePolicy(sizePolicy1)
        self.side_menu.setMinimumSize(QSize(0, 0))
        self.side_menu.setMaximumSize(QSize(0, 16777215))
        self.side_menu.setStyleSheet(u"font: 7 pt \"Ethnocentric\";")
        self.side_menu.setFrameShape(QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.side_menu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.skills_btn_label = QLabel(self.side_menu)
        self.skills_btn_label.setObjectName(u"skills_btn_label")

        self.gridLayout.addWidget(self.skills_btn_label, 3, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.details_button = QPushButton(self.side_menu)
        self.details_button.setObjectName(u"details_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/zoom-in.png", QSize(), QIcon.Normal, QIcon.Off)
        self.details_button.setIcon(icon3)
        self.details_button.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.details_button, 4, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.skills_button = QPushButton(self.side_menu)
        self.skills_button.setObjectName(u"skills_button")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/book.png", QSize(), QIcon.Normal, QIcon.Off)
        self.skills_button.setIcon(icon4)
        self.skills_button.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.skills_button, 3, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.users_btn_label = QLabel(self.side_menu)
        self.users_btn_label.setObjectName(u"users_btn_label")

        self.gridLayout.addWidget(self.users_btn_label, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.users_button = QPushButton(self.side_menu)
        self.users_button.setObjectName(u"users_button")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/users.png", QSize(), QIcon.Normal, QIcon.Off)
        self.users_button.setIcon(icon5)
        self.users_button.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.users_button, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.detail_btn_label = QLabel(self.side_menu)
        self.detail_btn_label.setObjectName(u"detail_btn_label")

        self.gridLayout.addWidget(self.detail_btn_label, 4, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.home_button = QPushButton(self.side_menu)
        self.home_button.setObjectName(u"home_button")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_button.setIcon(icon6)
        self.home_button.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.home_button, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.home_btn_label = QLabel(self.side_menu)
        self.home_btn_label.setObjectName(u"home_btn_label")

        self.gridLayout.addWidget(self.home_btn_label, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_6.addWidget(self.side_menu, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.mid_main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setStyleSheet(u"QLabel{\n"
"	font: 8pt \"Ethnocentric\";\n"
"color:rgb(0, 255, 255);\n"
"}\n"
"QPushButton{\n"
"	font: 8pt \"Ethnocentric\";\n"
"	border: 1px solid;\n"
"padding: 5px 10px;\n"
"	border-radius: 15px;\n"
"}")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.home_page)
        self.horizontalLayout_7.setSpacing(4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.home_main_frame = QFrame(self.home_page)
        self.home_main_frame.setObjectName(u"home_main_frame")
        self.home_main_frame.setFrameShape(QFrame.StyledPanel)
        self.home_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.home_main_frame)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.home_head_label = QLabel(self.home_main_frame)
        self.home_head_label.setObjectName(u"home_head_label")
        font = QFont()
        font.setFamilies([u"Ethnocentric"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.home_head_label.setFont(font)
        self.home_head_label.setStyleSheet(u"QLabel{\n"
"	font: 14pt \"Ethnocentric\";\n"
"}")

        self.verticalLayout_5.addWidget(self.home_head_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.home_info_label = QLabel(self.home_main_frame)
        self.home_info_label.setObjectName(u"home_info_label")

        self.verticalLayout_5.addWidget(self.home_info_label, 0, Qt.AlignHCenter)

        self.home_user_list = QListWidget(self.home_main_frame)
        self.home_user_list.setObjectName(u"home_user_list")

        self.verticalLayout_5.addWidget(self.home_user_list, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.home_btn_frame = QFrame(self.home_main_frame)
        self.home_btn_frame.setObjectName(u"home_btn_frame")
        self.home_btn_frame.setFrameShape(QFrame.StyledPanel)
        self.home_btn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.home_btn_frame)
        self.horizontalLayout_8.setSpacing(8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.home_login_btn = QPushButton(self.home_btn_frame)
        self.home_login_btn.setObjectName(u"home_login_btn")
        self.home_login_btn.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"border-color: rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	border-color: rgb(0, 255, 255);\n"
"	color: black;\n"
"	background-color: rgb(170, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	border-color: rgb(0, 255, 255);\n"
"	color: black;	\n"
"	background-color: rgb(0, 255, 255);\n"
"}\n"
"	")

        self.horizontalLayout_8.addWidget(self.home_login_btn, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.home_newuser_btn = QPushButton(self.home_btn_frame)
        self.home_newuser_btn.setObjectName(u"home_newuser_btn")
        font1 = QFont()
        font1.setFamilies([u"Ethnocentric"])
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        self.home_newuser_btn.setFont(font1)
        self.home_newuser_btn.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"border-color: rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	border-color: rgb(0, 255, 255);\n"
"	color: black;\n"
"	background-color: rgb(170, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	border-color: rgb(0, 255, 255);\n"
"	color: black;	\n"
"	background-color: rgb(0, 255, 255);\n"
"}\n"
"	")
        self.home_newuser_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_8.addWidget(self.home_newuser_btn, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_5.addWidget(self.home_btn_frame)


        self.horizontalLayout_7.addWidget(self.home_main_frame)

        self.stackedWidget.addWidget(self.home_page)
        self.new_user_page = QWidget()
        self.new_user_page.setObjectName(u"new_user_page")
        self.new_user_page.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.new_user_page)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 9, 0, -1)
        self.newuser_head_frame = QFrame(self.new_user_page)
        self.newuser_head_frame.setObjectName(u"newuser_head_frame")
        self.newuser_head_frame.setFrameShape(QFrame.StyledPanel)
        self.newuser_head_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.newuser_head_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.newuser_head_label = QLabel(self.newuser_head_frame)
        self.newuser_head_label.setObjectName(u"newuser_head_label")
        self.newuser_head_label.setStyleSheet(u"font: 13pt \"Ethnocentric\";")

        self.verticalLayout_7.addWidget(self.newuser_head_label, 0, Qt.AlignHCenter)

        self.newuser_error_label = QLabel(self.newuser_head_frame)
        self.newuser_error_label.setObjectName(u"newuser_error_label")
        self.newuser_error_label.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_7.addWidget(self.newuser_error_label, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.newuser_head_frame)

        self.newuser_mainframe = QFrame(self.new_user_page)
        self.newuser_mainframe.setObjectName(u"newuser_mainframe")
        sizePolicy1.setHeightForWidth(self.newuser_mainframe.sizePolicy().hasHeightForWidth())
        self.newuser_mainframe.setSizePolicy(sizePolicy1)
        self.newuser_mainframe.setStyleSheet(u"\n"
"font: 8pt \"Ethnocentric\";")
        self.newuser_mainframe.setFrameShape(QFrame.StyledPanel)
        self.newuser_mainframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.newuser_mainframe)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, -1)
        self.frame_3 = QFrame(self.newuser_mainframe)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_12.addWidget(self.label_5, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.new_username = QLineEdit(self.frame_3)
        self.new_username.setObjectName(u"new_username")
        self.new_username.setMaxLength(14)

        self.horizontalLayout_12.addWidget(self.new_username, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.frame = QFrame(self.newuser_mainframe)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_10.addWidget(self.label_3, 0, Qt.AlignRight)

        self.newuser_number = QLineEdit(self.frame)
        self.newuser_number.setObjectName(u"newuser_number")
        self.newuser_number.setMaxLength(13)

        self.horizontalLayout_10.addWidget(self.newuser_number, 0, Qt.AlignLeft)


        self.verticalLayout_6.addWidget(self.frame)

        self.new_gender_frame = QFrame(self.newuser_mainframe)
        self.new_gender_frame.setObjectName(u"new_gender_frame")
        self.new_gender_frame.setFrameShape(QFrame.StyledPanel)
        self.new_gender_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.new_gender_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(10, 5, 10, 5)
        self.label_2 = QLabel(self.new_gender_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_9.addWidget(self.label_2, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.gender_combobox = QComboBox(self.new_gender_frame)
        self.gender_combobox.setObjectName(u"gender_combobox")

        self.horizontalLayout_9.addWidget(self.gender_combobox, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_6.addWidget(self.new_gender_frame)

        self.frame_2 = QFrame(self.newuser_mainframe)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_11.addWidget(self.label_4, 0, Qt.AlignRight)

        self.guest_checker = QCheckBox(self.frame_2)
        self.guest_checker.setObjectName(u"guest_checker")

        self.horizontalLayout_11.addWidget(self.guest_checker, 0, Qt.AlignLeft)


        self.verticalLayout_6.addWidget(self.frame_2)


        self.verticalLayout_8.addWidget(self.newuser_mainframe)

        self.frame_5 = QFrame(self.new_user_page)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.newuser_cancel_btn = QPushButton(self.frame_5)
        self.newuser_cancel_btn.setObjectName(u"newuser_cancel_btn")
        self.newuser_cancel_btn.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"border-color: rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	border-color: rgb(0, 255, 255);\n"
"	color: black;\n"
"	background-color: rgb(170, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	border-color: rgb(0, 255, 255);\n"
"	color: black;	\n"
"	background-color: rgb(0, 255, 255);\n"
"}\n"
"	")

        self.horizontalLayout_13.addWidget(self.newuser_cancel_btn, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.newuser_create_btn = QPushButton(self.frame_5)
        self.newuser_create_btn.setObjectName(u"newuser_create_btn")
        self.newuser_create_btn.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"border-color: rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	border-color: rgb(0, 255, 255);\n"
"	color: black;\n"
"	background-color: rgb(170, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	border-color: rgb(0, 255, 255);\n"
"	color: black;	\n"
"	background-color: rgb(0, 255, 255);\n"
"}\n"
"	")

        self.horizontalLayout_13.addWidget(self.newuser_create_btn, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.new_user_page)

        self.horizontalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.mid_main_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.footer_frame.sizePolicy().hasHeightForWidth())
        self.footer_frame.setSizePolicy(sizePolicy2)
        self.footer_frame.setMinimumSize(QSize(0, 15))
        self.footer_frame.setMaximumSize(QSize(16777215, 0))
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.footer_left_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.footer_left_label = QLabel(self.footer_left_frame)
        self.footer_left_label.setObjectName(u"footer_left_label")
        self.footer_left_label.setStyleSheet(u"font: 6pt \"Ethnocentric\";")

        self.verticalLayout_3.addWidget(self.footer_left_label, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.footer_left_frame, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.footer_right_frame = QFrame(self.footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.footer_right_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.footer_help_btn = QPushButton(self.footer_right_frame)
        self.footer_help_btn.setObjectName(u"footer_help_btn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/help-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footer_help_btn.setIcon(icon7)
        self.footer_help_btn.setIconSize(QSize(14, 14))

        self.verticalLayout_2.addWidget(self.footer_help_btn, 0, Qt.AlignRight|Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.footer_right_frame, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_4.addWidget(self.footer_frame, 0, Qt.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.gender_combobox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.men_button.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"S4M 2.0 Assistant", None))
        self.mini_button.setText("")
        self.maxi_button.setText("")
        self.x_button.setText("")
        self.skills_btn_label.setText(QCoreApplication.translate("MainWindow", u"Skills", None))
        self.details_button.setText("")
        self.skills_button.setText("")
        self.users_btn_label.setText(QCoreApplication.translate("MainWindow", u"Users", None))
        self.users_button.setText("")
        self.detail_btn_label.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.home_button.setText("")
        self.home_btn_label.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.home_head_label.setText(QCoreApplication.translate("MainWindow", u"WIllkommen", None))
        self.home_info_label.setText(QCoreApplication.translate("MainWindow", u"Aktuelle Benutzer:", None))
        self.home_login_btn.setText(QCoreApplication.translate("MainWindow", u"Starte S4M", None))
        self.home_newuser_btn.setText(QCoreApplication.translate("MainWindow", u"Neuer User", None))
        self.newuser_head_label.setText(QCoreApplication.translate("MainWindow", u"Neuen Benutzer erstellen", None))
        self.newuser_error_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Benutzername", None))
        self.new_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max. 12 Zeichen", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Telefonnr.", None))
        self.newuser_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"012345678911", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.gender_combobox.setCurrentText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Gastzugang", None))
        self.guest_checker.setText(QCoreApplication.translate("MainWindow", u"Ist ein Gast", None))
        self.newuser_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Abbrechen", None))
        self.newuser_create_btn.setText(QCoreApplication.translate("MainWindow", u"Erstellen", None))
        self.footer_left_label.setText(QCoreApplication.translate("MainWindow", u"S4M 2.0 v1.0.1 | by S3R43o3", None))
        self.footer_help_btn.setText("")
    # retranslateUi

