#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : ZXTest
@File : MainWindow
@Description : wifi 密码查看工具主窗口
@Auther : WangCAC
@Email : wangcac1843608878@gmail.com
@Date : 2025/10/9 下午2:39
"""

import json
import logging
import os.path
import re
import subprocess
from datetime import datetime

from PySide6 import QtCore
from PySide6.QtCore import Slot, QObject
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow, QTabWidget, QTableWidgetItem, QHeaderView, QMessageBox
from PySide6.scripts.metaobjectdump import Signal

from UI.MainWindow import Ui_MainWindow
from Resources import icons
from UI.View.ReaderDialog import ReaderDialog


def get_wifi_names():
    """
    获取已经连接过的wifi列表
    @return: 已经连接过的wifi列表
    """
    names_profiles_data = []
    try:
        command = "netsh wlan show profiles"
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        output = result.stdout
        # 通过正则表达式获取 wifi名称 列表
        names_profiles_data = list(map(lambda x: get_wifi_name_by_line(x), output.splitlines()))
        names_profiles_data = list(filter(None, names_profiles_data))

        return names_profiles_data

    except Exception as e:
        logging.exception(e)

    return names_profiles_data


def get_wifi_pwds(wifi_names):
    """
    获取 wifi名称<=>wifi密码 的映射表
    @param wifi_names: wifi名称列表
    @return: 映射表
    """
    pwds_map = {}
    for wifi_name in wifi_names:
        pwds_profiles_data = []
        try:
            command = f'netsh wlan show profiles "{wifi_name}" key=clear'
            logging.info(f"查询：{command}")
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True, encoding="GBK",
                                    errors='ignore')
            output = result.stdout
            # 通过正则表达式获取 wifi密码
            pwds_profiles_data = list(map(lambda x: get_wifi_pwd_by_line(x), output.splitlines()))
            pwds_profiles_data = list(filter(None, pwds_profiles_data))

            print(wifi_name,pwds_profiles_data,sep="\n")

            if not pwds_profiles_data:
                pwds_map.setdefault(wifi_name, "")
            else:
                pwds_map.setdefault(wifi_name, pwds_profiles_data[0])

        except Exception as e:
            pwds_map.setdefault(wifi_name, None)
            logging.exception(e)
    return pwds_map


def get_wifi_name_by_line(line):
    """
    获取传入文本中的 wifi名称
    @param line: 传入的行文本
    @return: wifi名称
    """
    search_result = re.search("所有用户配置文件 : .*", line)
    if search_result:
        search_result = search_result.group(0)
        search_result = search_result.split(":")[-1].strip()
        return search_result
    return None


def get_wifi_pwd_by_line(line):
    """
    获取传入文本中的 wifi名称
    @param line: 传入的行文本
    @return: wifi名称
    """
    search_result = re.search("关键内容.*", line)
    if search_result:
        search_result = search_result.group(0)
        search_result = search_result.split(":")[-1].strip()
        return search_result
    return None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        # 设置标题
        self.setWindowTitle("Wifi 密码查看器")

        # 设置图标
        logoIcon = QIcon(QPixmap(":/icons/logo.png"))
        self.setWindowIcon(logoIcon)

        # 获取组件
        self.tableWidget = self.ui.tableWidget
        self.findButton = self.ui.findButton
        self.saveButton = self.ui.saveButton
        self.readButton = self.ui.readButton

        # 其他窗口
        # self.readerDialog = None

        # 绑定 信号<->槽函数
        self.findButton.clicked.connect(self.clickFindButton)
        self.readButton.clicked.connect(self.clickReadButton)
        self.saveButton.clicked.connect(self.clickSaveButton)

    def fillWifiInfo(self, dic):
        """
        填充Wifi相关数据槽函数
        @return: 无返回值
        """

        self.tableWidget.clearContents()

        self.tableWidget.setRowCount(len(dic))
        self.tableWidget.setColumnCount(2)

        headers = ["Wifi 名称", "Wifi 密码"]
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for row_index, (wifi_name, wifi_pwd) in enumerate(dic.items()):
            # 构造Item数据
            name_item = QTableWidgetItem(wifi_name)
            pwd_item = QTableWidgetItem(wifi_pwd)
            # 填充数据
            self.tableWidget.setItem(row_index, 0, name_item)
            self.tableWidget.setItem(row_index, 1, pwd_item)
        # 优化显示
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)

    @Slot()
    def clickFindButton(self):
        """
        点击按钮触发的事件——获取wifi信息并填充到表格里
        @return: 无返回值
        """
        self.fillWifiInfo(get_wifi_pwds(get_wifi_names()))

    @Slot()
    def clickReadButton(self):
        """
        点击读取按钮，弹出读取列表
        @return: 无返回值
        """
        dialog = ReaderDialog(self)
        dialog.data_ready.connect(self.readDataFromFile)
        dialog.exec()

    def readDataFromFile(self, filePath):
        print(filePath)
        try:
            with open(filePath, 'r', encoding="utf-8") as f:
                wifi_pwd_dic = json.load(f)
        except Exception as e:
            wifi_pwd_dic = {}

        self.fillWifiInfo(wifi_pwd_dic)

    @Slot()
    def clickSaveButton(self):
        """
        点击保存按钮后，保存数据，弹出相关提示窗口
        @return: 无返回值
        """
        flag, info = self.saveData(get_wifi_pwds(get_wifi_names()))
        if flag:
            QMessageBox.information(
                self,  # 父窗口
                "成功",  # 窗口标题
                info  # 提示信息
            )
        else:
            QMessageBox.critical(
                self,
                "失败",
                info
            )

    def saveData(self, dic):
        """
        把字典数据保存成 json
        @param dic: 传入的字典数据
        @return: 返回 bool状态:相关信息
        """
        try:
            pwd = os.path.abspath(".")
            savePath = os.path.join(pwd, "Save")
            if not os.path.exists(savePath):
                os.mkdir(savePath)
            now = datetime.now()
            saveFilePath = os.path.join(savePath, f"{now.strftime("%Y-%m-%d-%H-%M-%S")}.json")
            with open(saveFilePath, "w", encoding="utf-8") as f:
                json.dump(dic, f)

        except Exception as e:
            return False, f"保存失败：{e}"

        return True, f"保存成功：{saveFilePath}"
