# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(644, 328)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_Save = QPushButton(self.centralwidget)
        self.pushButton_Save.setObjectName(u"pushButton_Save")
        self.pushButton_Save.setGeometry(QRect(440, 250, 75, 24))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 311, 271))
        self.horizontalLayoutWidget_17 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_17.setObjectName(u"horizontalLayoutWidget_17")
        self.horizontalLayoutWidget_17.setGeometry(QRect(20, 140, 271, 31))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_17)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.horizontalLayoutWidget_17)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setTextFormat(Qt.PlainText)
        self.label_5.setWordWrap(False)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.checkBox_2 = QCheckBox(self.horizontalLayoutWidget_17)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_5.addWidget(self.checkBox_2)

        self.horizontalLayoutWidget_18 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_18.setObjectName(u"horizontalLayoutWidget_18")
        self.horizontalLayoutWidget_18.setGeometry(QRect(20, 170, 271, 31))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_18)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.horizontalLayoutWidget_18)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setTextFormat(Qt.PlainText)
        self.label_6.setWordWrap(False)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.checkBox_3 = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_6.addWidget(self.checkBox_3)

        self.horizontalLayoutWidget_15 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_15.setObjectName(u"horizontalLayoutWidget_15")
        self.horizontalLayoutWidget_15.setGeometry(QRect(20, 80, 271, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget_15)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.PlainText)
        self.label_3.setWordWrap(False)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.spinBox_3 = QSpinBox(self.horizontalLayoutWidget_15)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(120)
        self.spinBox_3.setValue(40)

        self.horizontalLayout_3.addWidget(self.spinBox_3)

        self.horizontalLayoutWidget_13 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_13.setObjectName(u"horizontalLayoutWidget_13")
        self.horizontalLayoutWidget_13.setGeometry(QRect(20, 20, 271, 31))
        self.horizontalLayout_1 = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.label_1 = QLabel(self.horizontalLayoutWidget_13)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setTextFormat(Qt.PlainText)
        self.label_1.setWordWrap(False)

        self.horizontalLayout_1.addWidget(self.label_1)

        self.spinBox_1 = QSpinBox(self.horizontalLayoutWidget_13)
        self.spinBox_1.setObjectName(u"spinBox_1")
        self.spinBox_1.setMinimum(21)
        self.spinBox_1.setMaximum(801)
        self.spinBox_1.setSingleStep(2)
        self.spinBox_1.setValue(501)

        self.horizontalLayout_1.addWidget(self.spinBox_1)

        self.horizontalLayoutWidget_16 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_16.setObjectName(u"horizontalLayoutWidget_16")
        self.horizontalLayoutWidget_16.setGeometry(QRect(20, 110, 271, 31))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_16)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.horizontalLayoutWidget_16)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setWordWrap(False)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.checkBox_1 = QCheckBox(self.horizontalLayoutWidget_16)
        self.checkBox_1.setObjectName(u"checkBox_1")

        self.horizontalLayout_4.addWidget(self.checkBox_1)

        self.horizontalLayoutWidget_14 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_14.setObjectName(u"horizontalLayoutWidget_14")
        self.horizontalLayoutWidget_14.setGeometry(QRect(20, 50, 271, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_14)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.spinBox_2 = QSpinBox(self.horizontalLayoutWidget_14)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(10)
        self.spinBox_2.setValue(0)

        self.horizontalLayout_2.addWidget(self.spinBox_2)

        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(20, 230, 271, 31))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_1 = QLineEdit(self.horizontalLayoutWidget_7)
        self.lineEdit_1.setObjectName(u"lineEdit_1")

        self.horizontalLayout_7.addWidget(self.lineEdit_1)

        self.pushButton_1 = QPushButton(self.horizontalLayoutWidget_7)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.horizontalLayout_7.addWidget(self.pushButton_1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 200, 132, 29))
        self.label_8.setTextFormat(Qt.PlainText)
        self.label_8.setWordWrap(False)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(320, 10, 311, 61))
        self.horizontalLayoutWidget_19 = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_19.setObjectName(u"horizontalLayoutWidget_19")
        self.horizontalLayoutWidget_19.setGeometry(QRect(10, 20, 291, 31))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_19)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_19)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setTextFormat(Qt.PlainText)
        self.label_7.setWordWrap(False)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.checkBox_4 = QCheckBox(self.horizontalLayoutWidget_19)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_8.addWidget(self.checkBox_4)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(320, 70, 311, 181))
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 120, 291, 29))
        self.label_11.setFont(font)
        self.label_11.setTextFormat(Qt.PlainText)
        self.label_11.setWordWrap(False)
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 70, 291, 29))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setTextFormat(Qt.PlainText)
        self.label_10.setWordWrap(False)
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 20, 291, 29))
        self.label_9.setTextFormat(Qt.PlainText)
        self.label_9.setWordWrap(False)
        self.hotkey1_lineEdit = QLineEdit(self.groupBox_3)
        self.hotkey1_lineEdit.setObjectName(u"hotkey1_lineEdit")
        self.hotkey1_lineEdit.setGeometry(QRect(10, 50, 291, 20))
        self.hotkey2_lineEdit = QLineEdit(self.groupBox_3)
        self.hotkey2_lineEdit.setObjectName(u"hotkey2_lineEdit")
        self.hotkey2_lineEdit.setGeometry(QRect(10, 100, 291, 20))
        self.hotkey3_lineEdit = QLineEdit(self.groupBox_3)
        self.hotkey3_lineEdit.setObjectName(u"hotkey3_lineEdit")
        self.hotkey3_lineEdit.setGeometry(QRect(10, 150, 291, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 644, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NoteProcessor", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip(QCoreApplication.translate("MainWindow", u"Author: Master Yip", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.pushButton_Save.setStatusTip(QCoreApplication.translate("MainWindow", u"Save the settings", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_Save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Image Enhancement", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Shape Correction", None))
#if QT_CONFIG(statustip)
        self.checkBox_2.setStatusTip(QCoreApplication.translate("MainWindow", u"Try homography projection when the region of interest is not facing upward precisely", None))
#endif // QT_CONFIG(statustip)
        self.checkBox_2.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Bkg Color Adapt", None))
#if QT_CONFIG(statustip)
        self.checkBox_3.setStatusTip(QCoreApplication.translate("MainWindow", u"Adapt background color. (e.g. blackboard)", None))
#endif // QT_CONFIG(statustip)
        self.checkBox_3.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Threshold Bias", None))
#if QT_CONFIG(statustip)
        self.spinBox_3.setStatusTip(QCoreApplication.translate("MainWindow", u"Adaptive threshold bias", None))
#endif // QT_CONFIG(statustip)
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"AdpThresh dia.", None))
#if QT_CONFIG(statustip)
        self.spinBox_1.setStatusTip(QCoreApplication.translate("MainWindow", u"Adaptive threshold diameter(pixel)", None))
