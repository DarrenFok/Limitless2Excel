# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStackedWidget,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 400)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: #2a2a2a;\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color: #2a2a2a;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 0, 731, 341))
        self.startPage = QWidget()
        self.startPage.setObjectName(u"startPage")
        self.programTitle = QLabel(self.startPage)
        self.programTitle.setObjectName(u"programTitle")
        self.programTitle.setGeometry(QRect(190, 50, 361, 61))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(36)
        font.setBold(True)
        self.programTitle.setFont(font)
        self.programTitle.setStyleSheet(u"QLabel {\n"
"	color: #ffffff\n"
"}")
        self.programTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.linkPrompt = QLabel(self.startPage)
        self.linkPrompt.setObjectName(u"linkPrompt")
        self.linkPrompt.setGeometry(QRect(20, 170, 171, 21))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(14)
        font1.setItalic(False)
        self.linkPrompt.setFont(font1)
        self.linkPrompt.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"}")
        self.linkPrompt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.linkField = QLineEdit(self.startPage)
        self.linkField.setObjectName(u"linkField")
        self.linkField.setGeometry(QRect(200, 160, 421, 31))
        self.linkField.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(62, 62, 62);\n"
"}")
        self.confirmButton = QPushButton(self.startPage)
        self.confirmButton.setObjectName(u"confirmButton")
        self.confirmButton.setGeometry(QRect(630, 160, 81, 31))
        font2 = QFont()
        font2.setPointSize(9)
        self.confirmButton.setFont(font2)
        self.confirmButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(89, 89, 89);\n"
"	color: #ffffff;\n"
"	border-radius: 10px;\n"
"}")
        self.subtitle = QLabel(self.startPage)
        self.subtitle.setObjectName(u"subtitle")
        self.subtitle.setGeometry(QRect(150, 120, 441, 16))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(12)
        self.subtitle.setFont(font3)
        self.subtitle.setStyleSheet(u"QLabel {\n"
"	color: #ffffff\n"
"}")
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.versionNumber = QLabel(self.startPage)
        self.versionNumber.setObjectName(u"versionNumber")
        self.versionNumber.setGeometry(QRect(10, 320, 111, 16))
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setItalic(True)
        self.versionNumber.setFont(font4)
        self.versionNumber.setStyleSheet(u"QLabel{\n"
"	color: #ffffff\n"
"}")
        self.stackedWidget.addWidget(self.startPage)
        self.directorySelectPage = QWidget()
        self.directorySelectPage.setObjectName(u"directorySelectPage")
        self.currentLinkTitle = QLabel(self.directorySelectPage)
        self.currentLinkTitle.setObjectName(u"currentLinkTitle")
        self.currentLinkTitle.setGeometry(QRect(20, 60, 201, 41))
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(12)
        font5.setItalic(False)
        self.currentLinkTitle.setFont(font5)
        self.currentLinkTitle.setStyleSheet(u"QLabel{\n"
"color: #ffffff\n"
"}")
        self.currentLinkTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.confirmLabel = QLabel(self.directorySelectPage)
        self.confirmLabel.setObjectName(u"confirmLabel")
        self.confirmLabel.setGeometry(QRect(240, 60, 461, 41))
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(10)
        font6.setItalic(True)
        self.confirmLabel.setFont(font6)
        self.confirmLabel.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.saveInPrompt = QLabel(self.directorySelectPage)
        self.saveInPrompt.setObjectName(u"saveInPrompt")
        self.saveInPrompt.setGeometry(QRect(230, 150, 71, 16))
        self.saveInPrompt.setFont(font1)
        self.saveInPrompt.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.browseButton = QPushButton(self.directorySelectPage)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setGeometry(QRect(310, 140, 111, 31))
        self.browseButton.setFont(font3)
        self.browseButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(89, 89, 89);\n"
"	color: #ffffff;\n"
"	border-radius: 10px;\n"
"}")
        self.cancelButton = QPushButton(self.directorySelectPage)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(430, 140, 111, 31))
        self.cancelButton.setFont(font5)
        self.cancelButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(89, 89, 89);\n"
