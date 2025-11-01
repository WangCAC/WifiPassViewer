# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReaderWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_ReaderWidget(object):
    def setupUi(self, ReaderWidget):
        if not ReaderWidget.objectName():
            ReaderWidget.setObjectName(u"ReaderWidget")
        ReaderWidget.resize(423, 347)
        self.gridLayout = QGridLayout(ReaderWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fileListWidget = QListWidget(ReaderWidget)
        QListWidgetItem(self.fileListWidget)
        self.fileListWidget.setObjectName(u"fileListWidget")
        font = QFont()
        font.setPointSize(10)
        self.fileListWidget.setFont(font)

        self.verticalLayout.addWidget(self.fileListWidget)

        self.readButton = QPushButton(ReaderWidget)
        self.readButton.setObjectName(u"readButton")
        self.readButton.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.readButton)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(ReaderWidget)

        QMetaObject.connectSlotsByName(ReaderWidget)
    # setupUi

    def retranslateUi(self, ReaderWidget):
        ReaderWidget.setWindowTitle(QCoreApplication.translate("ReaderWidget", u"Form", None))

        __sortingEnabled = self.fileListWidget.isSortingEnabled()
        self.fileListWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.fileListWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("ReaderWidget", u"1.json", None));
        self.fileListWidget.setSortingEnabled(__sortingEnabled)

        self.readButton.setText(QCoreApplication.translate("ReaderWidget", u"\u8bfb\u53d6", None))
    # retranslateUi

