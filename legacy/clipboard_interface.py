'''
Author: MasterYip 2205929492@qq.com
Date: 2023-04-18 19:28:20
LastEditors: MasterYip 2205929492@qq.com
LastEditTime: 2023-05-04 17:46:15
FilePath: \comprehensive-coding\FastImgNotingDown\clipboard_interface.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
# coding: utf-8
# pip install pillow, 用Image模块操作图片文件
from PIL import Image, ImageGrab, ImageQt
# BytesIO是操作二进制数据的模块
from io import BytesIO
# pip install pywin32 (win32clipboard是操作剪贴板的模块)
# TODO:This is unstable
# import win32clipboard
from PyQt5.QtWidgets import QApplication
import cv2
import numpy

# clipboard to Img(PIL & cv2)
def grab_img():
    # 保存剪切板内图片
    im = ImageGrab.grabclipboard()
    if isinstance(im, Image.Image):
        print("Image: size : %s, mode: %s" % (im.size, im.mode))
        # im.save("C:\\Users\\37767\\Desktop\\grab_clipboard.jpg")
    elif im:
        # TODO:Multiple images?
        for filename in im:
            print("filename:%s" % filename)
            im = Image.open(filename)
    else:
        print("clipboard is empty")
    return im

def grab_img_cv2():
    # 保存剪切板内图片
    im = ImageGrab.grabclipboard()
    
    if isinstance(im, Image.Image):
        print("Image: size : %s, mode: %s" % (im.size, im.mode))
        # im.save("C:\\Users\\37767\\Desktop\\grab_clipboard.jpg")
    elif im:
        # TODO:Multiple images?
        for filename in im:
            print("filename:%s" % filename)
            im = Image.open(filename)
    else:
        print("clipboard is empty")
        
    if im:
        return cv2.cvtColor(numpy.asarray(im),cv2.COLOR_RGB2BGR)
    else:
        return None

# Img to clipboard
def send_msg_to_clip(type_data, msg):
    """
    操作剪贴板分四步：
    1. 打开剪贴板：OpenClipboard()
    2. 清空剪贴板，新的数据才好写进去：EmptyClipboard()
    3. 往剪贴板写入数据：SetClipboardData()
    4. 关闭剪贴板：CloseClipboard()

    :param type_data: 数据的格式，
    unicode字符通常是传 win32con.CF_UNICODETEXT
    :param msg: 要写入剪贴板的数据
    """
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(type_data, msg)
    win32clipboard.CloseClipboard()

def send_msg_to_clip_pyqt5(QPixmap_img):
    clipboard = QApplication.clipboard()
    clipboard.clear()
    # TODO:This works on python 3.9 while 3.8 not
    clipboard.setPixmap(QPixmap_img)

def paste_img_from_file(file_img):
    image = Image.open(file_img)
    send_msg_to_clip_pyqt5(ImageQt.toqpixmap(image))

def paste_img_cv2(img):
    image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)) 
    send_msg_to_clip_pyqt5(ImageQt.toqpixmap(image))
    
if __name__ == "__main__":
    # 图片路径，如果是当前路径，直接写文件名
    # windows路径要注意是 \，例：'D:\\t.jpg'
    # linux是 /，例: '~/t.jpg'
    # file_image = 'E:\\Temp\\img\\1.png'
    # paste_img(file_image)
    
    img = grab_img_cv2()
    if not img is None:
        cv2.imshow("OpenCV",img)  
        cv2.waitKey()