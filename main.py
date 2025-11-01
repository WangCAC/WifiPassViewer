#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : ZXTest
@File : main.py
@Description : 
@Auther : WangCAC
@Email : wangcac1843608878@gmail.com
@Date : 2025/10/8 下午4:33
"""
import sys

from PySide6 import QtCore, QtWidgets, QtGui

from UI.View.MainWindow import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
