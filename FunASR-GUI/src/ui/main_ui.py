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
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTabWidget,
    QTextEdit, QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(830, 748)
        self.act_open_setting_file = QAction(MainWindow)
        self.act_open_setting_file.setObjectName(u"act_open_setting_file")
        self.act_open_setting_file.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_asr = QWidget()
        self.tab_asr.setObjectName(u"tab_asr")
        self.gridLayout_6 = QGridLayout(self.tab_asr)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget_2 = QTabWidget(self.tab_asr)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_single_asr = QWidget()
        self.tab_single_asr.setObjectName(u"tab_single_asr")
        self.widget = QWidget(self.tab_single_asr)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 781, 541))
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
        self.groupBox_2.setMinimumSize(QSize(300, 0))
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
        self.groupBox_3.setMaximumSize(QSize(200, 1200))
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

        self.btn_asr = QPushButton(self.tab_single_asr)
        self.btn_asr.setObjectName(u"btn_asr")
        self.btn_asr.setGeometry(QRect(330, 550, 81, 31))
        self.btn_asr_clear = QPushButton(self.tab_single_asr)
        self.btn_asr_clear.setObjectName(u"btn_asr_clear")
        self.btn_asr_clear.setGeometry(QRect(220, 550, 81, 31))
        self.tabWidget_2.addTab(self.tab_single_asr, "")
        self.tab_batch_asr = QWidget()
        self.tab_batch_asr.setObjectName(u"tab_batch_asr")
        self.btn_batch_asr = QPushButton(self.tab_batch_asr)
        self.btn_batch_asr.setObjectName(u"btn_batch_asr")
        self.btn_batch_asr.setGeometry(QRect(310, 550, 111, 31))
        self.widget2 = QWidget(self.tab_batch_asr)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(100, 0, 587, 541))
        self.verticalLayout_4 = QVBoxLayout(self.widget2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.combox_modelSelect_batch = QComboBox(self.widget2)
        self.combox_modelSelect_batch.addItem("")
        self.combox_modelSelect_batch.setObjectName(u"combox_modelSelect_batch")
        self.combox_modelSelect_batch.setFont(font1)

        self.verticalLayout_4.addWidget(self.combox_modelSelect_batch)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox_9 = QGroupBox(self.widget2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMaximumSize(QSize(250, 16777215))
        self.groupBox_11 = QGroupBox(self.groupBox_9)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(10, 30, 100, 60))
        self.groupBox_11.setMinimumSize(QSize(50, 60))
        self.groupBox_11.setMaximumSize(QSize(100, 80))
        self.gridLayout_7 = QGridLayout(self.groupBox_11)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.radiobtn_timestampY_batch_asr = QRadioButton(self.groupBox_11)
        self.radiobtn_timestampY_batch_asr.setObjectName(u"radiobtn_timestampY_batch_asr")

        self.gridLayout_7.addWidget(self.radiobtn_timestampY_batch_asr, 0, 0, 1, 1)

        self.radiobtn_timestampN_batch_asr = QRadioButton(self.groupBox_11)
        self.radiobtn_timestampN_batch_asr.setObjectName(u"radiobtn_timestampN_batch_asr")
        self.radiobtn_timestampN_batch_asr.setChecked(True)

        self.gridLayout_7.addWidget(self.radiobtn_timestampN_batch_asr, 0, 1, 1, 1)

        self.groupBox_12 = QGroupBox(self.groupBox_9)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(130, 30, 100, 60))
        self.groupBox_12.setMinimumSize(QSize(50, 60))
        self.groupBox_12.setMaximumSize(QSize(100, 80))
        self.gridLayout_8 = QGridLayout(self.groupBox_12)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.radiobtn_spkY_batch_asr = QRadioButton(self.groupBox_12)
        self.radiobtn_spkY_batch_asr.setObjectName(u"radiobtn_spkY_batch_asr")

        self.gridLayout_8.addWidget(self.radiobtn_spkY_batch_asr, 0, 0, 1, 1)

        self.radiobtn_spkN_batch_asr = QRadioButton(self.groupBox_12)
        self.radiobtn_spkN_batch_asr.setObjectName(u"radiobtn_spkN_batch_asr")
        self.radiobtn_spkN_batch_asr.setChecked(True)

        self.gridLayout_8.addWidget(self.radiobtn_spkN_batch_asr, 0, 1, 1, 1)


        self.horizontalLayout_6.addWidget(self.groupBox_9)

        self.groupBox_13 = QGroupBox(self.widget2)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radioBtn_batch_asrSaveTxtMode = QRadioButton(self.groupBox_13)
        self.radioBtn_batch_asrSaveTxtMode.setObjectName(u"radioBtn_batch_asrSaveTxtMode")
        self.radioBtn_batch_asrSaveTxtMode.setChecked(True)

        self.verticalLayout_3.addWidget(self.radioBtn_batch_asrSaveTxtMode)

        self.radioBtn_batch_asrSaveSrtMode = QRadioButton(self.groupBox_13)
        self.radioBtn_batch_asrSaveSrtMode.setObjectName(u"radioBtn_batch_asrSaveSrtMode")

        self.verticalLayout_3.addWidget(self.radioBtn_batch_asrSaveSrtMode)


        self.horizontalLayout_6.addWidget(self.groupBox_13)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.widget2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_batch_asr_inputDir = QLineEdit(self.widget2)
        self.lineEdit_batch_asr_inputDir.setObjectName(u"lineEdit_batch_asr_inputDir")
        self.lineEdit_batch_asr_inputDir.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_4.addWidget(self.lineEdit_batch_asr_inputDir)

        self.btn_batch_asr_inputDir_select = QPushButton(self.widget2)
        self.btn_batch_asr_inputDir_select.setObjectName(u"btn_batch_asr_inputDir_select")

        self.horizontalLayout_4.addWidget(self.btn_batch_asr_inputDir_select)

        self.btn_batch_asr_inputDir_open = QPushButton(self.widget2)
        self.btn_batch_asr_inputDir_open.setObjectName(u"btn_batch_asr_inputDir_open")

        self.horizontalLayout_4.addWidget(self.btn_batch_asr_inputDir_open)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.widget2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEdit_batch_asr_outputDir = QLineEdit(self.widget2)
        self.lineEdit_batch_asr_outputDir.setObjectName(u"lineEdit_batch_asr_outputDir")
        self.lineEdit_batch_asr_outputDir.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_5.addWidget(self.lineEdit_batch_asr_outputDir)

        self.btn_batch_asr_outputDir_select = QPushButton(self.widget2)
        self.btn_batch_asr_outputDir_select.setObjectName(u"btn_batch_asr_outputDir_select")

        self.horizontalLayout_5.addWidget(self.btn_batch_asr_outputDir_select)

        self.btn_batch_asr_outputDir_open = QPushButton(self.widget2)
        self.btn_batch_asr_outputDir_open.setObjectName(u"btn_batch_asr_outputDir_open")

        self.horizontalLayout_5.addWidget(self.btn_batch_asr_outputDir_open)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.groupBox_14 = QGroupBox(self.widget2)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setMinimumSize(QSize(0, 400))
        self.plainTextEdit_batch_asr_result = QPlainTextEdit(self.groupBox_14)
        self.plainTextEdit_batch_asr_result.setObjectName(u"plainTextEdit_batch_asr_result")
        self.plainTextEdit_batch_asr_result.setGeometry(QRect(30, 30, 521, 280))
        self.plainTextEdit_batch_asr_result.setMinimumSize(QSize(0, 280))

        self.verticalLayout_4.addWidget(self.groupBox_14)

        self.tabWidget_2.addTab(self.tab_batch_asr, "")

        self.gridLayout_6.addWidget(self.tabWidget_2, 0, 0, 1, 1)

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
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.act_open_setting_file)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FunASR-GUI", None))
        self.act_open_setting_file.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u6587\u4ef6", None))
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
        self.btn_asr.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8bc6\u522b", None))
        self.btn_asr_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5185\u5bb9", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_single_asr), QCoreApplication.translate("MainWindow", u"\u5355\u8bed\u97f3\u8bc6\u522b", None))
        self.btn_batch_asr.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6279\u91cf\u8bc6\u522b", None))
        self.combox_modelSelect_batch.setItemText(0, QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u8bed\u97f3\u8bc6\u522b\u6a21\u578b", None))

        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\u6a21\u5f0f\u9009\u62e9", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\u8f8d", None))
        self.radiobtn_timestampY_batch_asr.setText(QCoreApplication.translate("MainWindow", u"\u662f", None))
        self.radiobtn_timestampN_batch_asr.setText(QCoreApplication.translate("MainWindow", u"\u5426", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"\u8bf4\u8bdd\u4eba\u533a\u5206", None))
        self.radiobtn_spkY_batch_asr.setText(QCoreApplication.translate("MainWindow", u"\u662f", None))
        self.radiobtn_spkN_batch_asr.setText(QCoreApplication.translate("MainWindow", u"\u5426", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u683c\u5f0f", None))
        self.radioBtn_batch_asrSaveTxtMode.setText(QCoreApplication.translate("MainWindow", u"txt\u6587\u672c\u683c\u5f0f", None))
        self.radioBtn_batch_asrSaveSrtMode.setText(QCoreApplication.translate("MainWindow", u"srt\u5b57\u5e55\u683c\u5f0f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u8bc6\u522b\u76ee\u5f55\uff1a", None))
        self.btn_batch_asr_inputDir_select.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u76ee\u5f55", None))
        self.btn_batch_asr_inputDir_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u76ee\u5f55", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u7ed3\u679c\u76ee\u5f55\uff1a", None))
        self.btn_batch_asr_outputDir_select.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u76ee\u5f55", None))
        self.btn_batch_asr_outputDir_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u76ee\u5f55", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u8bc6\u522b\u7ed3\u679c", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_batch_asr), QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u8bed\u97f3\u8bc6\u522b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_asr), QCoreApplication.translate("MainWindow", u"\u8bed\u97f3\u8bc6\u522b", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u8bbe\u7f6e", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u8fdb\u9636\u8bbe\u7f6e", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u97f3\u9891", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8bf4\u8bdd\u901f\u5ea6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tts), QCoreApplication.translate("MainWindow", u"\u8bed\u97f3\u5408\u6210", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_audioprocess), QCoreApplication.translate("MainWindow", u"\u97f3\u89c6\u9891\u5904\u7406", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_asrModelCompare), QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u5bf9\u6bd4", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

