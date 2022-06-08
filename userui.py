from ctypes import util
from loguru import logger
from interface import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


from qt_material import apply_stylesheet
import sys, os, time, datetime, json, webbrowser
from ui_utils import UIutils










class UserUI(QMainWindow):
    def __init__(self ):
        QMainWindow.__init__(self)
        logger.debug('\nLaunching Userinterface')
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.men_button.clicked.connect(lambda: self.animateMenu())
        self.ui_utils = UIutils()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle("SAM 2.0")
        self.setWindowIcon(QIcon('assets/favpng.png'))
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
        self.ui.edit_gender_box.addItems(itemsnew)
        self.ui.gender_combobox.addItems(itemsnew)
        self.ui.edit_user_lang.addItems(langs)
        self.ui.newuser_lang_box.addItems(langs)
        if self.ui_utils.is_new_user():
            self.ui.start_sam_btn.setEnabled(False)
        self.userToEdit = None



        # Social buttons #
        self.hackzorURL = "https://www.hackzor.de"
        self.gitURL = "https://www.github.com/sera619"
        self.ytURL = "https://www.youtube.com/channel/UCJLXwZV5Kk4XRF6TSY_iPgQ"
        self.codepenURL = "https://codepen.io/sera619"
        self.mailURL = "mailto:seraphinus619@gmail.com"
        self.ui.social_codepen_btn.clicked.connect(lambda: webbrowser.open_new_tab(self.codepenURL))
        self.ui.social_git_btn.clicked.connect(lambda: webbrowser.open_new_tab(self.gitURL))
        self.ui.social_hackzor_btn.clicked.connect(lambda: webbrowser.open_new_tab(self.hackzorURL))
        self.ui.social_yt_btn.clicked.connect(lambda: webbrowser.open_new_tab(self.ytURL))
        self.ui.social_mail_btn.clicked.connect(lambda: webbrowser.open_new_tab(self.mailURL))
        ##############################################################################################

        self.ui.skills_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.skills_page))
        self.ui.dialog_cancel_btn.clicked.connect(lambda: self.edit_user_page())
        self.ui.dialog_ok_btn.clicked.connect(lambda: self.accept_delete())
        self.ui.menu_help_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.info_page))
        self.ui.edit_del_btn.clicked.connect(lambda: self.delete_user())
        self.ui.newuser_create_btn.clicked.connect(lambda: self.createNewUser())
        self.ui.x_button.clicked.connect(lambda: self.closeWindow())
        self.ui.mini_button.clicked.connect(lambda: self.showMinimized())
        self.ui.start_sam_btn.clicked.connect(lambda: self.start_sam())
        self.ui.users_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.user_page))
        self.ui.home_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))
        self.ui.create_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.new_user_page))
        self.ui.newuser_cancel_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))
        self.ui.edit_canel_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))
        self.ui.edit_update_btn.clicked.connect(lambda: self.update_user())
        self.ui.home_user_list.itemClicked.connect(lambda: self.edit_user_page())
        self.ui.home_help_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.info_page))

        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        self.update_userlist()
        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.top_frame.mouseMoveEvent = moveWindow
        


    def edit_user_page(self):
        user = self.ui.home_user_list.currentItem().text()
        self.userToEdit = user
        logger.debug('\nUser to edit: ' + user)
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_edit_page)
        self.ui.name_edit_input.setText(user)
        self.ui.phone_edit_input.setText(self.ui_utils.get_user_number(user))
        self.ui.edit_gender_box.setCurrentIndex(self.ui_utils.get_gender(user))
        self.ui.edit_guest_check.setChecked(self.ui_utils.is_user_guest(user))
        self.ui.edit_user_lang.setCurrentIndex(self.ui_utils.get_user_lang(user))
        self.ui.mail_edit_input.setText(self.ui_utils.get_user_mail(user))


    def delete_user(self):
        user = self.ui.home_user_list.currentItem().text()
        self.ui.dialog_text_label.setText('Möchstest du den Benutzer: '+ str(user) + ' wirklich löschen?')
        self.ui.stackedWidget.setCurrentWidget(self.ui.dialog_page)

    def accept_delete(self):
        self.ui_utils.delete_user(self.userToEdit)
        self.userToEdit = None

    def update_user(self):
        updated_username = self.ui.name_edit_input.text()
        updated_number = self.ui.phone_edit_input.text()
        updated_gender = self.ui.edit_gender_box.currentText()
        updated_lang = self.ui.edit_user_lang.currentText()
        updated_permission = self.ui.edit_guest_check.isChecked()
        updated_mail =  self.ui.mail_edit_input.text()
        self.ui_utils.edit_number(self.userToEdit, updated_number)
        self.ui_utils.edit_lang(self.userToEdit, updated_lang)
        self.ui_utils.edit_gender(self.userToEdit, updated_gender)
        self.ui_utils.edit_permissions(self.userToEdit, updated_permission)
        self.ui_utils.edit_mail(self.userToEdit, updated_mail)
        self.ui_utils.edit_name(self.userToEdit, updated_username)
        self.ui_utils.edit_number(self.userToEdit, updated_number)
        self.ui.edit_error_label.setText("Benutzer erfolgreich aktualisiert")
        self.update_userlist()
        time.sleep(1.5)
        self.userToEdit = None
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)

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
        logger.debug("\nUser {} created".format(new_username))
        self.update_userlist()
    
    def update_userlist(self):
        self.ui.home_user_list.clear()
        if self.ui_utils.is_new_user():
            self.ui.start_sam_btn.setEnabled(False)
        else:
            self.ui.start_sam_btn.setEnabled(True)
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