# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QSizePolicy, QVBoxLayout, QWidget)
import iconset_rc

class Ui_Splash(object):
    def setupUi(self, Splash):
        if not Splash.objectName():
            Splash.setObjectName(u"Splash")
        Splash.resize(500, 500)
        Splash.setMinimumSize(QSize(500, 500))
        Splash.setMaximumSize(QSize(500, 500))
        self.centralwidget = QWidget(Splash)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.circle = QFrame(self.container)
        self.circle.setObjectName(u"circle")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.circle.sizePolicy().hasHeightForWidth())
        self.circle.setSizePolicy(sizePolicy)
        self.circle.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(17, 27, 43);\n"
"	color:rgb(0, 255, 255);\n"
"	border-radius: 220px; 	\n"
"	font: 12pt \"Ethnocentric\";\n"
"\n"
"}")
        self.circle.setFrameShape(QFrame.NoFrame)
        self.circle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.circle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.texts = QFrame(self.circle)
        self.texts.setObjectName(u"texts")
        self.texts.setMaximumSize(QSize(16777215, 260))
        self.texts.setStyleSheet(u"background:none;")
        self.texts.setFrameShape(QFrame.NoFrame)
        self.texts.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.texts)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QFrame(self.texts)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setFrameShape(QFrame.StyledPanel)
        self.gridLayout_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.gridLayout_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.branding = QLabel(self.gridLayout_2)
        self.branding.setObjectName(u"branding")
        self.branding.setMaximumSize(QSize(16777215, 16777215))
        self.branding.setStyleSheet(u"font: 9pt \"Ethnocentric\";")
        self.branding.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.branding, 7, 0, 1, 1)

        self.frame = QFrame(self.gridLayout_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 35))
        self.frame.setMaximumSize(QSize(300, 35))
        self.frame.setStyleSheet(u"background-color: rgb(40, 64, 100);\n"
"border-radius: 13px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.version = QLabel(self.frame)
        self.version.setObjectName(u"version")
        self.version.setMaximumSize(QSize(400, 50))
        self.version.setStyleSheet(u"	border-radius: 25px;\n"
"	background-color: rgb(40, 64, 100);\n"
"")
        self.version.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.version, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame, 6, 0, 1, 1, Qt.AlignHCenter)

        self.title = QLabel(self.gridLayout_2)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 50))
        self.title.setMaximumSize(QSize(500, 16777215))
        self.title.setStyleSheet(u"font: 46pt \"Ethnocentric\";")
        self.title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.title, 4, 0, 1, 1)

        self.empty = QFrame(self.gridLayout_2)
        self.empty.setObjectName(u"empty")
        self.empty.setMinimumSize(QSize(0, 80))
        self.empty.setFrameShape(QFrame.StyledPanel)
        self.empty.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.empty, 5, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.gridLayout_2)


        self.verticalLayout_3.addWidget(self.texts)


        self.verticalLayout_2.addWidget(self.circle)


        self.verticalLayout.addWidget(self.container)

        Splash.setCentralWidget(self.centralwidget)

        self.retranslateUi(Splash)

        QMetaObject.connectSlotsByName(Splash)
    # setupUi

    def retranslateUi(self, Splash):
        Splash.setWindowTitle(QCoreApplication.translate("Splash", u"Loading", None))
        self.branding.setText(QCoreApplication.translate("Splash", u"2022 Development by S3R43o3", None))
        self.version.setText(QCoreApplication.translate("Splash", u"v1.5.8", None))
        self.title.setText(QCoreApplication.translate("Splash", u"S4M 2.0", None))
    # retranslateUi

