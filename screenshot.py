'''
Author: MasterYip 2205929492@qq.com
Date: 2022-12-19 16:53:52
LastEditors: MasterYip 2205929492@qq.com
LastEditTime: 2023-05-07 09:43:45
FilePath: \comprehensive-coding\FastImgNotingDown\screenshot.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
USE_PYSIDE6 = False
# import time
# from PySide6.QtGui import QPixmap
import cv2,numpy
from io import BytesIO
try:
    if USE_PYSIDE6==True:
        from PySide6.QtCore import Qt,Signal
        from PySide6.QtGui import QGuiApplication, QPalette, QPixmap, QBrush, QPainter, QPen, QImage
        from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
    else:
        raise Exception
except:
    from PyQt5.QtCore import Qt,pyqtSignal as Signal
    from PyQt5.QtGui import QGuiApplication, QPalette, QPixmap, QBrush, QPainter, QPen, QImage
    from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PIL import Image, ImageQt


class ScreenShotWidget(QWidget):
    GUI_MODE = False
    sigkeyhot = Signal(str)
    def __init__(self,parent=None):
        super(ScreenShotWidget ,self).__init__(parent)
        
        if self.GUI_MODE: self.show()
        
        # Settings
        self.invert_color = False
        
       
        
        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, Qt.lightGray)
        self.setPalette(self.palette)
        if USE_PYSIDE6:
            self.desk = QApplication.screens()[0]
            self.qrect = self.desk.size()
        else:
            self.desk = QApplication.desktop()
            self.qrect = self.desk.screenGeometry()
        self.setGeometry(20,20,200,200)
        self.pushbutton = QPushButton("开始截屏",self)
        self.pushbutton.setGeometry(30,30,160,20)
        self.state = 0
        self.state2 =0
        self.f = 0
        self.g = 0
        self.pushbutton.clicked.connect(self.start)
        self.setMouseTracking(True)
        
        self.label = QLabel()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.pushbutton)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        
    
    def start(self):
        self.state = 1
        self.hide()
        self.setGeometry(0,0,self.qrect.width(),self.qrect.height())
        # time.sleep(0.1)
        screen = QGuiApplication.primaryScreen()
        if USE_PYSIDE6:
            # TODO: This only support 1 screen situation
            self.p = QPixmap(screen.grabWindow(0,0,0,-1,-1))
        else:
            self.p = QPixmap(screen.grabWindow(self.desk.winId()))
        if self.invert_color:
            image = ImageQt.fromqpixmap(self.p)
            img = cv2.cvtColor(numpy.asarray(image),cv2.COLOR_RGB2BGR)
            img = cv2.bitwise_not(img)
            image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)) 
            output = BytesIO()
            image.save(output, 'BMP')
            data = output.getvalue()
            output.close()
            self.p = QPixmap(QImage.fromData(data))
        
        self.palette.setBrush(self.backgroundRole(),
                          QBrush(self.p))
        self.setPalette(self.palette)
        self.show()
        self.pushbutton.hide()
        self.label.hide()
    def mousePressEvent(self, e):
        if self.state == 1:
            self.a = e.globalX()
            self.b = e.globalY()
            self.state2 = 1
        else:
            pass
    def mouseMoveEvent(self, e):
        if (self.state == 1) & (self.state2 == 1):
            self.g = e.globalX()
            self.f = e.globalY()
            self.update()
    def paintEvent(self, e):
        if (self.state == 1) & (self.state2 == 1):
            paint = QPainter(self)
            paint.setPen(QPen(Qt.red, 4, Qt.SolidLine))
            if not paint.isActive():
                paint.begin(self)
            paint.drawRect(min(self.g, self.a), min(self.f, self.b),
                           abs(self.a - self.g), abs(self.b - self.f))
            paint.end()
    def mouseReleaseEvent(self, e):
        if self.state == 1 :
            self.state2 = 0
            self.c = e.globalX()
            self.d = e.globalY()
            clipboard = QApplication.clipboard()
            clipboard.clear()
            clipboard.setPixmap(self.p.copy(min(self.a,self.c),min(self.b,self.d),
                                            abs(self.c-self.a),abs(self.d-self.b)))
            self.state = 0
            if not self.GUI_MODE: self.hide()
            self.palette.setColor(QPalette.Window, Qt.lightGray)
            self.setPalette(self.palette)
            self.pushbutton.show()
            self.label.setPixmap(self.p.copy(min(self.a,self.c),min(self.b,self.d),
                                            abs(self.c-self.a),abs(self.d-self.b)))
            self.label.show()
            self.setGeometry(20,20, abs(self.c-self.a),abs(self.d-self.b))
            
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    wd = ScreenShotWidget()
    # wd.show()
    app.exec_()
