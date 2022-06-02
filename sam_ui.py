from cgitb import text
from loguru import logger
from interface import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect,QListWidgetItem
from PySide6.QtCore import *
from PySide6 import QtGui
from PySide6 import *
from qt_material import apply_stylesheet
import sys, os, time, datetime, json
from ui_utils import UIutils

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self ):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.men_button.clicked.connect(lambda: self.animateMenu())
        self.ui_utils = UIutils()
        apply_stylesheet(app, theme="dark_red.xml")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle("SAM 2.0")
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setXOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 92, 157, 550))
        self.ui.side_menu.setGraphicsEffect(self.shadow)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        itemsnew = ["Frau", "Mann"]
        self.ui.gender_combobox.addItems(itemsnew)



        self.ui.x_button.clicked.connect(lambda: self.closeWindow())
        self.ui.mini_button.clicked.connect(lambda: self.showMinimized())
        self.ui.home_newuser_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.new_user_page))
        self.ui.home_login_btn.clicked.connect(lambda: self.start_sam())
        self.ui.home_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))
        self.ui.users_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.new_user_page))
        self.ui.newuser_cancel_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))

        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        self.update_userlist()
        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.top_frame.mouseMoveEvent = moveWindow

    def animateMenu(self):
        width = self.ui.side_menu.minimumWidth()
        if width == 0:
            newWidth = 135
        else:
            newWidth = 0
        self.animation = QPropertyAnimation(self.ui.side_menu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()


    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def closeWindow(self):
        self.close()
        sys.exit(0)
    
    def createNewUser(self):
        new_username = self.ui.new_username.text()
        if new_username == "" or new_username == None:
            self.ui.newuser_error_label.setText("Bitte gebe einen Benutzernamen ein!")
            return
        elif UIutils.name_exist(new_username):
            self.ui.newuser_error_label.setText('"{}" existiert bereits! Wähle einen anderen Benutzernamen!',new_username)
            return
        new_usergender = self.ui.gender_combobox.currentText()            

        new_userphone = self.ui.newuser_number.text
        if new_userphone == "" or new_userphone == None:
            new_userphone == 0
        new_userphone = int(new_userphone)
        if self.ui.guest_checker.isChecked():
            new_userintents = ["animalsounds","gettime"]
        else:
            new_userintents = ["*"]
        new_uservoice = []
        self.ui_utils.create_user(new_username,new_usergender,new_userphone,new_userintents,new_uservoice)
        logger.debug("User {} created".format(new_username))
        self.update_userlist()
    
    def update_userlist(self):        
        for user in self.ui_utils.get_user_list():
            new_item = QListWidgetItem()
            new_item.setText(user)
            self.ui.home_user_list.addItem(new_item)

    def reset_newuser(self):
        self.ui.new_username.setText("")
        self.ui.newuser_number.setText("")
        self.ui.guest_checker.setChecked(False)

    def start_sam(self):
        import main
        main()




def main():
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Error: {}".format(e))
    except KeyboardInterrupt:
        print('\n\nProgram terminated by user.\n')
        sys.exit(0)
    finally:
        sys.exit(0)
