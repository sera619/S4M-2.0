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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import iconset_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(997, 794)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"border:none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
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

        self.horizontalLayout_4.addWidget(self.men_button, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.top_left_frame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.top_mid_frame = QFrame(self.top_frame)
        self.top_mid_frame.setObjectName(u"top_mid_frame")
        self.top_mid_frame.setFrameShape(QFrame.StyledPanel)
        self.top_mid_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.top_mid_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.top_mid_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.top_mid_frame, 0, Qt.AlignTop)

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
        self.window_buttons.setStyleSheet(u"Border: none")
        self.window_buttons.setFrameShape(QFrame.StyledPanel)
        self.window_buttons.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout = QHBoxLayout(self.window_buttons)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mini_button = QPushButton(self.window_buttons)
        self.mini_button.setObjectName(u"mini_button")

        self.horizontalLayout.addWidget(self.mini_button, 0, Qt.AlignRight)

        self.maxi_button = QPushButton(self.window_buttons)
        self.maxi_button.setObjectName(u"maxi_button")

        self.horizontalLayout.addWidget(self.maxi_button, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.x_button = QPushButton(self.window_buttons)
        self.x_button.setObjectName(u"x_button")

        self.horizontalLayout.addWidget(self.x_button, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.window_buttons)


        self.horizontalLayout_3.addWidget(self.top_right_frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.top_frame, 0, Qt.AlignTop)

        self.mid_main_frame = QFrame(self.centralwidget)
        self.mid_main_frame.setObjectName(u"mid_main_frame")
        self.mid_main_frame.setFrameShape(QFrame.StyledPanel)
        self.mid_main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.mid_main_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.side_menu = QFrame(self.mid_main_frame)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setFrameShape(QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.side_menu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.side_menu)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.side_menu)

        self.stackedWidget = QStackedWidget(self.mid_main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.stackedWidget.addWidget(self.home_page)
        self.user_page = QWidget()
        self.user_page.setObjectName(u"user_page")
        self.stackedWidget.addWidget(self.user_page)

        self.horizontalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.mid_main_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
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
        self.footer_right_label = QLabel(self.footer_right_frame)
        self.footer_right_label.setObjectName(u"footer_right_label")

        self.verticalLayout_2.addWidget(self.footer_right_label, 0, Qt.AlignRight|Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.footer_right_frame)


        self.verticalLayout_4.addWidget(self.footer_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.men_button.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.mini_button.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.maxi_button.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.x_button.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.footer_left_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.footer_right_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

