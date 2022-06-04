import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from qt_material import apply_stylesheet
from circ_progress import ProgressCirc 

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(500, 500)
        self.setWindowTitle('Circular Progress Bar')
        self.setStyleSheet('background: transparent;')
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.button = QPushButton('close', self)
        self.button.setGeometry(QRect(0, 0, 400, 50))
        self.button.setStyleSheet('background: darkred;border: 1px solid black;')
        self.button.clicked.connect(self.close)
        self.container = QFrame()
        self.container.setStyleSheet("background-color: transparent;")
        self.layout = QVBoxLayout()

        # initialize progress bar
        self.progress = ProgressCirc()
        self.progress.value = 60
        self.progress.progress_rounded_cap = True
        self.progress.add_shadow(True)
        self.progress.setMinimumSize(self.progress.width, self.progress.height) 

        # add slider 
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,100)
        self.slider.setValue(0)
        self.slider.valueChanged.connect(self.change_value)

        # adding widgets to layout 
        self.layout.addWidget(self.progress, Qt.AlignCenter,Qt.AlignCenter)
        self.layout.addWidget(self.slider, Qt.AlignCenter,Qt.AlignCenter)
        self.layout.addWidget(self.button, Qt.AlignCenter,Qt.AlignCenter)

        # adding layout to container and center container 
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)



        self.show()
    
    def change_value(self, value):
        self.progress.setValue(value)
        

if __name__ == "__main__":
     app = QApplication(sys.argv)
     main = MainWindow()
     main.show()
     sys.exit(app.exec())