"	color: #ffffff;\n"
"	border-radius: 10px;\n"
"}")
        self.stackedWidget.addWidget(self.directorySelectPage)
        self.confirmationPage = QWidget()
        self.confirmationPage.setObjectName(u"confirmationPage")
        self.savedToPrompt = QLabel(self.confirmationPage)
        self.savedToPrompt.setObjectName(u"savedToPrompt")
        self.savedToPrompt.setGeometry(QRect(20, 70, 261, 31))
        self.savedToPrompt.setFont(font3)
        self.savedToPrompt.setStyleSheet(u"QLabel{\n"
"color: #ffffff\n"
"}")
        self.directoryEdit = QLabel(self.confirmationPage)
        self.directoryEdit.setObjectName(u"directoryEdit")
        self.directoryEdit.setGeometry(QRect(290, 69, 421, 31))
        self.directoryEdit.setFont(font6)
        self.directoryEdit.setStyleSheet(u"QLabel{\n"
"color: #ffffff;\n"
"}")
        self.whatNextPrompt = QLabel(self.confirmationPage)
        self.whatNextPrompt.setObjectName(u"whatNextPrompt")
        self.whatNextPrompt.setGeometry(QRect(240, 140, 281, 41))
        self.whatNextPrompt.setFont(font1)
        self.whatNextPrompt.setStyleSheet(u"QLabel{\n"
"color: #ffffff\n"
"}")
        self.whatNextPrompt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.createAnotherButton = QPushButton(self.confirmationPage)
        self.createAnotherButton.setObjectName(u"createAnotherButton")
        self.createAnotherButton.setGeometry(QRect(210, 190, 201, 31))
        font7 = QFont()
        font7.setFamilies([u"Roboto"])
        self.createAnotherButton.setFont(font7)
        self.createAnotherButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(89, 89, 89);\n"
"	color: #ffffff;\n"
"	border-radius: 10px;\n"
"}")
        self.closeProgramButton = QPushButton(self.confirmationPage)
        self.closeProgramButton.setObjectName(u"closeProgramButton")
        self.closeProgramButton.setGeometry(QRect(420, 190, 131, 31))
        font8 = QFont()
        font8.setFamilies([u"Roboto"])
        font8.setItalic(False)
        self.closeProgramButton.setFont(font8)
        self.closeProgramButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(89, 89, 89);\n"
"	color: #ffffff;\n"
"	border-radius: 10px;\n"
"}")
        self.stackedWidget.addWidget(self.confirmationPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 750, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Limitless2Excel", None))
        self.programTitle.setText(QCoreApplication.translate("MainWindow", u"Limitless2Excel", None))
        self.linkPrompt.setText(QCoreApplication.translate("MainWindow", u"Limitless TCG Link:", None))
        self.confirmButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.subtitle.setText(QCoreApplication.translate("MainWindow", u"An automatic .xlsx sheet generator for LimitlessTCG decklists", None))
        self.versionNumber.setText(QCoreApplication.translate("MainWindow", u"Version 0.2.0-beta.1", None))
        self.currentLinkTitle.setText(QCoreApplication.translate("MainWindow", u"Current LimitlessTCG Link:", None))
        self.confirmLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.saveInPrompt.setText(QCoreApplication.translate("MainWindow", u"Save As:", None))
        self.browseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.savedToPrompt.setText(QCoreApplication.translate("MainWindow", u"Deck .xlsx file successfully saved to:", None))
        self.directoryEdit.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.whatNextPrompt.setText(QCoreApplication.translate("MainWindow", u"What would you like to do next?", None))
        self.createAnotherButton.setText(QCoreApplication.translate("MainWindow", u"Create another .xlsx deck checklist", None))
        self.closeProgramButton.setText(QCoreApplication.translate("MainWindow", u"Close Program", None))
    # retranslateUi

