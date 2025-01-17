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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QStatusBar, QTabWidget, QTextEdit, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(978, 845)
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
        self.gridLayout_11 = QGridLayout(self.tab_single_asr)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.tab_single_asr)
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

        self.groupBox_2 = QGroupBox(self.tab_single_asr)
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

        self.groupBox_3 = QGroupBox(self.tab_single_asr)
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
        self.layoutWidget = QWidget(self.groupBox_asrSave)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(22, 31, 221, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_asrSavaDir = QLineEdit(self.layoutWidget)
        self.lineEdit_asrSavaDir.setObjectName(u"lineEdit_asrSavaDir")
        self.lineEdit_asrSavaDir.setMaximumSize(QSize(160, 16777215))

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


        self.gridLayout_11.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_asr_clear = QPushButton(self.tab_single_asr)
        self.btn_asr_clear.setObjectName(u"btn_asr_clear")

        self.horizontalLayout_7.addWidget(self.btn_asr_clear)

        self.btn_asr = QPushButton(self.tab_single_asr)
        self.btn_asr.setObjectName(u"btn_asr")

        self.horizontalLayout_7.addWidget(self.btn_asr)


        self.gridLayout_11.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_single_asr, "")
        self.tab_batch_asr = QWidget()
        self.tab_batch_asr.setObjectName(u"tab_batch_asr")
        self.gridLayout_10 = QGridLayout(self.tab_batch_asr)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.combox_modelSelect_batch = QComboBox(self.tab_batch_asr)
        self.combox_modelSelect_batch.addItem("")
        self.combox_modelSelect_batch.setObjectName(u"combox_modelSelect_batch")
        self.combox_modelSelect_batch.setFont(font1)

        self.verticalLayout_4.addWidget(self.combox_modelSelect_batch)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox_9 = QGroupBox(self.tab_batch_asr)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMaximumSize(QSize(250, 16777215))
        self.gridLayout_9 = QGridLayout(self.groupBox_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_11 = QGroupBox(self.groupBox_9)
        self.groupBox_11.setObjectName(u"groupBox_11")
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


        self.gridLayout_9.addWidget(self.groupBox_11, 0, 0, 1, 1)

        self.groupBox_12 = QGroupBox(self.groupBox_9)
        self.groupBox_12.setObjectName(u"groupBox_12")
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


        self.gridLayout_9.addWidget(self.groupBox_12, 0, 1, 1, 1)


        self.horizontalLayout_6.addWidget(self.groupBox_9)

        self.groupBox_13 = QGroupBox(self.tab_batch_asr)
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
        self.label_3 = QLabel(self.tab_batch_asr)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_batch_asr_inputDir = QLineEdit(self.tab_batch_asr)
        self.lineEdit_batch_asr_inputDir.setObjectName(u"lineEdit_batch_asr_inputDir")
        self.lineEdit_batch_asr_inputDir.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_4.addWidget(self.lineEdit_batch_asr_inputDir)

        self.btn_batch_asr_inputDir_select = QPushButton(self.tab_batch_asr)
        self.btn_batch_asr_inputDir_select.setObjectName(u"btn_batch_asr_inputDir_select")

        self.horizontalLayout_4.addWidget(self.btn_batch_asr_inputDir_select)

        self.btn_batch_asr_inputDir_open = QPushButton(self.tab_batch_asr)
        self.btn_batch_asr_inputDir_open.setObjectName(u"btn_batch_asr_inputDir_open")

        self.horizontalLayout_4.addWidget(self.btn_batch_asr_inputDir_open)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.tab_batch_asr)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEdit_batch_asr_outputDir = QLineEdit(self.tab_batch_asr)
        self.lineEdit_batch_asr_outputDir.setObjectName(u"lineEdit_batch_asr_outputDir")
        self.lineEdit_batch_asr_outputDir.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_5.addWidget(self.lineEdit_batch_asr_outputDir)

        self.btn_batch_asr_outputDir_select = QPushButton(self.tab_batch_asr)
        self.btn_batch_asr_outputDir_select.setObjectName(u"btn_batch_asr_outputDir_select")

        self.horizontalLayout_5.addWidget(self.btn_batch_asr_outputDir_select)

        self.btn_batch_asr_outputDir_open = QPushButton(self.tab_batch_asr)
        self.btn_batch_asr_outputDir_open.setObjectName(u"btn_batch_asr_outputDir_open")

        self.horizontalLayout_5.addWidget(self.btn_batch_asr_outputDir_open)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.groupBox_14 = QGroupBox(self.tab_batch_asr)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setMinimumSize(QSize(0, 400))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.plainTextEdit_batch_asr_result = QPlainTextEdit(self.groupBox_14)
        self.plainTextEdit_batch_asr_result.setObjectName(u"plainTextEdit_batch_asr_result")
        self.plainTextEdit_batch_asr_result.setMinimumSize(QSize(0, 280))

        self.verticalLayout_5.addWidget(self.plainTextEdit_batch_asr_result)

        self.btn_batch_asr = QPushButton(self.groupBox_14)
        self.btn_batch_asr.setObjectName(u"btn_batch_asr")

        self.verticalLayout_5.addWidget(self.btn_batch_asr)


        self.verticalLayout_4.addWidget(self.groupBox_14)


        self.gridLayout_10.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_batch_asr, "")

        self.gridLayout_6.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_asr, "")
        self.tab_tts = QWidget()
        self.tab_tts.setObjectName(u"tab_tts")
        self.gridLayout_12 = QGridLayout(self.tab_tts)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.tabWidget_3 = QTabWidget(self.tab_tts)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_single_tts = QWidget()
        self.tab_single_tts.setObjectName(u"tab_single_tts")
        self.groupBox_6 = QGroupBox(self.tab_single_tts)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 8, 320, 71))
        self.groupBox_6.setMinimumSize(QSize(320, 0))
        self.groupBox_6.setMaximumSize(QSize(320, 80))
        self.gridLayout_13 = QGridLayout(self.groupBox_6)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.combox_tts_model_select_single = QComboBox(self.groupBox_6)
        self.combox_tts_model_select_single.setObjectName(u"combox_tts_model_select_single")
        self.combox_tts_model_select_single.setMaximumSize(QSize(300, 30))

        self.gridLayout_13.addWidget(self.combox_tts_model_select_single, 0, 0, 1, 1)

        self.lab_tts_model_introduce = QLabel(self.tab_single_tts)
        self.lab_tts_model_introduce.setObjectName(u"lab_tts_model_introduce")
        self.lab_tts_model_introduce.setGeometry(QRect(10, 80, 320, 60))
        self.lab_tts_model_introduce.setMinimumSize(QSize(100, 60))
        self.lab_tts_model_introduce.setMaximumSize(QSize(320, 80))
        self.lab_tts_model_introduce.setTextFormat(Qt.TextFormat.AutoText)
        self.lab_tts_model_introduce.setWordWrap(True)
        self.groupBox_7 = QGroupBox(self.tab_single_tts)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(370, 0, 531, 141))
        self.gridLayout_14 = QGridLayout(self.groupBox_7)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.textEdit_tts_txtInput_single = QTextEdit(self.groupBox_7)
        self.textEdit_tts_txtInput_single.setObjectName(u"textEdit_tts_txtInput_single")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_tts_txtInput_single.sizePolicy().hasHeightForWidth())
        self.textEdit_tts_txtInput_single.setSizePolicy(sizePolicy)

        self.gridLayout_14.addWidget(self.textEdit_tts_txtInput_single, 0, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.tab_single_tts)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(10, 140, 891, 191))
        self.groupBox_15 = QGroupBox(self.groupBox_8)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(10, 20, 139, 161))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.radiobtn_mode_pretrainedvoice = QRadioButton(self.groupBox_15)
        self.radiobtn_mode_pretrainedvoice.setObjectName(u"radiobtn_mode_pretrainedvoice")

        self.verticalLayout_6.addWidget(self.radiobtn_mode_pretrainedvoice)

        self.radiobtn_mode_fastclone = QRadioButton(self.groupBox_15)
        self.radiobtn_mode_fastclone.setObjectName(u"radiobtn_mode_fastclone")

        self.verticalLayout_6.addWidget(self.radiobtn_mode_fastclone)

        self.radiobtn_mode_transclone = QRadioButton(self.groupBox_15)
        self.radiobtn_mode_transclone.setObjectName(u"radiobtn_mode_transclone")

        self.verticalLayout_6.addWidget(self.radiobtn_mode_transclone)

        self.radiobtn_mode_instruct = QRadioButton(self.groupBox_15)
        self.radiobtn_mode_instruct.setObjectName(u"radiobtn_mode_instruct")

        self.verticalLayout_6.addWidget(self.radiobtn_mode_instruct)

        self.groupBox_16 = QGroupBox(self.groupBox_8)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setGeometry(QRect(160, 20, 280, 161))
        self.gridLayout_15 = QGridLayout(self.groupBox_16)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.textEdit_guid = QTextEdit(self.groupBox_16)
        self.textEdit_guid.setObjectName(u"textEdit_guid")

        self.gridLayout_15.addWidget(self.textEdit_guid, 0, 0, 1, 1)

        self.groupBox_17 = QGroupBox(self.groupBox_8)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setGeometry(QRect(460, 20, 201, 71))
        self.gridLayout_16 = QGridLayout(self.groupBox_17)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.combox_pretrainedvoice_select = QComboBox(self.groupBox_17)
        self.combox_pretrainedvoice_select.setObjectName(u"combox_pretrainedvoice_select")

        self.gridLayout_16.addWidget(self.combox_pretrainedvoice_select, 0, 0, 1, 1)

        self.groupBox_18 = QGroupBox(self.groupBox_8)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setGeometry(QRect(710, 100, 110, 72))
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_18)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.radiobtn_streamY = QRadioButton(self.groupBox_18)
        self.radiobtn_streamY.setObjectName(u"radiobtn_streamY")

        self.horizontalLayout_8.addWidget(self.radiobtn_streamY)

        self.radiobtn_streamN = QRadioButton(self.groupBox_18)
        self.radiobtn_streamN.setObjectName(u"radiobtn_streamN")

        self.horizontalLayout_8.addWidget(self.radiobtn_streamN)

        self.groupBox_19 = QGroupBox(self.groupBox_8)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setGeometry(QRect(700, 20, 101, 70))
        self.gridLayout_17 = QGridLayout(self.groupBox_19)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.dSpinBox_speed_single = QDoubleSpinBox(self.groupBox_19)
        self.dSpinBox_speed_single.setObjectName(u"dSpinBox_speed_single")
        self.dSpinBox_speed_single.setMinimum(0.500000000000000)
        self.dSpinBox_speed_single.setMaximum(2.000000000000000)
        self.dSpinBox_speed_single.setSingleStep(0.100000000000000)
        self.dSpinBox_speed_single.setValue(1.000000000000000)

        self.gridLayout_17.addWidget(self.dSpinBox_speed_single, 0, 0, 1, 1)

        self.groupBox_20 = QGroupBox(self.groupBox_8)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setGeometry(QRect(460, 100, 219, 74))
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.spinBox_randInference_single = QSpinBox(self.groupBox_20)
        self.spinBox_randInference_single.setObjectName(u"spinBox_randInference_single")
        self.spinBox_randInference_single.setMinimum(-999999999)
        self.spinBox_randInference_single.setMaximum(999999999)

        self.horizontalLayout_9.addWidget(self.spinBox_randInference_single)

        self.btn_randGenerate_single = QPushButton(self.groupBox_20)
        self.btn_randGenerate_single.setObjectName(u"btn_randGenerate_single")

        self.horizontalLayout_9.addWidget(self.btn_randGenerate_single)

        self.groupBox_21 = QGroupBox(self.tab_single_tts)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setGeometry(QRect(10, 330, 901, 131))
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_21)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.groupBox_22 = QGroupBox(self.groupBox_21)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.gridLayout_18 = QGridLayout(self.groupBox_22)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_upload_prompt_audio_single = QPushButton(self.groupBox_22)
        self.btn_upload_prompt_audio_single.setObjectName(u"btn_upload_prompt_audio_single")
        self.btn_upload_prompt_audio_single.setMaximumSize(QSize(120, 80))

        self.horizontalLayout_10.addWidget(self.btn_upload_prompt_audio_single)

        self.label_prompt_audioname_single = QLabel(self.groupBox_22)
        self.label_prompt_audioname_single.setObjectName(u"label_prompt_audioname_single")
        self.label_prompt_audioname_single.setFont(font)
        self.label_prompt_audioname_single.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_prompt_audioname_single)


        self.gridLayout_18.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.groupBox_22)

        self.groupBox_23 = QGroupBox(self.groupBox_21)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.gridLayout_19 = QGridLayout(self.groupBox_23)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.textEdit_promptInput_single = QTextEdit(self.groupBox_23)
        self.textEdit_promptInput_single.setObjectName(u"textEdit_promptInput_single")

        self.gridLayout_19.addWidget(self.textEdit_promptInput_single, 0, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.groupBox_23)

        self.groupBox_24 = QGroupBox(self.tab_single_tts)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setGeometry(QRect(10, 460, 901, 121))
        self.gridLayout_20 = QGridLayout(self.groupBox_24)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.groupBox_25 = QGroupBox(self.groupBox_24)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.textEdit_instructInput_single = QTextEdit(self.groupBox_25)
        self.textEdit_instructInput_single.setObjectName(u"textEdit_instructInput_single")
        self.textEdit_instructInput_single.setGeometry(QRect(10, 30, 851, 41))

        self.gridLayout_20.addWidget(self.groupBox_25, 0, 0, 1, 1)

        self.groupBox_26 = QGroupBox(self.tab_single_tts)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.groupBox_26.setGeometry(QRect(20, 580, 391, 91))
        self.layoutWidget_3 = QWidget(self.groupBox_26)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 40, 231, 31))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_12.addWidget(self.label_5)

        self.lineEdit_ttsSavaDir = QLineEdit(self.layoutWidget_3)
        self.lineEdit_ttsSavaDir.setObjectName(u"lineEdit_ttsSavaDir")
        self.lineEdit_ttsSavaDir.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout_12.addWidget(self.lineEdit_ttsSavaDir)

        self.btn_ttsResultDirSelect = QPushButton(self.groupBox_26)
        self.btn_ttsResultDirSelect.setObjectName(u"btn_ttsResultDirSelect")
        self.btn_ttsResultDirSelect.setGeometry(QRect(280, 30, 89, 25))
        self.btn_ttsResultDirOpen = QPushButton(self.groupBox_26)
        self.btn_ttsResultDirOpen.setObjectName(u"btn_ttsResultDirOpen")
        self.btn_ttsResultDirOpen.setGeometry(QRect(280, 60, 89, 25))
        self.btn_tts = QPushButton(self.tab_single_tts)
        self.btn_tts.setObjectName(u"btn_tts")
        self.btn_tts.setGeometry(QRect(590, 610, 101, 41))
        self.tabWidget_3.addTab(self.tab_single_tts, "")
        self.tab_batch_tts = QWidget()
        self.tab_batch_tts.setObjectName(u"tab_batch_tts")
        self.tabWidget_3.addTab(self.tab_batch_tts, "")

        self.gridLayout_12.addWidget(self.tabWidget_3, 0, 1, 1, 1)

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
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)


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
        self.btn_asr_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5185\u5bb9", None))
        self.btn_asr.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8bc6\u522b", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_single_asr), QCoreApplication.translate("MainWindow", u"\u5355\u8bed\u97f3\u8bc6\u522b", None))
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
        self.btn_batch_asr.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6279\u91cf\u8bc6\u522b", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_batch_asr), QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u8bed\u97f3\u8bc6\u522b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_asr), QCoreApplication.translate("MainWindow", u"\u8bed\u97f3\u8bc6\u522b", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6a21\u578b", None))
        self.lab_tts_model_introduce.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u6a21\u578b\uff0c\u652f\u6301\u4e0e\u8bad\u7ec3\u963f\u8fbe\u788e\u7247\u52a0\u5927\u6253\u51fb\u554a\u554a\u5927\u5927\u8428\u5927\u5927\u963f\u65af\u963f\u65af\u5927\u5927\u554a\u963f\u8fbe\u4e3a\u5927\u8d5b\u963f\u9053\u7684\u5e74\u554a\u7684\u54e6\u662f\u554a\u7684\u54e6\u554a\u6211\u7684\u9a84\u50b2\u548c", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u5408\u6210\u6587\u672c", None))
        self.textEdit_tts_txtInput_single.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5927\u901f\u5ea6\u548c\u6211insnvdsiapdoaj\u554a\u7684\u5927\u5927\u5927\u8d5b\u963f\u8fbe\u4e09\u5927\u554a\u554a\u5927\u8d5b\u5de8\u5927\u5927\u5927\u7684\u5965\u55f2\u4e09\u5e26\u54e6\u5927\u5927\u8d5b\u7684\u54e6iadjad\u963f\u65af\u5230idasjd</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><b"
                        "r /></p></body></html>", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u914d\u7f6e", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"\u6a21\u5f0f\u9009\u62e9", None))
        self.radiobtn_mode_pretrainedvoice.setText(QCoreApplication.translate("MainWindow", u"\u9884\u8bad\u7ec3\u97f3\u8272", None))
        self.radiobtn_mode_fastclone.setText(QCoreApplication.translate("MainWindow", u"3s\u6781\u901f\u590d\u523b", None))
        self.radiobtn_mode_transclone.setText(QCoreApplication.translate("MainWindow", u"\u8de8\u8bed\u79cd\u590d\u523b", None))
        self.radiobtn_mode_instruct.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u7136\u8bed\u8a00\u63a7\u5236", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c\u6b65\u9aa4", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"\u9884\u8bad\u7ec3\u97f3\u8272\u9009\u62e9", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u6d41\u5f0f\u63a8\u7406", None))
        self.radiobtn_streamY.setText(QCoreApplication.translate("MainWindow", u"\u662f", None))
        self.radiobtn_streamN.setText(QCoreApplication.translate("MainWindow", u"\u5426", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6\u8c03\u8282", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"\u968f\u673a\u63a8\u7406\u79cd\u5b50", None))
        self.btn_randGenerate_single.setText(QCoreApplication.translate("MainWindow", u"\u968f\u673a", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"prompt\u914d\u7f6e", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u62e9prompt\u97f3\u9891\u6587\u4ef6", None))
        self.btn_upload_prompt_audio_single.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20", None))
        self.label_prompt_audioname_single.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u4e0a\u4f20\u9700\u8981\u8bc6\u522b\u7684\u97f3\u9891\u6587\u4ef6", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u5165prompt\u6587\u672c", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"instruct\u914d\u7f6e", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u5165instruct\u6587\u672c", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u4fdd\u5b58", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8def\u5f84\uff1a", None))
        self.btn_ttsResultDirSelect.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8def\u5f84", None))
        self.btn_ttsResultDirOpen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u8def\u5f84", None))
        self.btn_tts.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5408\u6210", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_single_tts), QCoreApplication.translate("MainWindow", u"\u5355\u8bed\u97f3\u5408\u6210", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_batch_tts), QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u8bed\u97f3\u5408\u6210", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tts), QCoreApplication.translate("MainWindow", u"\u8bed\u97f3\u5408\u6210", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_audioprocess), QCoreApplication.translate("MainWindow", u"\u97f3\u89c6\u9891\u5904\u7406", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_asrModelCompare), QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u5bf9\u6bd4", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

