'''
Author: MasterYip 2205929492@qq.com
Date: 2023-05-02 22:35:27
LastEditors: MasterYip 2205929492@qq.com
LastEditTime: 2023-05-07 11:56:21
FilePath: \comprehensive-coding\FastImgNotingDown\main.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
USE_PYSIDE6 = False

import glob
import os
import sys
from pathlib import Path

import note_color_threshold as nct
import cv2
import numpy as np
import logging
from io import BytesIO
from hotkeys import HotkeysMgr
# from system_hotkey import SystemHotkey
# from matplotlib.pyplot import imshow

from screenshot import ScreenShotWidget #TODO: Have to choose PySide6 or PyQt5 inside this file
if USE_PYSIDE6:
    from main_ui import *
    from PySide6.QtCore import Slot,QObject,Signal
    from PySide6.QtGui import QTextCursor, QAction, QIcon, QGuiApplication, QImage, QFont
    from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QMenu, QSystemTrayIcon
else: #PyQt5
    from main_ui_pyqt5 import *
    from PyQt5.QtCore import pyqtSlot as Slot,QObject,pyqtSignal as Signal, QMimeData
    from PyQt5.QtGui import QTextCursor, QIcon, QGuiApplication, QImage, QFont
    from PyQt5.QtWidgets import QAction, QApplication, QMainWindow, QMessageBox, QWidget, QMenu, QSystemTrayIcon
from PIL import Image, ImageGrab, ImageQt

# Directory Management
try:
    # Run in Terminal
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
except:
    # Run in ipykernel & interactive
    ROOT_DIR = os.getcwd()

# Logger
format_str = '%(asctime)s - %(name)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(funcName)s - %(message)s'
datefmt_str = "%y-%m-%d %H:%M:%S"
# Remove existing handlers for basicConfig to take effect.
# TODO: This may not be a good idea, because this will infect other modules.
root_logger = logging.getLogger()
for h in root_logger.handlers: root_logger.removeHandler(h)
logging.basicConfig(filename=os.path.join(ROOT_DIR,'log.txt'),
                    format = format_str,
                    datefmt= datefmt_str,
                    level=logging.INFO)

cil_handler = logging.StreamHandler(os.sys.stderr)#默认是sys.stderr
cil_handler.setLevel(logging.INFO) # TODO: 会被BasicConfig限制？(过滤树)
cil_handler.setFormatter(logging.Formatter(fmt=format_str, datefmt=datefmt_str))

global_logger = logging.getLogger('Global')
global_logger.addHandler(cil_handler)

class MyWindow(QMainWindow, Ui_MainWindow):
    textColors = ['FF5C5C','398AD9','5BEC8D','FD42AC','FF33FF','4B8200','DE87B8']
    sigkeyhot = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__()
        self.screenshot = ScreenShotWidget()
        self.setupUi(self)
        
        # Default Settings
        self.Folder_dir = 'E:\\Temp\\img'
        self.Thresh_dia = 501
        self.di_rad = 0
        self.bias = 40
        self.mode = 0
        self.auto_warp=False
        self.Black_board = False
        self.screenshot.invert_color = False
        
         # Hot key
        self.sigkeyhot.connect(self.hotkey_press_event)
        self.hotkeymgr = HotkeysMgr(self.sigkeyhot)
        self.hotkey_preset_dict = {"clipboard_img_process":('control','alt','c'),
                                   "folder_img_process":('control','alt','f'),
                                   "capture_hotkey":('alt','q')}
        # UI
        self._minimize_action = QAction()
        self._maximize_action = QAction()
        self._restore_action = QAction()
        self._quit_action = QAction()

        self._tray_icon = QSystemTrayIcon()
        self._tray_icon_menu = QMenu()
        
        # Note: Must before connect
        self.create_actions()
        self.create_tray_icon()
        
        self.pushButton_1.clicked.connect(self.folder_img_process)
        self.pushButton_Save.clicked.connect(self.setting_save)
        self._tray_icon.activated.connect(self.icon_activated)
        self.hotkey1_lineEdit.keyPressEvent = lambda x:self.hotkey_lineEdit_keyPressEvent(x,self.hotkey1_lineEdit)
        self.hotkey1_lineEdit.focusInEvent = lambda x:self.hotkeymgr.unregister_all()
        self.hotkey1_lineEdit.focusOutEvent = lambda x:self.hotkeymgr.register_all()
        self.hotkey1_lineEdit.setText("+".join(self.hotkey_preset_dict["clipboard_img_process"]))
        self.hotkey2_lineEdit.keyPressEvent = lambda x:self.hotkey_lineEdit_keyPressEvent(x,self.hotkey2_lineEdit)
        self.hotkey2_lineEdit.focusInEvent = lambda x:self.hotkeymgr.unregister_all()
        self.hotkey2_lineEdit.focusOutEvent = lambda x:self.hotkeymgr.register_all()
        self.hotkey2_lineEdit.setText("+".join(self.hotkey_preset_dict["folder_img_process"]))
        self.hotkey3_lineEdit.keyPressEvent = lambda x:self.hotkey_lineEdit_keyPressEvent(x,self.hotkey3_lineEdit)
        self.hotkey3_lineEdit.focusInEvent = lambda x:self.hotkeymgr.unregister_all()
        self.hotkey3_lineEdit.focusOutEvent = lambda x:self.hotkeymgr.register_all()
        self.hotkey3_lineEdit.setText("+".join(self.hotkey_preset_dict["capture_hotkey"]))
        # Icon
        self.icon_dict = {"icon":QIcon(os.path.join(ROOT_DIR,"img","icon.png")),
                          "icon_w":QIcon(os.path.join(ROOT_DIR,"img","icon_w.png")),
                          "icon_b":QIcon(os.path.join(ROOT_DIR,"img","icon_b.png"))}
        
        self.set_icon("icon")
        self._tray_icon.setVisible(True)
        self._tray_icon.setToolTip("FastImgNotingDown")
        self._tray_icon.show()
         
    def hotkey_press_event(self, i_str):
        if not self.hotkey1_lineEdit.hasFocus():
            global_logger.info("pressing: %s" % (i_str,))
            if i_str == "folder_img_process":
                self.folder_img_process()
            elif i_str == "clipboard_img_process":
                self.clipboard_img_process()
            elif i_str == "capture_hotkey":
                self.screenshot.start()
    
    def hotkey_lineEdit_keyPressEvent(self, QKeyEvent, lineEdit):
        key_list = []
        if QKeyEvent.key()<256:
            if QKeyEvent.modifiers() & Qt.ControlModifier: key_list.append('control')
            if QKeyEvent.modifiers() & Qt.ShiftModifier: key_list.append('shift')
            if QKeyEvent.modifiers() & Qt.AltModifier: key_list.append('alt')
            # key_list.append(QKeyEvent.text())
            key_list.append(chr(QKeyEvent.key()).lower())
            lineEdit.setText('+'.join(key_list))
            if lineEdit.objectName() == "hotkey1_lineEdit":
                self.hotkey_preset_dict["clipboard_img_process"] = tuple(key_list)
            if lineEdit.objectName() == "hotkey2_lineEdit":
                self.hotkey_preset_dict["folder_img_process"] = tuple(key_list)
            if lineEdit.objectName() == "hotkey3_lineEdit":
                self.hotkey_preset_dict["capture_hotkey"] = tuple(key_list)
    
    def setting_save(self):
        self.Folder_dir = self.lineEdit_1.text()
        self.Thresh_dia = self.spinBox_1.value()
        self.di_rad = self.spinBox_2.value()
        self.bias = self.spinBox_3.value()
        self.mode = self.checkBox_1.isChecked()
        self.auto_warp= self.checkBox_2.isChecked()
        self.Black_board = self.checkBox_3.isChecked()
        self.screenshot.invert_color = self.checkBox_4.isChecked()
        # Hotkey
        print(self.hotkey_preset_dict)
        self.hotkeymgr.set_hotkey("clipboard_img_process",self.hotkey_preset_dict["clipboard_img_process"])
        self.hotkeymgr.set_hotkey("folder_img_process",self.hotkey_preset_dict["folder_img_process"])
        self.hotkeymgr.set_hotkey("capture_hotkey",self.hotkey_preset_dict["capture_hotkey"])
  
    def create_actions(self):
        self._minimize_action = QAction("Minimize", self)
        self._minimize_action.triggered.connect(self.hide)

        self._maximize_action = QAction("Maximize", self)
        self._maximize_action.triggered.connect(self.showMaximized)

        self._restore_action = QAction("Restore", self)
        self._restore_action.triggered.connect(self.showNormal)

        self._quit_action = QAction("Quit", self)
        if USE_PYSIDE6:
            self._quit_action.triggered.connect(os._exit)
            # self._quit_action.triggered.connect(qApp.quit) #aApp macro in pyside6
        else:
            self._quit_action.triggered.connect(os._exit)
            # self._quit_action.triggered.connect(app.quit) #app macro in pyqt5
        
    def create_tray_icon(self):
        self._tray_icon_menu = QMenu(self)
        self._tray_icon_menu.addAction(self._minimize_action)
        self._tray_icon_menu.addAction(self._maximize_action)
        self._tray_icon_menu.addAction(self._restore_action)
        self._tray_icon_menu.addSeparator()
        self._tray_icon_menu.addAction(self._quit_action)

        self._tray_icon = QSystemTrayIcon(self)
        self._tray_icon.setContextMenu(self._tray_icon_menu)
        
    @Slot(int)
    def set_icon(self, index_key):
        icon = self.icon_dict[index_key]
        self._tray_icon.setIcon(icon)
        self.setWindowIcon(icon)
    
    def icon_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            pass
        if reason == QSystemTrayIcon.DoubleClick:
            self.showNormal()
        if reason == QSystemTrayIcon.MiddleClick:
            pass
        
    def closeEvent(self, event):
        if not event.spontaneous() or not self.isVisible():
            return
        if self._tray_icon.isVisible():
            # QMessageBox.information(self, "Systray",
            #                         "The program will keep running in the system tray. "
            #                         "To terminate the program, choose <b>Quit</b> in the context "
            #                         "menu of the system tray entry.")
            self.hide()
            event.ignore()
    
    def folder_img_process(self):
        self.Folder_dir = self.lineEdit_1.text()
        self.Thresh_dia = self.spinBox_1.value()
        self.di_rad = self.spinBox_2.value()
        self.bias = self.spinBox_3.value()
        self.mode = self.checkBox_1.isChecked()
        self.auto_warp= self.checkBox_2.isChecked()
        self.Black_board = self.checkBox_3.isChecked()
        
        # print(glob.glob(dir+'\\**\\*.jpg',recursive=True)) #全部搜索
        #注意 Linux为// Win为\\
        # file_dirs = glob.glob(Folder_dir+'\\*.jpg') +  glob.glob(Folder_dir+'\\*.png') #Win
        file_dirs = glob.glob(self.Folder_dir+'//*.jpg') +  glob.glob(self.Folder_dir+'//*.png')  #Linux

        for file_dir in file_dirs:
            file_name = Path(file_dir).stem
            if not ('Thresh_' in file_name):
                global_logger.info("Processing: " + file_name)
                # img = cv2.imread(file_dir)
                img = cv2.imdecode(np.fromfile(file_dir,dtype=np.uint8),-1) #可读取中文路径
                img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                if self.auto_warp: 
                    BR = nct.BlackboardRecorder(img)
                    if self.Black_board: src_points, dst_points, (dst_img_w, dst_img_h) = BR.find_possible_ROIs(BR.thresh_ivt)
                    else: src_points, dst_points, (dst_img_w, dst_img_h) = BR.find_possible_ROIs(BR.thresh)
                    img = BR.homography_projection(BR.img,src_points, dst_points, (dst_img_w, dst_img_h))
                if self.Black_board:
                    thresh = nct.note_color_threshold_for_black_bkg(img,dilate_rad=self.di_rad,Thresh_bias = self.bias,
                                                                    Thresh_dia=self.Thresh_dia,mode=self.mode)
                else: 
                    thresh = nct.note_color_threshold_for_white_bkg(img,dilate_rad=self.di_rad,Thresh_bias = self.bias,
                                                        Thresh_dia=self.Thresh_dia,mode=self.mode)
                cv2.imwrite(self.Folder_dir+'\\Thresh_'+file_name+'.png', thresh, [cv2.IMWRITE_PNG_COMPRESSION, 9])
        try:
            imshow(thresh)
        except:
            global_logger.warning("Img load failed.")
            pass
        os.startfile(self.Folder_dir)
    
    def paste_img_cv2(self, img):
        clipboard = QApplication.clipboard()
        clipboard.clear()
        image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)) 
        if USE_PYSIDE6:
            clipboard.setImage(ImageQt.toqimage(image))
        else: # TODO: Need to be fixed
            # 声明output字节对象
            output = BytesIO()
            # 用BMP (Bitmap) 格式存储
            # 这里是位图，然后用output字节对象来存储
            image.save(output, 'BMP')
            # BMP图片有14字节的header，需要额外去除(Qimage 不需要)
            # data = output.getvalue()[14:]
            data = output.getvalue()
            output.close()
            clipboard.setImage(QImage.fromData(data))
    
    def grab_img_cv2(self):
        # 保存剪切板内图片
        im = ImageGrab.grabclipboard()
        if isinstance(im, Image.Image):
            print("Image: size : %s, mode: %s" % (im.size, im.mode))
        elif im:
            # TODO:Multiple images?
            for filename in im:
                print("filename:%s" % filename)
                im = Image.open(filename)
        else: print("clipboard is empty")
        if im: return cv2.cvtColor(np.asarray(im),cv2.COLOR_RGB2BGR)
        else: return None
    
    def clipboard_img_process(self):
        # TODO:compress img to shrink size(save to tmp folder and copy from folder)
        self.set_icon("icon_b")
        img = self.grab_img_cv2()
        if not img is None:
            # No need to convert when read from clipboard
            # img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            if self.auto_warp:
                try:
                    BR = nct.BlackboardRecorder(img)
                    if self.Black_board: src_points, dst_points, (dst_img_w, dst_img_h) = BR.find_possible_ROIs(BR.thresh_ivt)
                    else: src_points, dst_points, (dst_img_w, dst_img_h) = BR.find_possible_ROIs(BR.thresh)
                    img = BR.homography_projection(BR.img,src_points, dst_points, (dst_img_w, dst_img_h))
                except:
                    global_logger.warning("Searching ROI failed, cancelling homography projection.")
            if self.Black_board:
                thresh = nct.note_color_threshold_for_black_bkg(img,dilate_rad=self.di_rad,Thresh_bias = self.bias,
                                                                Thresh_dia=self.Thresh_dia,mode=self.mode)
            else: 
                thresh = nct.note_color_threshold_for_white_bkg(img,dilate_rad=self.di_rad,Thresh_bias = self.bias,
                                                    Thresh_dia=self.Thresh_dia,mode=self.mode)
            self.paste_img_cv2(thresh)
        else:
            global_logger.info("No Img in clipboard.")
        self.set_icon("icon")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "Systray", "I couldn't detect any system tray on this system.")
        sys.exit(1)

    QApplication.setQuitOnLastWindowClosed(False)
    
    myWin = MyWindow()
    myWin.show()
    
    sys.exit(app.exec())


