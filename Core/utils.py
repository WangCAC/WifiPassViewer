#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : ZXTest
@File : utils
@Description : 
@Auther : WangCAC
@Email : wangcac1843608878@gmail.com
@Date : 2025/10/8 下午4:37
"""

import subprocess
import re
import logging
import sys
import colorlog

# 1. 创建一个 logger
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)

# 2. 创建一个 handler，用于输出到控制台
handler = colorlog.StreamHandler()

# 3. 定义 handler 的输出格式，并设置颜色
#    log_colors 参数可以自定义不同日志级别的颜色
formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s - %(levelname)s - %(message)s',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)
handler.setFormatter(formatter)

# 4. 给logger添加handler
logger.addHandler(handler)


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
        logger.exception(e)

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
            logger.info(f"查询：{command}")
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True, encoding="GBK",
                                    errors='ignore')
            output = result.stdout
            # 通过正则表达式获取 wifi密码
            pwds_profiles_data = list(map(lambda x: get_wifi_pwd_by_line(x), output.splitlines()))
            pwds_profiles_data = list(filter(None, pwds_profiles_data))
            pwds_map.setdefault(wifi_name, pwds_profiles_data[0])

        except Exception as e:
            pwds_map.setdefault(wifi_name, None)
            logging.exception(e)
        logger.info(f"查询结果：{pwds_map[wifi_name]}")
    return pwds_map


print(get_wifi_pwds(get_wifi_names()))
