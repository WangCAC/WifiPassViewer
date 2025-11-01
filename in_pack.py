#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : ZXTest
@File : in_pack
@Description : 
@Auther : WangCAC
@Email : wangcac1843608878@gmail.com
@Date : 2025/10/9 下午5:39
"""
from soeasypack import to_pack

main_py_path = r"D:\workpath2\Python\Projects\ZXTest\Projects\WifiCator\main.py"
save_dir = r"D:\workpath2\Python\Projects\ZXTest\Projects\WifiCator\output"
png_path = r"D:\workpath2\Python\Projects\ZXTest\Projects\WifiCator\Resources\icons\logo.png"

to_pack(main_py_path, save_dir, png_path=png_path, embed_exe=True)
