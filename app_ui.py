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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QStackedWidget, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(750, 411)
        mainWindow.setStyleSheet(u"QWidget{\n"
"border-radius: 16px;\n"
"}")
        self.titleBar = QWidget(mainWindow)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setGeometry(QRect(0, 0, 751, 41))
        self.titleBar.setStyleSheet(u"QWidget{\n"
"background-color: #2a2a2a;\n"
"}")
        self.windowName = QLabel(self.titleBar)
        self.windowName.setObjectName(u"windowName")
        self.windowName.setGeometry(QRect(300, 10, 151, 16))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setItalic(False)
        self.windowName.setFont(font)
        self.windowName.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.windowName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.closeButton = QPushButton(self.titleBar)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(710, 10, 31, 24))
        self.closeButton.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(89, 89, 89);\n"
"border-radius: 13px;\n"
"}")
        self.minimizeButton = QPushButton(self.titleBar)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setGeometry(QRect(670, 10, 31, 24))
        self.minimizeButton.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(89, 89, 89);\n"
"border-radius: 13px;\n"
"}")
        self.stackedWidget = QStackedWidget(mainWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 10, 751, 391))
        self.stackedWidget.setStyleSheet(u"")
        self.startPage = QWidget()
        self.startPage.setObjectName(u"startPage")
        self.startPage.setStyleSheet(u"QWidget{\n"
"background-color: #2a2a2a;\n"
"}")
        self.programTitle = QLabel(self.startPage)
        self.programTitle.setObjectName(u"programTitle")
        self.programTitle.setGeometry(QRect(190, 50, 361, 61))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(36)
        font1.setBold(True)
        self.programTitle.setFont(font1)
        self.programTitle.setStyleSheet(u"QLabel {\n"
"	color: #ffffff\n"
"}")
        self.programTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.linkPrompt = QLabel(self.startPage)
        self.linkPrompt.setObjectName(u"linkPrompt")
        self.linkPrompt.setGeometry(QRect(20, 170, 171, 21))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(14)
        font2.setItalic(False)
        self.linkPrompt.setFont(font2)
        self.linkPrompt.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"}")
        self.linkPrompt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.linkField = QLineEdit(self.startPage)
        self.linkField.setObjectName(u"linkField")
        self.linkField.setGeometry(QRect(200, 160, 421, 31))
        self.linkField.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(62, 62, 62);\n"
"	border-radius: 12px;\n"
"}")
        self.confirmButton = QPushButton(self.startPage)
        self.confirmButton.setObjectName(u"confirmButton")
        self.confirmButton.setGeometry(QRect(630, 160, 81, 31))
        font3 = QFont()
        font3.setPointSize(9)
        self.confirmButton.setFont(font3)
        self.confirmButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(89, 89, 89);\n"
"	color: #ffffff;\n"
"	border-radius: 10px;\n"
"}")
        self.subtitle = QLabel(self.startPage)
        self.subtitle.setObjectName(u"subtitle")
        self.subtitle.setGeometry(QRect(150, 120, 441, 21))
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(12)
        self.subtitle.setFont(font4)
        self.subtitle.setStyleSheet(u"QLabel {\n"
"	color: #ffffff\n"
"}")
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.versionNumber = QLabel(self.startPage)
        self.versionNumber.setObjectName(u"versionNumber")
        self.versionNumber.setGeometry(QRect(10, 360, 111, 16))
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setItalic(True)
        self.versionNumber.setFont(font5)
        self.versionNumber.setStyleSheet(u"QLabel{\n"
"	color: #ffffff\n"
"}")
        self.stackedWidget.addWidget(self.startPage)
        self.directorySelectPage = QWidget()
        self.directorySelectPage.setObjectName(u"directorySelectPage")
        self.directorySelectPage.setStyleSheet(u"QWidget{\n"
"background-color: #2a2a2a;\n"
"}")
        self.currentLinkTitle = QLabel(self.directorySelectPage)
        self.currentLinkTitle.setObjectName(u"currentLinkTitle")
        self.currentLinkTitle.setGeometry(QRect(20, 60, 201, 41))
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(12)
        font6.setItalic(False)
        self.currentLinkTitle.setFont(font6)
        self.currentLinkTitle.setStyleSheet(u"QLabel{\n"
"color: #ffffff\n"
"}")
        self.currentLinkTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.confirmLabel = QLabel(self.directorySelectPage)
        self.confirmLabel.setObjectName(u"confirmLabel")
        self.confirmLabel.setGeometry(QRect(240, 60, 461, 41))
        font7 = QFont()
        font7.setFamilies([u"Roboto"])
        font7.setPointSize(10)
        font7.setItalic(True)
        self.confirmLabel.setFont(font7)
        self.confirmLabel.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.saveInPrompt = QLabel(self.directorySelectPage)
        self.saveInPrompt.setObjectName(u"saveInPrompt")
        self.saveInPrompt.setGeometry(QRect(230, 150, 71, 16))
        self.saveInPrompt.setFont(font2)
        self.saveInPrompt.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.browseButton = QPushButton(self.directorySelectPage)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setGeometry(QRect(310, 140, 111, 31))
        self.browseButton.setFont(font4)
        self.browseButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(89, 89, 89);\n"
