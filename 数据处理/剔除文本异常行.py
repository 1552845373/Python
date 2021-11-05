#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/10/18 21:30
# @Author : Cheng
# @File : 剔除文本异常行.py
# @Software : PyCharm

import os
root = "C:\\Users\\陌离\Desktop\\06-气象原始数据"

for dirpath, dirnames, filenames in os.walk(root):
    for filename in filenames:
        if os.path.splitext(filename)[1] == '.log':  # 目录下包含.log的文件
            path = os.path.join(dirpath,filename)
            path1 = os.path.join(dirpath,os.path.splitext(filename)[0]+'.txt')
            with open(path, 'r') as r:
                l = len(r.readlines()[1:2][0])
                r.seek(0, 0)
                lines = r.readlines()

            with open(path1, 'w') as w:
                for line in lines:
                    if len(line) == l:
                        w.write(line)
