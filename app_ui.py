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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(785, 440)
        mainWindow.setStyleSheet(u"QWidget{\n"
"border-radius: 16px;\n"
"}")
        self.titleBar = QWidget(mainWindow)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setGeometry(QRect(0, 0, 751, 41))
        self.titleBar.setStyleSheet(u"QWidget{\n"
"background-color: rgb(17, 17, 17);\n"
"border-top-left-radius: 16px;\n"
"border-top-right-radius: 16px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"}")
        self.windowName = QLabel(self.titleBar)
        self.windowName.setObjectName(u"windowName")
        self.windowName.setGeometry(QRect(300, 10, 151, 21))
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
        self.programTitle.setGeometry(QRect(200, 80, 361, 61))
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
        self.linkPrompt.setGeometry(QRect(30, 230, 171, 21))
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
        self.linkField.setGeometry(QRect(210, 220, 421, 31))
        self.linkField.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(62, 62, 62);\n"
"	border-radius: 12px;\n"
"	padding-left: 5px;\n"
"}")
        self.confirmButton = QPushButton(self.startPage)
        self.confirmButton.setObjectName(u"confirmButton")
        self.confirmButton.setGeometry(QRect(640, 220, 81, 31))
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
        self.subtitle.setGeometry(QRect(160, 150, 441, 21))
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
        self.horizontalLayoutWidget = QWidget(self.directorySelectPage)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(200, 220, 351, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.saveInPrompt = QLabel(self.horizontalLayoutWidget)
        self.saveInPrompt.setObjectName(u"saveInPrompt")
        self.saveInPrompt.setFont(font2)
        self.saveInPrompt.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.saveInPrompt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.saveInPrompt)

        self.browseButton = QPushButton(self.horizontalLayoutWidget)
        self.browseButton.setObjectName(u"browseButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseButton.sizePolicy().hasHeightForWidth())
        self.browseButton.setSizePolicy(sizePolicy)
        self.browseButton.setFont(font4)
        self.browseButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(89, 89, 89);\n"
"	color: #ffffff;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.browseButton)

        self.cancelButton = QPushButton(self.horizontalLayoutWidget)
        self.cancelButton.setObjectName(u"cancelButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy1)
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(12)
        font6.setItalic(False)
        self.cancelButton.setFont(font6)
        self.cancelButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(89, 89, 89);\n"
"	color: #ffffff;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.cancelButton)

        self.horizontalLayoutWidget_2 = QWidget(self.directorySelectPage)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(130, 150, 521, 31))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.currentLinkTitle = QLabel(self.horizontalLayoutWidget_2)
        self.currentLinkTitle.setObjectName(u"currentLinkTitle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.currentLinkTitle.sizePolicy().hasHeightForWidth())
        self.currentLinkTitle.setSizePolicy(sizePolicy2)
        self.currentLinkTitle.setFont(font6)
        self.currentLinkTitle.setStyleSheet(u"QLabel{\n"
"color: #ffffff\n"
"}")
        self.currentLinkTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.currentLinkTitle)

        self.confirmLabel = QLabel(self.horizontalLayoutWidget_2)
        self.confirmLabel.setObjectName(u"confirmLabel")
        font7 = QFont()
        font7.setFamilies([u"Roboto"])
        font7.setPointSize(10)
        font7.setItalic(True)
        self.confirmLabel.setFont(font7)
        self.confirmLabel.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"link: rgb(255, 255, 255);\n"
"visited: rgb(255, 255, 255);\n"
"background-color: rgb(62, 62, 62);\n"
"border-radius: 12px;\n"
"}")
        self.confirmLabel.setTextFormat(Qt.TextFormat.RichText)
        self.confirmLabel.setIndent(5)
        self.confirmLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextBrowserInteraction|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_4.addWidget(self.confirmLabel)

        self.stackedWidget.addWidget(self.directorySelectPage)
        self.confirmationPage = QWidget()
        self.confirmationPage.setObjectName(u"confirmationPage")
        self.confirmationPage.setStyleSheet(u"QWidget{\n"
"background-color: #2a2a2a;\n"
"}")
        self.verticalLayoutWidget = QWidget(self.confirmationPage)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(160, 190, 431, 81))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.whatNextPrompt = QLabel(self.verticalLayoutWidget)
        self.whatNextPrompt.setObjectName(u"whatNextPrompt")
        self.whatNextPrompt.setFont(font2)
        self.whatNextPrompt.setStyleSheet(u"QLabel{\n"
"color: #ffffff\n"
"}")
        self.whatNextPrompt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.whatNextPrompt)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.createAnotherButton = QPushButton(self.verticalLayoutWidget)
        self.createAnotherButton.setObjectName(u"createAnotherButton")
        sizePolicy.setHeightForWidth(self.createAnotherButton.sizePolicy().hasHeightForWidth())
        self.createAnotherButton.setSizePolicy(sizePolicy)
        font8 = QFont()
        font8.setFamilies([u"Roboto"])
        self.createAnotherButton.setFont(font8)
        self.createAnotherButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(89, 89, 89);\n"
