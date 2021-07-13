#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/5/13 14:54
# @Author : Cheng
# @File : 标准比较法.py
# @Software : PyCharm

import openpyxl
import math

wb = openpyxl.load_workbook('E:\\哈尔滨工程大学\\研一课程\\水声测试与计量技术\实验数据\\互易校准、灵敏度\\标准比对法.xlsx')
ws = wb["Sheet1"]
Mxlist, Svlist, Ms = [], [], [-211, -213,- 213, -214, -214, -215,-215]
qlist = []
d = 0.1
f = [item.value*1000 for item in list(ws.columns)[0][2:]] # 单位转换成Hz
ex = [item.value/1000 for item in list(ws.columns)[1][2:]] # 单位转换成V
es = [item.value/1000 for item in list(ws.columns)[3][2:]] # 单位转换成V
for i in range(7):
    Mx = Ms[i] + 20*math.log10(ex[i]) - 20*math.log10(es[i])
    Sv = 20*math.log10(ex[i]*d) - Mx
    q = f[i]/8000
    Mxlist.append(Mx)
    Svlist.append(Sv)
    qlist.append(q)
print("发射器声源级：\n", Svlist, "\n接收器灵敏度级：\n", Mxlist, "\n品质因数Q：\n", qlist)