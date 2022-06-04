from loguru import logger
from interface import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


from qt_material import apply_stylesheet
import sys, os, time, datetime, json
from ui_utils import UIutils










class UserUI(QMainWindow):
    def __init__(self ):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.men_button.clicked.connect(lambda: self.animateMenu())
        self.ui_utils = UIutils()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle("SAM 2.0")
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setXOffset(0)
        self.shadow.setColor(QColor(0, 240, 255, 550))
        self.setGraphicsEffect(self.shadow)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.newuser_error_label.setText("")
        itemsnew = ["Frau", "Mann"]
        langs = ["Deutsch", "Englisch"]
        self.ui.gender_combobox.addItems(itemsnew)
        self.ui.newuser_lang_box.addItems(langs)
        if self.ui_utils.is_new_user():
            self.ui.home_start_btn.setEnabled(False)
        self.ui.details_button.clicked.connect(lambda: self.animateMiniUI())


        self.ui.newuser_create_btn.clicked.connect(lambda: self.createNewUser())
        self.ui.x_button.clicked.connect(lambda: self.closeWindow())
        self.ui.mini_button.clicked.connect(lambda: self.showMinimized())
        self.ui.home_newuser_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.new_user_page))
        self.ui.home_start_btn.clicked.connect(lambda: self.start_sam())
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
        elif self.ui_utils.name_exist(new_username) == True:
            self.ui.newuser_error_label.setText('"{}" existiert bereits! Wähle einen anderen Benutzernamen!',new_username)
            return
        new_usergender = self.ui.gender_combobox.currentText()            

        new_userphone = self.ui.newuser_number.text()
        if new_userphone == "" or new_userphone == None:
            new_userphone == 0
        new_userphone = int(new_userphone)
        if self.ui.guest_checker.isChecked():
            new_userintents = ["animalsounds","gettime"]
        else:
            new_userintents = ["*"]
        new_uservoice = []
        new_userlang = self.ui.newuser_lang_box.currentText()
        self.ui_utils.create_user(new_username,
        new_usergender,
        new_userphone,
        new_uservoice,
        new_userintents,
        new_userlang)
        logger.debug("User {} created".format(new_username))
        self.update_userlist()
    
    def update_userlist(self):
        self.ui.home_user_list.clear()
        if self.ui_utils.is_new_user():
            self.ui.home_start_btn.setEnabled(False)
        else:
            self.ui.home_start_btn.setEnabled(True)
        for user in self.ui_utils.get_user_list():
            if user== "sera" or user == "sarah":
                pass
            else:                
                new_item = QListWidgetItem()
                new_item.setText(user.capitalize())
                self.ui.home_user_list.addItem(new_item)

    def reset_newuser(self):
        self.ui.new_username.setText("")
        self.ui.newuser_number.setText("")
        self.ui.guest_checker.setChecked(False)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.exit(app.exec_())