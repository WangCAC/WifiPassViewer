#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : ZXTest
@File : ReaderWidget
@Description : 
@Auther : WangCAC
@Email : wangcac1843608878@gmail.com
@Date : 2025/10/11 上午9:23
"""
import json
import os.path
from datetime import datetime

from PySide6.QtCore import Slot, Signal
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QWidget, QDialog

from UI.ReaderDialog import Ui_ReaderDialog
from UI.ReaderWidget import Ui_ReaderWidget

class ReaderDialog(QDialog):
    data_ready = Signal(str)

    def __init__(self, parent=None):
        """
        初始化
        @param parent: 父窗口类
        """
        super().__init__(parent)

        # 设置Qt_UI文件
        self.ui = Ui_ReaderDialog()
        self.ui.setupUi(self)

        # 设置标题
        self.setWindowTitle("选择要读取的存档")

        # 设置图标
        logoIcon = QIcon(QPixmap(":/icons/logo.png"))
        self.setWindowIcon(logoIcon)

        # 获取组件
        self.readerButton = self.ui.readButton
        self.delButton = self.ui.delButton
        self.mergeButton = self.ui.mergeButton

        self.fileListWidget = self.ui.fileListWidget

        # 初始化
        self.readeFileNames()

        # 绑定 信号<->槽函数
        self.readerButton.clicked.connect(self.clickReadButton)
        self.delButton.clicked.connect(self.clickDelButton)
        self.mergeButton.clicked.connect(self.clickMergeButton)

    def getSaveFileNames(self):
        """
        获取保存文件夹里的 json文件名列表
        @return: 返回 json文件名列表
        """
        filesDir = os.path.join(os.path.abspath("."), "Save")

        if not os.path.exists(filesDir):
            os.makedirs(filesDir)

        fileList = [x for x in os.listdir(filesDir) if os.path.splitext(x)[-1] == '.json']
        return fileList

    def readeFileNames(self):
        """
        读取存档文件列表
        @return: 无返回值
        """
        fileList = self.getSaveFileNames()
        self.fileListWidget.clear()
        for fileName in fileList:
            self.fileListWidget.addItem(fileName)

    @Slot(str)
    def clickReadButton(self):
        """
        点击读取按钮后，返回选中的文件名字符串给主窗口类
        @return: 返回当前选中的文件名
        """
        currentFile = self.fileListWidget.currentItem()
        filePath = os.path.join(os.path.abspath("./Save"), currentFile.text())
        if filePath:
            self.data_ready.emit(filePath)
            super().accept()

    @Slot()
    def clickDelButton(self):
        """
        点击删除按钮后，删除当前选中的json文件
        @return: 无返回值
        """
        currentFile = self.fileListWidget.currentItem()
        filePath = os.path.join(os.path.abspath("./Save"), currentFile.text())
        if os.path.exists(filePath):
            os.remove(filePath)
            self.readeFileNames()

    @Slot()
    def clickMergeButton(self):
        """
        点击合并按钮后，合并已有的json文件数据
        @return: 无返回值
        """
        fileList = self.getSaveFileNames()
        wifi_pwd_dic = {}
        for fileName in fileList:
            filePath = os.path.join(os.path.abspath("./Save"), fileName)
            with open(filePath, 'r', encoding="utf-8") as f:
                dic = json.load(f)
                for key, value in dic.items():
                    wifi_pwd_dic.setdefault(key, value)

            os.remove(filePath)
            self.readeFileNames()

        now = datetime.now()
        saveFilePath = os.path.join(os.path.abspath("./Save"), f"merge-{now.strftime("%Y-%m-%d-%H-%M-%S")}.json")

        if wifi_pwd_dic == {}:
            return
        with open(saveFilePath, 'w', encoding="utf-8") as f:
            json.dump(wifi_pwd_dic, f, ensure_ascii=False, indent=4)
        self.readeFileNames()
