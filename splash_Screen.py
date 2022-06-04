import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *

from mainui import Ui_MainWindow
from splashscreenui import Ui_Splash
from circ_progress import ProgressCirc
from userui import UserUI

counter = 0
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Splash()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.progress = ProgressCirc()
        self.progress.height = 480
        self.progress.width = 480
        self.progress.value = 80
        self.progress.font_size = 23
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.move(10,10)
        self.progress.setParent(self.ui.centralwidget)
        self.progress.add_shadow(True)
        self.progress.enable_bg = True
        self.progress.show()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(60)



        self.show()

    def update(self):
        global counter
        self.progress.setValue(counter)
        if counter >= 100:
            self.timer.stop()
            self.main = UserUI()
            self.main.show()
            self.close()
        counter += 1




class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = SplashScreen()
    
    sys.exit(app.exec())