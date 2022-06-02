# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'S4M-MiniUi.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MiniFrame(object):
    def setupUi(self, MiniFrame):
        if not MiniFrame.objectName():
            MiniFrame.setObjectName(u"MiniFrame")
        MiniFrame.setEnabled(True)
        MiniFrame.resize(179, 290)
        MiniFrame.setStyleSheet(u"*{\n"
"	background-color: rgb(2, 28, 35);\n"
"	color: rgb(0, 255, 255);\n"
"	border:none;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(MiniFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Main_frame = QFrame(MiniFrame)
        self.Main_frame.setObjectName(u"Main_frame")
        self.Main_frame.setFrameShape(QFrame.StyledPanel)
        self.Main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Main_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.Main_frame)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.header_frame)

        self.mid_frame = QFrame(self.Main_frame)
        self.mid_frame.setObjectName(u"mid_frame")
        self.mid_frame.setFrameShape(QFrame.StyledPanel)
        self.mid_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.mid_frame)

        self.button_frame = QFrame(self.Main_frame)
        self.button_frame.setObjectName(u"button_frame")
        self.button_frame.setFrameShape(QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.button_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.button_frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.button_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.button_frame, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.Main_frame)


        self.retranslateUi(MiniFrame)

        QMetaObject.connectSlotsByName(MiniFrame)
    # setupUi

    def retranslateUi(self, MiniFrame):
        MiniFrame.setWindowTitle(QCoreApplication.translate("MiniFrame", u"Frame", None))
        self.pushButton.setText(QCoreApplication.translate("MiniFrame", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MiniFrame", u"PushButton", None))
    # retranslateUi

