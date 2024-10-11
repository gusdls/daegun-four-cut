# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1097, 613)
        font = QFont()
        font.setFamilies([u".AppleSystemUIFont"])
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"#MainWindow {\n"
"	background-color: #fcf5c7;\n"
"}")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainWidget = QWidget(self.centralwidget)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setStyleSheet(u"QWidget#mainWidget {\n"
"	background: url(:/assets/background.png) no-repeat center;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.mainWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.mainWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"")
        self.cameraPage = QWidget()
        self.cameraPage.setObjectName(u"cameraPage")
        self.gridLayout_3 = QGridLayout(self.cameraPage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.cameraPage)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: black;")

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.videoLabel = QLabel(self.cameraPage)
        self.videoLabel.setObjectName(u"videoLabel")
        font1 = QFont()
        font1.setPointSize(28)
        self.videoLabel.setFont(font1)
        self.videoLabel.setStyleSheet(u"")
        self.videoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.videoLabel, 0, 0, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        self.stackedWidget.addWidget(self.cameraPage)
        self.selectPage = QWidget()
        self.selectPage.setObjectName(u"selectPage")
        self.selectPage.setEnabled(True)
        self.gridLayout_4 = QGridLayout(self.selectPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.selectButton = QPushButton(self.selectPage)
        self.selectButton.setObjectName(u"selectButton")
        self.selectButton.setEnabled(True)
        self.selectButton.setMinimumSize(QSize(110, 40))
        self.selectButton.setMaximumSize(QSize(110, 40))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.selectButton.setFont(font2)
        self.selectButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #B3C5D7;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: darkgray;\n"
"}")
        self.selectButton.setCheckable(False)
        self.selectButton.setChecked(False)
        self.selectButton.setAutoExclusive(False)
        self.selectButton.setAutoDefault(False)
        self.selectButton.setFlat(False)

        self.gridLayout_4.addWidget(self.selectButton, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(617, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.widget = QWidget(self.selectPage)
        self.widget.setObjectName(u"widget")
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.selectLayout = QGridLayout()
        self.selectLayout.setSpacing(9)
        self.selectLayout.setObjectName(u"selectLayout")

        self.gridLayout_5.addLayout(self.selectLayout, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.selectPage)
        self.resultPage = QWidget()
        self.resultPage.setObjectName(u"resultPage")
        self.gridLayout_6 = QGridLayout(self.resultPage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.resultPage)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QPushButton {\n"
"	background-color: #C5D5EA;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #B3C5D7;\n"
"}")
        self.gridLayout_8 = QGridLayout(self.widget_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.filterButton_1 = QPushButton(self.widget_2)
        self.filterButton_1.setObjectName(u"filterButton_1")
        self.filterButton_1.setMinimumSize(QSize(80, 80))
        self.filterButton_1.setMaximumSize(QSize(80, 80))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.filterButton_1.setFont(font3)
        self.filterButton_1.setCheckable(True)
        self.filterButton_1.setChecked(True)
        self.filterButton_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.filterButton_1)

        self.filterButton_2 = QPushButton(self.widget_2)
        self.filterButton_2.setObjectName(u"filterButton_2")
        self.filterButton_2.setMinimumSize(QSize(80, 80))
        self.filterButton_2.setMaximumSize(QSize(80, 80))
        self.filterButton_2.setFont(font3)
        self.filterButton_2.setCheckable(True)
        self.filterButton_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.filterButton_2)

        self.filterButton_3 = QPushButton(self.widget_2)
        self.filterButton_3.setObjectName(u"filterButton_3")
        self.filterButton_3.setMinimumSize(QSize(80, 80))
        self.filterButton_3.setMaximumSize(QSize(80, 80))
        self.filterButton_3.setFont(font3)
        self.filterButton_3.setCheckable(True)
        self.filterButton_3.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.filterButton_3)


        self.gridLayout_8.addLayout(self.verticalLayout_4, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget_2, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.resultPage)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.resultLabel = QLabel(self.widget_3)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.resultLabel, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget_3, 0, 1, 1, 1)

        self.widget_4 = QWidget(self.resultPage)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_7 = QGridLayout(self.widget_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.saveButton = QPushButton(self.widget_4)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(110, 40))
        self.saveButton.setMaximumSize(QSize(110, 40))
        self.saveButton.setFont(font2)
        self.saveButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #759EB8;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: darkgray;\n"
"}")

        self.gridLayout_7.addWidget(self.saveButton, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_2, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget_4, 0, 2, 1, 1)

        self.gridLayout_6.setColumnStretch(1, 1)
        self.stackedWidget.addWidget(self.resultPage)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.gridLayout_2.addWidget(self.mainWidget, 0, 1, 1, 1)

        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setStyleSheet(u"QWidget {\n"
"	background-color: #B3C5D7;\n"
"	padding-right: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: white;\n"
"	text-align: left;\n"
"	border: none;\n"
"	height: 30px;\n"
"	padding-left: 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#startButton {\n"
"	text-align: center;\n"
"	border-radius: 10px;\n"
"	margin-right: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #C5D5EA;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: white;\n"
"	color: #B3C5D7;\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.logoLabel = QLabel(self.sidebar)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setPixmap(QPixmap(u":/assets/logo.png"))

        self.verticalLayout_2.addWidget(self.logoLabel)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.navCamera = QPushButton(self.sidebar)
        self.navCamera.setObjectName(u"navCamera")
        font4 = QFont()
        font4.setFamilies([u".AppleSystemUIFont"])
        font4.setPointSize(16)
        font4.setBold(False)
        self.navCamera.setFont(font4)
        self.navCamera.setStyleSheet(u"")
        self.navCamera.setCheckable(True)
        self.navCamera.setChecked(True)
        self.navCamera.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.navCamera)

        self.navSelect = QPushButton(self.sidebar)
        self.navSelect.setObjectName(u"navSelect")
        font5 = QFont()
        font5.setFamilies([u".AppleSystemUIFont"])
        font5.setPointSize(16)
        self.navSelect.setFont(font5)
        self.navSelect.setCheckable(True)
        self.navSelect.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.navSelect)

        self.navResult = QPushButton(self.sidebar)
        self.navResult.setObjectName(u"navResult")
        font6 = QFont()
        font6.setPointSize(16)
        self.navResult.setFont(font6)
        self.navResult.setCheckable(True)
        self.navResult.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.navResult)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 328, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.startButton = QPushButton(self.sidebar)
        self.startButton.setObjectName(u"startButton")
        font7 = QFont()
        font7.setFamilies([u".AppleSystemUIFont"])
        font7.setPointSize(14)
        font7.setBold(True)
        self.startButton.setFont(font7)
        self.startButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/assets/camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startButton.setIcon(icon)
        self.startButton.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.startButton)


        self.gridLayout_2.addWidget(self.sidebar, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.selectButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u00a9 2024 DaegunManga - All Rights Reserved.", None))
        self.videoLabel.setText("")
        self.selectButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.filterButton_1.setText(QCoreApplication.translate("MainWindow", u"F1", None))
        self.filterButton_2.setText(QCoreApplication.translate("MainWindow", u"F2", None))
        self.filterButton_3.setText(QCoreApplication.translate("MainWindow", u"F3", None))
        self.resultLabel.setText("")
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.logoLabel.setText("")
        self.navCamera.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.navSelect.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.navResult.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Shot", None))
    # retranslateUi