#endif // QT_CONFIG(statustip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Color Retaining", None))
#if QT_CONFIG(statustip)
        self.checkBox_1.setStatusTip(QCoreApplication.translate("MainWindow", u"Retain color in image", None))
#endif // QT_CONFIG(statustip)
        self.checkBox_1.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Dilate rad.", None))
#if QT_CONFIG(statustip)
        self.spinBox_2.setStatusTip(QCoreApplication.translate("MainWindow", u"Handwriting dilate", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.lineEdit_1.setStatusTip(QCoreApplication.translate("MainWindow", u"Images batch processing folder", None))
#endif // QT_CONFIG(statustip)
        self.lineEdit_1.setText(QCoreApplication.translate("MainWindow", u"E:\\Temp\\img", None))
        self.lineEdit_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Img Folder", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"Exec", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Batch Processing", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Screen Shot Tool", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Inversion Adapt", None))
#if QT_CONFIG(statustip)
        self.checkBox_4.setStatusTip(QCoreApplication.translate("MainWindow", u"Adapt color inversion.", None))
#endif // QT_CONFIG(statustip)
        self.checkBox_4.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Hotkeys", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"ScreenShot", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Batch Processing", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Image Enhancement", None))
#if QT_CONFIG(statustip)
        self.hotkey1_lineEdit.setStatusTip(QCoreApplication.translate("MainWindow", u"Press the keys combination to set a new hotkey for Image Enhancement", None))
#endif // QT_CONFIG(statustip)
        self.hotkey1_lineEdit.setPlaceholderText("")
#if QT_CONFIG(statustip)
        self.hotkey2_lineEdit.setStatusTip(QCoreApplication.translate("MainWindow", u"Press the keys combination to set a new hotkey for Batch Processing", None))
#endif // QT_CONFIG(statustip)
        self.hotkey2_lineEdit.setPlaceholderText("")
#if QT_CONFIG(statustip)
        self.hotkey3_lineEdit.setStatusTip(QCoreApplication.translate("MainWindow", u"Press the keys combination to set a new hotkey for ScreenShot", None))
#endif // QT_CONFIG(statustip)
        self.hotkey3_lineEdit.setPlaceholderText("")
#if QT_CONFIG(statustip)
        self.statusbar.setStatusTip("")
#endif // QT_CONFIG(statustip)
    # retranslateUi

