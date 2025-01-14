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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(808, 687)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_asr = QWidget()
        self.tab_asr.setObjectName(u"tab_asr")
        self.btn_asr_clear = QPushButton(self.tab_asr)
        self.btn_asr_clear.setObjectName(u"btn_asr_clear")
        self.btn_asr_clear.setGeometry(QRect(280, 540, 81, 31))
        self.btn_asr = QPushButton(self.tab_asr)
        self.btn_asr.setObjectName(u"btn_asr")
        self.btn_asr.setGeometry(QRect(380, 540, 81, 31))
        self.widget = QWidget(self.tab_asr)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(12, 2, 771, 531))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_upload_audio = QPushButton(self.groupBox)
        self.btn_upload_audio.setObjectName(u"btn_upload_audio")
        self.btn_upload_audio.setMaximumSize(QSize(120, 80))

        self.horizontalLayout.addWidget(self.btn_upload_audio)

        self.label_audioname = QLabel(self.groupBox)
        self.label_audioname.setObjectName(u"label_audioname")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        self.label_audioname.setFont(font)
        self.label_audioname.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_audioname)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.combox_modelSelect = QComboBox(self.groupBox)
        self.combox_modelSelect.addItem("")
        self.combox_modelSelect.setObjectName(u"combox_modelSelect")
        font1 = QFont()
        font1.setItalic(True)
        self.combox_modelSelect.setFont(font1)

        self.gridLayout_2.addWidget(self.combox_modelSelect, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.txtEdit_result = QTextEdit(self.groupBox_2)
        self.txtEdit_result.setObjectName(u"txtEdit_result")
        self.txtEdit_result.setReadOnly(True)

        self.gridLayout_3.addWidget(self.txtEdit_result, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.groupBox_3 = QGroupBox(self.widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(300, 120))
        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 40, 100, 60))
        self.groupBox_4.setMinimumSize(QSize(50, 60))
        self.groupBox_4.setMaximumSize(QSize(100, 80))
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.radiobtn_timestampY = QRadioButton(self.groupBox_4)
        self.radiobtn_timestampY.setObjectName(u"radiobtn_timestampY")

        self.gridLayout_4.addWidget(self.radiobtn_timestampY, 0, 0, 1, 1)

        self.radiobtn_timestampN = QRadioButton(self.groupBox_4)
        self.radiobtn_timestampN.setObjectName(u"radiobtn_timestampN")
        self.radiobtn_timestampN.setChecked(True)

        self.gridLayout_4.addWidget(self.radiobtn_timestampN, 0, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(150, 40, 100, 60))
        self.groupBox_5.setMinimumSize(QSize(50, 60))
        self.groupBox_5.setMaximumSize(QSize(100, 80))
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.radiobtn_spkY = QRadioButton(self.groupBox_5)
        self.radiobtn_spkY.setObjectName(u"radiobtn_spkY")

        self.gridLayout_5.addWidget(self.radiobtn_spkY, 0, 0, 1, 1)

        self.radiobtn_spkN = QRadioButton(self.groupBox_5)
        self.radiobtn_spkN.setObjectName(u"radiobtn_spkN")
        self.radiobtn_spkN.setChecked(True)

        self.gridLayout_5.addWidget(self.radiobtn_spkN, 0, 1, 1, 1)

        self.frame = QFrame(self.groupBox_3)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(10, 120, 281, 251))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.groupBox_asrSave = QGroupBox(self.frame)
        self.groupBox_asrSave.setObjectName(u"groupBox_asrSave")
        self.groupBox_asrSave.setEnabled(False)
        self.groupBox_asrSave.setGeometry(QRect(10, 44, 261, 197))
        self.btn_asrResultDirSelect = QPushButton(self.groupBox_asrSave)
        self.btn_asrResultDirSelect.setObjectName(u"btn_asrResultDirSelect")
        self.btn_asrResultDirSelect.setGeometry(QRect(170, 100, 89, 25))
        self.groupBox_10 = QGroupBox(self.groupBox_asrSave)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(10, 80, 129, 106))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioBtn_asrSaveTxtMode = QRadioButton(self.groupBox_10)
        self.radioBtn_asrSaveTxtMode.setObjectName(u"radioBtn_asrSaveTxtMode")
        self.radioBtn_asrSaveTxtMode.setChecked(True)

        self.verticalLayout_2.addWidget(self.radioBtn_asrSaveTxtMode)

        self.radioBtn_asrSaveSrtMode = QRadioButton(self.groupBox_10)
        self.radioBtn_asrSaveSrtMode.setObjectName(u"radioBtn_asrSaveSrtMode")

        self.verticalLayout_2.addWidget(self.radioBtn_asrSaveSrtMode)

        self.btn_asrResultDirOpen = QPushButton(self.groupBox_asrSave)
        self.btn_asrResultDirOpen.setObjectName(u"btn_asrResultDirOpen")
        self.btn_asrResultDirOpen.setGeometry(QRect(170, 130, 89, 25))
        self.lab_asrSaveMessage = QLabel(self.groupBox_asrSave)
        self.lab_asrSaveMessage.setObjectName(u"lab_asrSaveMessage")
        self.lab_asrSaveMessage.setGeometry(QRect(10, 60, 241, 17))
        self.lab_asrSaveMessage.setFont(font1)
        self.widget1 = QWidget(self.groupBox_asrSave)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 30, 251, 27))
        self.horizontalLayout_3 = QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_asrSavaDir = QLineEdit(self.widget1)
        self.lineEdit_asrSavaDir.setObjectName(u"lineEdit_asrSavaDir")

        self.horizontalLayout_3.addWidget(self.lineEdit_asrSavaDir)

        self.chkbox_asrResultSave = QCheckBox(self.frame)
        self.chkbox_asrResultSave.setObjectName(u"chkbox_asrResultSave")
        self.chkbox_asrResultSave.setEnabled(True)
        self.chkbox_asrResultSave.setGeometry(QRect(10, 10, 121, 28))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setItalic(True)
        self.chkbox_asrResultSave.setFont(font2)

        self.horizontalLayout_2.addWidget(self.groupBox_3)

        self.tabWidget.addTab(self.tab_asr, "")
        self.tab_tts = QWidget()
        self.tab_tts.setObjectName(u"tab_tts")
        self.groupBox_7 = QGroupBox(self.tab_tts)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(20, 10, 601, 121))
        self.groupBox_8 = QGroupBox(self.tab_tts)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(20, 170, 621, 241))
        self.groupBox_6 = QGroupBox(self.groupBox_8)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(20, 30, 211, 111))
        self.label = QLabel(self.groupBox_6)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 67, 17))
        self.tabWidget.addTab(self.tab_tts, "")
        self.tab_audioprocess = QWidget()
        self.tab_audioprocess.setObjectName(u"tab_audioprocess")
        self.tabWidget.addTab(self.tab_audioprocess, "")
        self.tab_asrModelCompare = QWidget()
        self.tab_asrModelCompare.setObjectName(u"tab_asrModelCompare")
        self.tabWidget.addTab(self.tab_asrModelCompare, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 808, 27))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FunASR-GUI", None))
        self.btn_asr_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5185\u5bb9", None))
        self.btn_asr.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8bc6\u522b", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u8bbe\u7f6e", None))
        self.btn_upload_audio.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20", None))
        self.label_audioname.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u4e0a\u4f20\u9700\u8981\u8bc6\u522b\u7684\u97f3\u9891\u6587\u4ef6", None))
        self.combox_modelSelect.setItemText(0, QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u8bed\u97f3\u8bc6\u522b\u6a21\u578b", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u7ed3\u679c", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u8fdb\u9636\u8bbe\u7f6e", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\u8f8d", None))
        self.radiobtn_timestampY.setText(QCoreApplication.translate("MainWindow", u"\u662f", None))
        self.radiobtn_timestampN.setText(QCoreApplication.translate("MainWindow", u"\u5426", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u8bf4\u8bdd\u4eba\u533a\u5206", None))
        self.radiobtn_spkY.setText(QCoreApplication.translate("MainWindow", u"\u662f", None))
        self.radiobtn_spkN.setText(QCoreApplication.translate("MainWindow", u"\u5426", None))
        self.groupBox_asrSave.setTitle(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u7ed3\u679c\u4fdd\u5b58", None))
        self.btn_asrResultDirSelect.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8def\u5f84", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u683c\u5f0f", None))
        self.radioBtn_asrSaveTxtMode.setText(QCoreApplication.translate("MainWindow", u"txt\u6587\u672c\u683c\u5f0f", None))
        self.radioBtn_asrSaveSrtMode.setText(QCoreApplication.translate("MainWindow", u"srt\u5b57\u5e55\u683c\u5f0f", None))
        self.btn_asrResultDirOpen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u8def\u5f84", None))
        self.lab_asrSaveMessage.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8def\u5f84\uff1a", None))
        self.chkbox_asrResultSave.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u81ea\u52a8\u4fdd\u5b58", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_asr), QCoreApplication.translate("MainWindow", u"\u8bed\u97f3\u8bc6\u522b", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u8bbe\u7f6e", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u8fdb\u9636\u8bbe\u7f6e", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u97f3\u9891", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8bf4\u8bdd\u901f\u5ea6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tts), QCoreApplication.translate("MainWindow", u"\u8bed\u97f3\u5408\u6210", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_audioprocess), QCoreApplication.translate("MainWindow", u"\u97f3\u89c6\u9891\u5904\u7406", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_asrModelCompare), QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u5bf9\u6bd4", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
    # retranslateUi

