#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/5/24 10:14
# @Author : Cheng
# @File : SST回归分析.py
# @Software : PyCharm

import netCDF4 as nc
from matplotlib import pyplot as plt
import numpy as np
import warnings
from scipy.optimize import leastsq

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

def readnc(openfilepath = 'D:\\sst.mon.mean.nc'):
    """
    读取NC数据文件，获得1560个月的全球月平均SST
    :param openfilepath: 数据位置
    :return:y: 1560个月的全球月平均SST形成的列表
    """
    # 忽略警告
    warnings.filterwarnings("ignore")
    # 显示全部数据
    np.set_printoptions(threshold=np.inf)
    # 读取nc文件
    f = nc.Dataset(openfilepath)
    # print(dataset.variables.keys()) # 打印变量的属性值
    # 读取数据
    lat = f.variables['lat'][:]
    lon = f.variables['lon'][:]
    time = f.variables['time']
    y = []
    for i in range(1560):
        sst = f.variables['sst'][i]
        y.append(np.mean(sst))
    # 关闭nc文件
    f.close()
    return y

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
        global count
        count += 1
        print(f"误差函数被调用次数：{count}")
        return func(n)(x) - y

    # 进行最小二乘，系数存放在第0个位置
    fac = leastsq(error, np.ones(n+1), args=(x, y))
    # 打印拟合曲线的表达式
    print("拟合曲线为：\n", np.poly1d(fac[0]))
    # 预测未来某一个月的全球平均SST
    predict = np.polyval(np.poly1d(fac[0]), [i+2509 for i in range(12)])
    average = np.mean(predict)
    print("12个月的预测值为：\n", predict)
    print("2100年全球SST预测值为：\n", average)
    # 绘制函数图像
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.scatter(x, y, color="blue", label="样本点", linewidth=2)
    x = np.linspace(min(x),max(x),1000)
    plt.plot(x, np.poly1d(fac[0])(x), color="red", label="拟合曲线", linewidth=5)
    # plt.title(np.poly1d(fac[0]))
    plt.rcParams.update({'font.size': 14})
    plt.legend()
    plt.text(4, 14, "函数关系式：", fontsize=14)
    plt.text(4, 13.9, np.poly1d(fac[0]), fontsize=14)
    plt.xlabel('月')
    plt.ylabel('℃')
    plt.title("全球月平均SST散点图")
    plt.show()

if __name__ == '__main__':
    y = readnc()
    x = [i+1 for i in range(1560)]
    count = 0
    least(x, y, 1)
