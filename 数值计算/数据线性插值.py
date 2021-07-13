#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/5/26 14:28
# @Author : Cheng
# @File : 数据线性插值.py
# @Software : PyCharm

import netCDF4 as nc
from matplotlib import pyplot as plt
import numpy as np
import warnings
from scipy.optimize import leastsq

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

def readtxt(openfilepath = 'C:\\Users\\陌离\\Desktop\\O3T10-1\\01.txt'):
    deepls, templs, speedls = [], [], []
    warnings.filterwarnings("ignore")
    # 显示全部数据
    np.set_printoptions(threshold=np.inf)
    # 读取nc文件
    f = open(openfilepath, "r", encoding="utf-8")
    for line in f.readlines():
        deep, temp, speed = line.split()
        deepls.append(eval(deep)), templs.append(eval(temp)), speedls.append(eval(speed))

    f.close()
    return deepls, templs, speedls


def least(x,y,n):              # x,y为样本点，n为给定的拟合次数
    """
    用最小二乘法进行拟合，得到拟合曲线的函数关系式，并绘制样本散点图，叠加上拟合曲线
    :param x: 坐标横轴
    :param y: 坐标纵轴
    :param n: 自定义拟合次数
    """
    # 需要拟合的函数func
    def func(n):
        # list = []
        # for i in n:
        #     list.append(1)
        return np.poly1d(n)

    # 误差函数
    def error(n,x,y):
        return func(n)(x) - y

    # 进行最小二乘，系数存放在第0个位置
    fac = leastsq(error, np.ones(n+1), args=(x, y))
    # 打印拟合曲线的表达式
    print(np.poly1d(fac[0]))
    # 预测

    predict = np.polyval(np.poly1d(fac[0]), 2300)
    print(predict)
    # 绘制函数图像
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.scatter(x, y, color="blue", label="样本点", linewidth=2)
    x = np.linspace(min(x),max(x),1000)
    plt.plot(x, np.poly1d(fac[0])(x), color="red", label="拟合曲线", linewidth=5)
    # plt.title(np.poly1d(fac[0]))
    plt.rcParams.update({'font.size': 14})
    plt.legend()
    # plt.text(4, 14, "函数关系式：", fontsize=14)
    plt.text(4, 13.9, np.poly1d(fac[0]), fontsize=14)
    plt.xlabel('月')
    plt.ylabel('℃')
    plt.title("全球月平均SST散点图")
    plt.show()

if __name__ == '__main__':
    deepls, templs, speedls = readtxt()

    m = int((2300 - deepls[-1])/5+1)
    delta = (4 - templs[-1])/m
    for i in range(m):
        templs.append(templs[-1]+delta)
    print(templs)

