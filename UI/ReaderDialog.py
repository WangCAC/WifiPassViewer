# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReaderDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLayout, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QWidget)

class Ui_ReaderDialog(object):
    def setupUi(self, ReaderDialog):
        if not ReaderDialog.objectName():
            ReaderDialog.setObjectName(u"ReaderDialog")
        ReaderDialog.resize(428, 190)
        self.gridLayout = QGridLayout(ReaderDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fileListWidget = QListWidget(ReaderDialog)
        QListWidgetItem(self.fileListWidget)
        self.fileListWidget.setObjectName(u"fileListWidget")
        font = QFont()
        font.setPointSize(10)
        self.fileListWidget.setFont(font)

        self.horizontalLayout.addWidget(self.fileListWidget)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.readButton = QPushButton(ReaderDialog)
        self.readButton.setObjectName(u"readButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.readButton.sizePolicy().hasHeightForWidth())
        self.readButton.setSizePolicy(sizePolicy)
        self.readButton.setMinimumSize(QSize(80, 40))
        self.readButton.setFont(font)
        self.readButton.setAutoRepeat(False)

        self.gridLayout_2.addWidget(self.readButton, 0, 0, 1, 1)

        self.delButton = QPushButton(ReaderDialog)
        self.delButton.setObjectName(u"delButton")
        sizePolicy.setHeightForWidth(self.delButton.sizePolicy().hasHeightForWidth())
        self.delButton.setSizePolicy(sizePolicy)
        self.delButton.setMinimumSize(QSize(80, 40))
        self.delButton.setFont(font)

        self.gridLayout_2.addWidget(self.delButton, 1, 0, 1, 1)

        self.mergeButton = QPushButton(ReaderDialog)
        self.mergeButton.setObjectName(u"mergeButton")
        sizePolicy.setHeightForWidth(self.mergeButton.sizePolicy().hasHeightForWidth())
        self.mergeButton.setSizePolicy(sizePolicy)
        self.mergeButton.setMinimumSize(QSize(80, 40))
        self.mergeButton.setFont(font)

        self.gridLayout_2.addWidget(self.mergeButton, 2, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(ReaderDialog)

        QMetaObject.connectSlotsByName(ReaderDialog)
    # setupUi

    def retranslateUi(self, ReaderDialog):
        ReaderDialog.setWindowTitle(QCoreApplication.translate("ReaderDialog", u"Dialog", None))

        __sortingEnabled = self.fileListWidget.isSortingEnabled()
        self.fileListWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.fileListWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("ReaderDialog", u"1.json", None));
        self.fileListWidget.setSortingEnabled(__sortingEnabled)

        self.readButton.setText(QCoreApplication.translate("ReaderDialog", u"\u8bfb\u53d6", None))
        self.delButton.setText(QCoreApplication.translate("ReaderDialog", u"\u5220\u9664", None))
        self.mergeButton.setText(QCoreApplication.translate("ReaderDialog", u"\u4e00\u952e\u5408\u5e76", None))
    # retranslateUi

