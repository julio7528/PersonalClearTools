# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PersonalClearTools.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLayout, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QWidget)

class Ui_PersonalClearTools(object):
    def setupUi(self, PersonalClearTools):
        if not PersonalClearTools.objectName():
            PersonalClearTools.setObjectName(u"PersonalClearTools")
        PersonalClearTools.resize(600, 205)
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        PersonalClearTools.setFont(font)
        PersonalClearTools.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(PersonalClearTools)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.vCbxDeleteFiles = QCheckBox(self.centralwidget)
        self.vCbxDeleteFiles.setObjectName(u"vCbxDeleteFiles")
        self.vCbxDeleteFiles.setIconSize(QSize(18, 18))
        self.vCbxDeleteFiles.setChecked(True)

        self.gridLayout_2.addWidget(self.vCbxDeleteFiles, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.vCbxEmptyRecycleBin = QCheckBox(self.centralwidget)
        self.vCbxEmptyRecycleBin.setObjectName(u"vCbxEmptyRecycleBin")
        self.vCbxEmptyRecycleBin.setIconSize(QSize(18, 18))
        self.vCbxEmptyRecycleBin.setChecked(True)

        self.gridLayout_3.addWidget(self.vCbxEmptyRecycleBin, 0, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_4.addWidget(self.progressBar, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.vCbxClosePrograms = QCheckBox(self.centralwidget)
        self.vCbxClosePrograms.setObjectName(u"vCbxClosePrograms")
        self.vCbxClosePrograms.setIconSize(QSize(18, 18))
        self.vCbxClosePrograms.setChecked(True)

        self.gridLayout.addWidget(self.vCbxClosePrograms, 0, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.vBtnCheckXMLFile = QPushButton(self.centralwidget)
        self.vBtnCheckXMLFile.setObjectName(u"vBtnCheckXMLFile")

        self.gridLayout_8.addWidget(self.vBtnCheckXMLFile, 1, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setSpacing(6)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")

        self.gridLayout_12.addLayout(self.gridLayout_14, 1, 0, 1, 1)

        self.vBtnRun = QPushButton(self.centralwidget)
        self.vBtnRun.setObjectName(u"vBtnRun")

        self.gridLayout_12.addWidget(self.vBtnRun, 0, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_12, 1, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_9, 2, 0, 1, 1)

        self.vBtnCheckLogFiles = QPushButton(self.centralwidget)
        self.vBtnCheckLogFiles.setObjectName(u"vBtnCheckLogFiles")

        self.gridLayout_8.addWidget(self.vBtnCheckLogFiles, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_8, 1, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_7, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_6, 1, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        PersonalClearTools.setCentralWidget(self.centralwidget)
        self.vStatusBar = QStatusBar(PersonalClearTools)
        self.vStatusBar.setObjectName(u"vStatusBar")
        PersonalClearTools.setStatusBar(self.vStatusBar)

        self.retranslateUi(PersonalClearTools)

        QMetaObject.connectSlotsByName(PersonalClearTools)
    # setupUi

    def retranslateUi(self, PersonalClearTools):
        PersonalClearTools.setWindowTitle(QCoreApplication.translate("PersonalClearTools", u"PersonalClearTools", None))
        self.vCbxDeleteFiles.setText(QCoreApplication.translate("PersonalClearTools", u"Delete Files", None))
        self.vCbxEmptyRecycleBin.setText(QCoreApplication.translate("PersonalClearTools", u"Empty Recycle Bin", None))
        self.vCbxClosePrograms.setText(QCoreApplication.translate("PersonalClearTools", u"Close Opened Programs", None))
        self.vBtnCheckXMLFile.setText(QCoreApplication.translate("PersonalClearTools", u"Check XML File", None))
        self.vBtnRun.setText(QCoreApplication.translate("PersonalClearTools", u"RUN", None))
        self.vBtnCheckLogFiles.setText(QCoreApplication.translate("PersonalClearTools", u"Check Log Files", None))
    # retranslateUi

