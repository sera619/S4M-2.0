
from turtle import width
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class ProgressCirc(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.value = 0
        self.height = 200
        self.width = 200
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = 0x00FFFF
        self.bgcolor = 0x111b2b
        self.max_value = 100
        self.font_size = 12
        self.suffix = "%"
        self.text_color = 0x00FFFF
        self.enable_shadow =True
        self.enable_bg = True
        self.resize(self.width, self.height)


    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self) 
            self.shadow.setBlurRadius(25)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 240, 255, 120))
            self.setGraphicsEffect(self.shadow)



    def setValue(self, value):
        self.value = value
        self.repaint() 


    def paintEvent(self, event):
        width = self.width - self.progress_width
        height = self.height -self.progress_width
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value


        # PAINT TEMPLATE
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)
        paint.setFont(QFont("Ethnocentric", self.font_size))

        rect = QRect(0,0,self.width,self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        # PAINT PROGRESS
        pen = QPen()
        pen.setWidth(self.progress_width)

        if self.enable_bg:
            pen.setColor(QColor(self.bgcolor))
            paint.setPen(pen)
            paint.drawArc(margin, margin, width, height, 0, 360 *16)

        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        pen.setColor(QColor(self.progress_color))
        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, -90 * 16, -value*16)

        # PAINT TEXT
        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")

        # YOU HAVE TO CLOSE PAINTER!
        paint.end()