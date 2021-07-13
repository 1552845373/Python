#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/5/12 15:49
# @Author : Cheng
# @File : 互易校准.py
# @Software : PyCharm

import openpyxl
import math

wb = openpyxl.load_workbook('E:\\哈尔滨工程大学\\研一课程\\水声测试与计量技术\实验数据\\互易校准、灵敏度\\互易校准法.xlsx')
ws = wb["Sheet1"]
SiFlist, MJlist, SiHlist, MHlist = [], [], [], []
R = 50
d = 0.1
f = [item.value*1000 for item in list(ws.columns)[0][2:]] # 单位转换成Hz
eFH = [item.value*1000 for item in list(ws.columns)[1][2:]] # 单位转换成mV，和下面的保持一致
eFJ = [item.value for item in list(ws.columns)[3][2:]]
eHJ = [item.value for item in list(ws.columns)[5][2:]]
eH = [item.value for item in list(ws.columns)[6][2:]]
for i in range(7):
    J = 2/(1e+15*f[i])
    SiF = 20*math.log10(((eFJ[i]*eHJ[i]*R*d)/(eFH[i]*eH[i]*J))**0.5)
    MJ = 20*math.log10(((eFJ[i]*eHJ[i]*R*d*J)/(eFH[i]*eH[i]))**0.5)
    SiH = 20*math.log10(((eFH[i]*eHJ[i]*R*d)/(eFJ[i]*eH[i]*J))**0.5)
    MH = 20*math.log10(((eFH[i]*eHJ[i]*R*d*J)/(eFJ[i]*eH[i]))**0.5)
    SiFlist.append(SiF)
    MJlist.append(MJ)
    SiHlist.append(SiH)
    MHlist.append(MH)
print("发射器发送电流响应级：\n", SiFlist, "\n接收器灵敏度级：\n", MJlist, "\n互易换能器发送电流响应级：\n", SiHlist, "\n互易换能器灵敏度级：\n", MHlist)
