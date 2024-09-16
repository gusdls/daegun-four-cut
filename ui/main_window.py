# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
        MainWindow.setStyleSheet(u"")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setStyleSheet(u"QWidget {\n"
"	background-color: #FFEE93;\n"
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
"	background-color: #fff1a9;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: white;\n"
"	color: #FFEE93;\n"
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
        font1 = QFont()
        font1.setFamilies([u".AppleSystemUIFont"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.navCamera.setFont(font1)
        self.navCamera.setStyleSheet(u"")
        self.navCamera.setCheckable(True)
        self.navCamera.setChecked(True)
        self.navCamera.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.navCamera)

        self.navResult = QPushButton(self.sidebar)
        self.navResult.setObjectName(u"navResult")
        font2 = QFont()
        font2.setFamilies([u".AppleSystemUIFont"])
        font2.setPointSize(16)
        self.navResult.setFont(font2)
        self.navResult.setCheckable(True)
        self.navResult.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.navResult)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 328, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.startButton = QPushButton(self.sidebar)
        self.startButton.setObjectName(u"startButton")
        font3 = QFont()
        font3.setFamilies([u".AppleSystemUIFont"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.startButton.setFont(font3)
        self.startButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/assets/camera.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.startButton.setIcon(icon)
        self.startButton.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.startButton)


        self.gridLayout_2.addWidget(self.sidebar, 0, 0, 1, 1)

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
        self.videoLabel = QLabel(self.cameraPage)
        self.videoLabel.setObjectName(u"videoLabel")
        font4 = QFont()
        font4.setPointSize(28)
        self.videoLabel.setFont(font4)
        self.videoLabel.setStyleSheet(u"color: white;")
        self.videoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.videoLabel, 0, 0, 1, 1)

        self.copyLabel = QLabel(self.cameraPage)
        self.copyLabel.setObjectName(u"copyLabel")
        self.copyLabel.setStyleSheet(u"color: black;")

        self.gridLayout_3.addWidget(self.copyLabel, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout_3.setRowStretch(0, 1)
        self.stackedWidget.addWidget(self.cameraPage)
        self.resultPage = QWidget()
        self.resultPage.setObjectName(u"resultPage")
        self.resultPage.setEnabled(True)
        self.gridLayout_4 = QGridLayout(self.resultPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.saveButton = QPushButton(self.resultPage)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setEnabled(True)
        self.saveButton.setMinimumSize(QSize(110, 40))
        self.saveButton.setMaximumSize(QSize(110, 40))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.saveButton.setFont(font5)
        self.saveButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #FFEE93;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #ffeb7f;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: darkgray;\n"
"}")
        self.saveButton.setCheckable(False)
        self.saveButton.setChecked(False)
        self.saveButton.setAutoExclusive(False)
        self.saveButton.setAutoDefault(False)
        self.saveButton.setFlat(False)

        self.gridLayout_4.addWidget(self.saveButton, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(617, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.widget = QWidget(self.resultPage)
        self.widget.setObjectName(u"widget")
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(9)
        self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.resultPage)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.gridLayout_2.addWidget(self.mainWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.saveButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logoLabel.setText("")
        self.navCamera.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.navResult.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Shot", None))
        self.videoLabel.setText("")
        self.copyLabel.setText(QCoreApplication.translate("MainWindow", u"\u00a9 2024 DaegunManga - All Rights Reserved.", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

