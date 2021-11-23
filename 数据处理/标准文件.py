#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/11/11 17:28
# @Author : Cheng
# @File : 标准文件.py
# @Software : PyCharm

s1 = '1'+\
'2'+\
'02'+\
'国家530专项'.rjust(30-4,' ')+\
'21'+\
'中船重工集团公司第七一五研究所'.rjust(30-15,' ')+\
"南海".rjust(20-2,' ')+\
'SCS-E声学调查'.rjust(20-4,' ')+\
'长和海洋科考船'.rjust(20-7,' ')+\
'2019121620200229-0800'+\
' '*(24+12+44)+\
'刘福臣'.rjust(8-3,' ')+\
' '*6+\
'刘福臣'.rjust(8-3,' ')+\
' '*6+\
'\n'


s2 = '2'+\
'3'+\
' '*4+\
'99.99'+\
'一体式气象站'.rjust(20-6,' ')+\
'GMX600'.rjust(10,' ')+\
' 日期.风向风速.气压.气温.经纬度.航向航速'+\
' '*10+\
'香港培德国际有限公司'.rjust(32-10,' ')+\
' '*508+\
'\n'

import os
root = "C:\\Users\\陌离\\Desktop\\气象标准文件"

for dirpath, dirnames, filenames in os.walk(root):
    for filename in filenames:
        if os.path.splitext(filename)[1] == '.txt':  # 目录下包含.txt的文件
            path = os.path.join(dirpath,filename)
            path1 = os.path.join(dirpath,os.path.splitext(filename)[0]+'.txt')
            with open(path1, 'r') as r:
                lines = r.readlines()[2:]

            with open(path1, 'w') as w:
                w.write(s1)
                w.write(s2)
                for line in lines:
                    w.write(line)
