# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(605, 584)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 531, 471))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.combox_modelSelect = QComboBox(self.widget)
        self.combox_modelSelect.setObjectName(u"combox_modelSelect")

        self.verticalLayout.addWidget(self.combox_modelSelect)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_upload_audio = QPushButton(self.widget)
        self.btn_upload_audio.setObjectName(u"btn_upload_audio")
        self.btn_upload_audio.setMaximumSize(QSize(120, 80))

        self.horizontalLayout.addWidget(self.btn_upload_audio)

        self.label_audioname = QLabel(self.widget)
        self.label_audioname.setObjectName(u"label_audioname")

        self.horizontalLayout.addWidget(self.label_audioname)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.txtEdit_result = QTextEdit(self.widget)
        self.txtEdit_result.setObjectName(u"txtEdit_result")

        self.verticalLayout.addWidget(self.txtEdit_result)

        self.btn_asr = QPushButton(self.widget)
        self.btn_asr.setObjectName(u"btn_asr")

        self.verticalLayout.addWidget(self.btn_asr)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 605, 37))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_upload_audio.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20", None))
        self.label_audioname.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u4e0a\u4f20\u9700\u8981\u8bc6\u522b\u7684\u97f3\u9891\u6587\u4ef6", None))
        self.btn_asr.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8bc6\u522b", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u8bed\u97f3\u8bc6\u522b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8bed\u97f3\u5408\u6210", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u97f3\u89c6\u9891\u5904\u7406", None))
    # retranslateUi

