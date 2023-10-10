'''
Author: MasterYip 2205929492@qq.com
Date: 2022-12-30 09:31:06
LastEditors: MasterYip 2205929492@qq.com
LastEditTime: 2022-12-30 11:25:19
FilePath: \comprehensive-coding\miscellaneous\WLANtransfer.py
Description: 

Copyright (c) 2022 by MasterYip 2205929492@qq.com, All Rights Reserved. 
'''
import cv2
import numpy as np
import os
from glob import glob
from matplotlib.pyplot import imshow
# from __future__ import print_function
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
if is_admin():
    print('IS')
    # 将要运行的代码加到这里
    # dev_name = ''
    dir_name = '\\\\SFTR-MATE30\\Gallery\\Screenshots'

    if os.path.exists(dir_name):
        file_dirs = glob(dir_name+'\\*')
        file_dir = file_dirs[0]
        img = cv2.imdecode(np.fromfile(file_dir,dtype=np.uint8),-1)
        cv2.imshow('H',img)
        cv2.waitKey(0)
    else:
        print("No Device found.")

    ret = os.popen('netsh wlan start hostednetwork')
    print(ret.readlines())
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, 
                                        __file__, None, 1)