"	color: #ffffff;\n"
"	border-radius: 10px;\n"
"}")
        self.cancelButton = QPushButton(self.directorySelectPage)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(430, 140, 111, 31))
        self.cancelButton.setFont(font6)
        self.cancelButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(89, 89, 89);\n"
"	color: #ffffff;\n"
"	border-radius: 10px;\n"
"}")
        self.stackedWidget.addWidget(self.directorySelectPage)
        self.confirmationPage = QWidget()
        self.confirmationPage.setObjectName(u"confirmationPage")
        self.confirmationPage.setStyleSheet(u"QWidget{\n"
"background-color: #2a2a2a;\n"
"}")
        self.savedToPrompt = QLabel(self.confirmationPage)
        self.savedToPrompt.setObjectName(u"savedToPrompt")
        self.savedToPrompt.setGeometry(QRect(20, 70, 261, 31))
        self.savedToPrompt.setFont(font4)
        self.savedToPrompt.setStyleSheet(u"QLabel{\n"
"color: #ffffff\n"
"}")
        self.directoryEdit = QLabel(self.confirmationPage)
        self.directoryEdit.setObjectName(u"directoryEdit")
        self.directoryEdit.setGeometry(QRect(290, 69, 421, 31))
        self.directoryEdit.setFont(font7)
        self.directoryEdit.setStyleSheet(u"QLabel{\n"
"color: #ffffff;\n"
"}")
        self.whatNextPrompt = QLabel(self.confirmationPage)
        self.whatNextPrompt.setObjectName(u"whatNextPrompt")
        self.whatNextPrompt.setGeometry(QRect(240, 140, 281, 41))
        self.whatNextPrompt.setFont(font2)
        self.whatNextPrompt.setStyleSheet(u"QLabel{\n"
"color: #ffffff\n"
"}")
        self.whatNextPrompt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.createAnotherButton = QPushButton(self.confirmationPage)
        self.createAnotherButton.setObjectName(u"createAnotherButton")
        self.createAnotherButton.setGeometry(QRect(210, 190, 201, 31))
        font8 = QFont()
        font8.setFamilies([u"Roboto"])
        self.createAnotherButton.setFont(font8)
        self.createAnotherButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(89, 89, 89);\n"
"	color: #ffffff;\n"
"	border-radius: 10px;\n"
"}")
        self.closeProgramButton = QPushButton(self.confirmationPage)
        self.closeProgramButton.setObjectName(u"closeProgramButton")
        self.closeProgramButton.setGeometry(QRect(420, 190, 131, 31))
        self.closeProgramButton.setFont(font)
        self.closeProgramButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(89, 89, 89);\n"
"	color: #ffffff;\n"
"	border-radius: 10px;\n"
"}")
        self.stackedWidget.addWidget(self.confirmationPage)
        self.stackedWidget.raise_()
        self.titleBar.raise_()

        self.retranslateUi(mainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Form", None))
        self.windowName.setText(QCoreApplication.translate("mainWindow", u"Limitless2Excel", None))
        self.closeButton.setText(QCoreApplication.translate("mainWindow", u"x", None))
        self.minimizeButton.setText(QCoreApplication.translate("mainWindow", u"-", None))
        self.programTitle.setText(QCoreApplication.translate("mainWindow", u"Limitless2Excel", None))
        self.linkPrompt.setText(QCoreApplication.translate("mainWindow", u"Limitless TCG Link:", None))
        self.confirmButton.setText(QCoreApplication.translate("mainWindow", u"Confirm", None))
        self.subtitle.setText(QCoreApplication.translate("mainWindow", u"An automatic .xlsx sheet generator for LimitlessTCG decklists", None))
        self.versionNumber.setText(QCoreApplication.translate("mainWindow", u"Version 0.2.0-beta.1", None))
        self.currentLinkTitle.setText(QCoreApplication.translate("mainWindow", u"Current LimitlessTCG Link:", None))
        self.confirmLabel.setText(QCoreApplication.translate("mainWindow", u"TextLabel", None))
        self.saveInPrompt.setText(QCoreApplication.translate("mainWindow", u"Save As:", None))
        self.browseButton.setText(QCoreApplication.translate("mainWindow", u"Browse", None))
        self.cancelButton.setText(QCoreApplication.translate("mainWindow", u"Cancel", None))
        self.savedToPrompt.setText(QCoreApplication.translate("mainWindow", u"Deck .xlsx file successfully saved to:", None))
        self.directoryEdit.setText(QCoreApplication.translate("mainWindow", u"TextLabel", None))
        self.whatNextPrompt.setText(QCoreApplication.translate("mainWindow", u"What would you like to do next?", None))
        self.createAnotherButton.setText(QCoreApplication.translate("mainWindow", u"Create another .xlsx deck checklist", None))
        self.closeProgramButton.setText(QCoreApplication.translate("mainWindow", u"Close Program", None))
    # retranslateUi

