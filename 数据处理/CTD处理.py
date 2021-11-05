#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/10/30 10:15
# @Author : Cheng
# @File : CTD处理.py
# @Software : PyCharm

import xlrd
import numpy as np
from scipy import interpolate

book = xlrd.open_workbook("C:\\Users\\陌离\\Desktop\\O1\\060659_20191216_1627.xlsx")
sheet = book.sheet_by_name("Data")
t = sheet.col_values(2)[2:]
d = sheet.col_values(5)[2:]
s = sheet.col_values(6)[2:]
print(d)
# f = interpolate.Akima1DInterpolator(d.sort(), s)
#插值比例尺
# xnew=np.linspace(df.iloc[0,0],df.iloc[109,0],220)

#插值方式，"nearest","zero"为阶梯插值，slinear 线性插值
#插值函数
# f=interpolate.interp1d(df.iloc[:,0],df.iloc[:,1],kind=kind)
#插值
# ynew=f(xnew)
#绘制插值数据曲线
