from interface import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import *
from PySide6 import *
import sys, os, time, datetime


class MainWindow(QMainWindow):
    def __init__(self ):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QApplication(sys.argv)
def main():
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Error: {}", e)
    except KeyboardInterrupt:
        print('\n\nProgram terminated by user.\n')
        sys.exit(0)
    finally:
        sys.exit(0)
