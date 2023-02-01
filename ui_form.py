# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1423, 857)
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.actionSetup = QAction(MainWindow)
        self.actionSetup.setObjectName(u"actionSetup")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSetMiasPath = QAction(MainWindow)
        self.actionSetMiasPath.setObjectName(u"actionSetMiasPath")
        self.actionSetMicoPath = QAction(MainWindow)
        self.actionSetMicoPath.setObjectName(u"actionSetMicoPath")
        self.actionSetMuaPath = QAction(MainWindow)
        self.actionSetMuaPath.setObjectName(u"actionSetMuaPath")
        self.actionSetLinkerPath = QAction(MainWindow)
        self.actionSetLinkerPath.setObjectName(u"actionSetLinkerPath")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalWidget_4 = QWidget(self.centralwidget)
        self.verticalWidget_4.setObjectName(u"verticalWidget_4")
        self.verticalWidget_4.setGeometry(QRect(0, 0, 1241, 781))
        self.mainLayout = QVBoxLayout(self.verticalWidget_4)
        self.mainLayout.setObjectName(u"mainLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.verticalWidget_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.textEdit = QTextEdit(self.verticalWidget_4)
        self.textEdit.setObjectName(u"textEdit")
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(12)
        self.textEdit.setFont(font)

        self.verticalLayout_3.addWidget(self.textEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.verticalWidget_4)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.verticalWidget_4)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.verticalWidget_4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.verticalWidget_4)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.verticalWidget_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.verticalWidget_4)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.textEdit_2 = QTextEdit(self.verticalWidget_4)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.verticalLayout_2.addWidget(self.textEdit_2)

        self.label_2 = QLabel(self.verticalWidget_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.textEdit_3 = QTextEdit(self.verticalWidget_4)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.mainLayout.addLayout(self.horizontalLayout)

        self.label_5 = QLabel(self.verticalWidget_4)
        self.label_5.setObjectName(u"label_5")

        self.mainLayout.addWidget(self.label_5)

        self.textEdit_4 = QTextEdit(self.verticalWidget_4)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMinimumSize(QSize(0, 150))
        self.textEdit_4.setMaximumSize(QSize(16777215, 150))
        self.textEdit_4.setReadOnly(True)

        self.mainLayout.addWidget(self.textEdit_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1423, 25))
        self.menuOpen_File = QMenu(self.menubar)
        self.menuOpen_File.setObjectName(u"menuOpen_File")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOpen_File.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuOpen_File.addAction(self.actionOpen_File)
        self.menuOpen_File.addAction(self.actionAbout)
        self.menuOpen_File.addAction(self.actionExit)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionSetMiasPath)
        self.menuOptions.addAction(self.actionSetMicoPath)
        self.menuOptions.addAction(self.actionSetMuaPath)
        self.menuOptions.addAction(self.actionSetLinkerPath)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mide: Minimal ide for Minisys1a", None))
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.actionSetup.setText(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSetMiasPath.setText(QCoreApplication.translate("MainWindow", u"SetMiasPath", None))
        self.actionSetMicoPath.setText(QCoreApplication.translate("MainWindow", u"SetMicoPath", None))
        self.actionSetMuaPath.setText(QCoreApplication.translate("MainWindow", u"SetMuaPath", None))
        self.actionSetLinkerPath.setText(QCoreApplication.translate("MainWindow", u"SetLinkerPath", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"C source file", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MIDE", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Compile", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Link", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Assemble", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"asm output", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"coe output", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Log:", None))
        self.menuOpen_File.setTitle(QCoreApplication.translate("MainWindow", u"Open", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