"	color: #ffffff;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_11.addWidget(self.createAnotherButton)

        self.closeProgramButton = QPushButton(self.verticalLayoutWidget)
        self.closeProgramButton.setObjectName(u"closeProgramButton")
        sizePolicy1.setHeightForWidth(self.closeProgramButton.sizePolicy().hasHeightForWidth())
        self.closeProgramButton.setSizePolicy(sizePolicy1)
        self.closeProgramButton.setFont(font)
        self.closeProgramButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(89, 89, 89);\n"
"	color: #ffffff;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_11.addWidget(self.closeProgramButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayoutWidget_5 = QWidget(self.confirmationPage)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(30, 130, 691, 31))
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.savedToPrompt = QLabel(self.horizontalLayoutWidget_5)
        self.savedToPrompt.setObjectName(u"savedToPrompt")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.savedToPrompt.sizePolicy().hasHeightForWidth())
        self.savedToPrompt.setSizePolicy(sizePolicy3)
        font9 = QFont()
        font9.setFamilies([u"Roboto"])
        font9.setPointSize(10)
        self.savedToPrompt.setFont(font9)
        self.savedToPrompt.setStyleSheet(u"QLabel{\n"
"color: #ffffff\n"
"}")

        self.horizontalLayout_12.addWidget(self.savedToPrompt)

        self.directoryEdit = QLabel(self.horizontalLayoutWidget_5)
        self.directoryEdit.setObjectName(u"directoryEdit")
        self.directoryEdit.setFont(font7)
        self.directoryEdit.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"link: rgb(255, 255, 255);\n"
"background-color: rgb(62, 62, 62);\n"
"border-radius: 12px;\n"
"}")
        self.directoryEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.directoryEdit.setIndent(5)
        self.directoryEdit.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextBrowserInteraction|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_12.addWidget(self.directoryEdit)

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
        self.saveInPrompt.setText(QCoreApplication.translate("mainWindow", u"Save As:", None))
        self.browseButton.setText(QCoreApplication.translate("mainWindow", u"Browse", None))
        self.cancelButton.setText(QCoreApplication.translate("mainWindow", u"Cancel", None))
        self.currentLinkTitle.setText(QCoreApplication.translate("mainWindow", u"Current LimitlessTCG Link:", None))
        self.confirmLabel.setText(QCoreApplication.translate("mainWindow", u"\"<a style=\"color:white; text-decoration:none;\">Click Me</a>\"", None))
        self.whatNextPrompt.setText(QCoreApplication.translate("mainWindow", u"What would you like to do next?", None))
        self.createAnotherButton.setText(QCoreApplication.translate("mainWindow", u"Create another .xlsx deck checklist", None))
        self.closeProgramButton.setText(QCoreApplication.translate("mainWindow", u"Close Program", None))
        self.savedToPrompt.setText(QCoreApplication.translate("mainWindow", u"Deck .xlsx file successfully saved to:", None))
        self.directoryEdit.setText(QCoreApplication.translate("mainWindow", u"TextLabel", None))
    # retranslateUi

