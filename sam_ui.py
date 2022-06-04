
from re import S
from loguru import logger
from scipy.__config__ import show
from interface import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect,QListWidgetItem, QWidget
from PySide6.QtCore import *
from PySide6 import QtGui
from PySide6 import *
from qt_material import apply_stylesheet
import sys, os, time, datetime, json
from ui_utils import UIutils
from MiniUI import Ui_MiniFrame
import main as SAM

app = QApplication(sys.argv)



class MiniUI(QWidget):
    def __init__(self):
        super(MiniUI, self).__init__()
        self.ui = Ui_MiniFrame()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.close)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.is_showing = False
    
    def closeWindow(self):
        self.close
        self.is_showing = False

    def showWindow(self):
        self.show()
        self.is_showing = True

class MainWindow(QMainWindow):
    def __init__(self ):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.miniui = MiniUI()
        self.ui.setupUi(self)
        self.SAM = SAM
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
        self.ui.newuser_error_label.setText("")
        itemsnew = ["Frau", "Mann"]
        langs = ["Deutsch", "Englisch"]
        self.ui.gender_combobox.addItems(itemsnew)
        self.ui.newuser_lang_box.addItems(langs)
        if self.ui_utils.is_new_user():
            self.ui.home_start_btn.setEnabled(False)
        self.ui.details_button.clicked.connect(lambda: self.animateMiniUI())
        self.userToEdit = None

        self.ui.newuser_create_btn.clicked.connect(lambda: self.createNewUser())
        self.ui.x_button.clicked.connect(lambda: self.closeWindow())
        self.ui.mini_button.clicked.connect(lambda: self.showMinimized())
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

    def animateMiniUI(self):        
        if self.miniui.is_showing:
            self.miniui.closeWindow()
        else:
            
            self.miniui.showWindow()
    

    def editUser(self,username):
        self.userToEdit = username
        self.ui.name_edit_input.setText(self.userToEdit)
        self.ui.stackedWidget.setCurrentWidget(self.ui.user_edit_page)


    def editUsername(self):
        self.userToEdit = None
        self.userToEdit = self.ui.home_user_list.currentItem().text()
        self.ui_utils.user_to_edit = self.userToEdit
        if self.ui.name_edit_input.text() != "":
            self.ui.name_edit_input.setText(self.userToEdit)
        self.ui_utils.edit_name = self.ui.name_edit_input.text()    


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
                #new_item.connect.isSelected(self.editUser(user))
                self.ui.home_user_list.itemClicked.connect(self.editUser(user))

    def reset_newuser(self):
        self.ui.new_username.setText("")
        self.ui.newuser_number.setText("")
        self.ui.guest_checker.setChecked(False)

    def start_sam(self):
        self.hide
        self.SAM.runSam()




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
