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
        MainWindow.resize(771, 402)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 771, 341))
        self.startPage = QWidget()
        self.startPage.setObjectName(u"startPage")
        self.programTitle = QLabel(self.startPage)
        self.programTitle.setObjectName(u"programTitle")
        self.programTitle.setGeometry(QRect(230, 40, 321, 61))
        font = QFont()
        font.setPointSize(36)
        self.programTitle.setFont(font)
        self.linkPrompt = QLabel(self.startPage)
        self.linkPrompt.setObjectName(u"linkPrompt")
        self.linkPrompt.setGeometry(QRect(50, 170, 161, 21))
        font1 = QFont()
        font1.setPointSize(14)
        self.linkPrompt.setFont(font1)
        self.linkField = QLineEdit(self.startPage)
        self.linkField.setObjectName(u"linkField")
        self.linkField.setGeometry(QRect(210, 170, 411, 31))
        self.confirmButton = QPushButton(self.startPage)
        self.confirmButton.setObjectName(u"confirmButton")
        self.confirmButton.setGeometry(QRect(630, 170, 91, 31))
        self.confirmButton.setFont(font1)
        self.stackedWidget.addWidget(self.startPage)
        self.directorySelectPage = QWidget()
        self.directorySelectPage.setObjectName(u"directorySelectPage")
        self.currentLinkTitle = QLabel(self.directorySelectPage)
        self.currentLinkTitle.setObjectName(u"currentLinkTitle")
        self.currentLinkTitle.setGeometry(QRect(20, 60, 221, 41))
        self.currentLinkTitle.setFont(font1)
        self.confirmLabel = QLabel(self.directorySelectPage)
        self.confirmLabel.setObjectName(u"confirmLabel")
        self.confirmLabel.setGeometry(QRect(250, 70, 501, 31))
        self.saveInPrompt = QLabel(self.directorySelectPage)
        self.saveInPrompt.setObjectName(u"saveInPrompt")
        self.saveInPrompt.setGeometry(QRect(200, 150, 71, 16))
        self.saveInPrompt.setFont(font1)
        self.browseButton = QPushButton(self.directorySelectPage)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setGeometry(QRect(280, 140, 111, 31))
        self.browseButton.setFont(font1)
        self.cancelButton = QPushButton(self.directorySelectPage)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(400, 140, 111, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.cancelButton.setFont(font2)
        self.stackedWidget.addWidget(self.directorySelectPage)
        self.confirmationPage = QWidget()
        self.confirmationPage.setObjectName(u"confirmationPage")
        self.savedToPrompt = QLabel(self.confirmationPage)
        self.savedToPrompt.setObjectName(u"savedToPrompt")
        self.savedToPrompt.setGeometry(QRect(40, 70, 251, 31))
        self.savedToPrompt.setFont(font2)
        self.directoryEdit = QLabel(self.confirmationPage)
        self.directoryEdit.setObjectName(u"directoryEdit")
        self.directoryEdit.setGeometry(QRect(290, 80, 431, 20))
        self.whatNextPrompt = QLabel(self.confirmationPage)
        self.whatNextPrompt.setObjectName(u"whatNextPrompt")
        self.whatNextPrompt.setGeometry(QRect(240, 140, 281, 41))
        self.whatNextPrompt.setFont(font1)
        self.createAnotherButton = QPushButton(self.confirmationPage)
        self.createAnotherButton.setObjectName(u"createAnotherButton")
        self.createAnotherButton.setGeometry(QRect(160, 180, 201, 41))
        self.closeProgramButton = QPushButton(self.confirmationPage)
        self.closeProgramButton.setObjectName(u"closeProgramButton")
        self.closeProgramButton.setGeometry(QRect(400, 180, 191, 41))
        self.stackedWidget.addWidget(self.confirmationPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 771, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.programTitle.setText(QCoreApplication.translate("MainWindow", u"Limitless2Excel", None))
        self.linkPrompt.setText(QCoreApplication.translate("MainWindow", u"Limitless TCG Link:", None))
        self.confirmButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
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

