#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/6/25 12:58
# @Author : Cheng
# @File : 时间序列预测.py
# @Software : PyCharm

import netCDF4 as nc
from matplotlib import pyplot as plt
import numpy as np
import warnings
from sklearn.metrics import mean_squared_error
from math import sqrt
from scipy.optimize import leastsq

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

def readnc(openfilepath = 'D:\\sst.mon.mean.nc'):
    """
    读取NC数据文件，获得1560个月的全球月平均SST
    :param openfilepath: 数据位置
    :return:y(1560个月的全球月平均SST形成的列表)
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

def least(x,y,test_index,test,n):              # x,y为样本点，n为给定的拟合次数
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
    # x = np.linspace(min(x),max(x),1000)
    # plt.plot(test_index, np.poly1d(fac[0])(test_index), color="red", label="拟合曲线", linewidth=2)
    plt.plot(x+test_index, np.poly1d(fac[0])(x+test_index), color="red", label="拟合曲线", linewidth=2)
    # plt.title(np.poly1d(fac[0]))
    plt.text(4, 13.8, "函数关系式：", fontsize=14)
    plt.text(4, 13.7, np.poly1d(fac[0]), fontsize=14)
    return np.poly1d(fac[0])(test_index)

def exponential_smoothing(series, alpha):
    """
        series - dataset with timestamps
        alpha - float [0.0, 1.0], smoothing parameter
    """
    result = [series[0]] # first value is same as series
    for i in range(1, len(series)):
        result.append(alpha * series[i] + (1 - alpha) * result[i-1])
    return result

if __name__ == '__main__':
    count = 0
    y = readnc()
    x = [i+1 for i in range(1560)]
    train_index, test_index  = x[0:1300], x[1300:]
    train, test = y[0:1300], y[1300:]
    plt.plot(train_index, train, color="blue", label="训练集", linewidth=1)
    plt.plot(test_index, test, color="orange", label="测试集", linewidth=1)

    # # 朴素法
    # y_pre = [train[-1] for i in test_index]
    # plt.plot(test_index, y_pre, color="red", label="朴素法预测", linewidth=2)

    # # 简单平均法
    # y_pre = [np.mean(train) for i in test_index]
    # plt.plot(test_index, y_pre, color="red", label="简单平均法预测", linewidth=2)

    # # 移动平均法
    # y_pre = [np.mean(train[-100:]) for i in test_index]
    # plt.plot(test_index, y_pre, color="red", label="移动平均法预测", linewidth=2)

    # 最小二乘法
    y_pre = least(train_index, train, test_index, test, 6)

    # # 一次指数平滑法
    # result = exponential_smoothing(y, alpha=0.6)
    # plt.scatter(train_index+test_index, result, color="red", label="滑动平滑法", linewidth=0.5)
    # y_pre = result[1300:]

    # # 计算均方根误差
    # rmse = sqrt(mean_squared_error(test, y_pre))
    # plt.text(4, 13.8, f"均方根误差：{rmse}", fontsize=18)
    # # print(f"均方根误差：{rmse}")

    plt.rcParams.update({'font.size': 14})
    plt.legend()
    plt.xlabel('月')
    plt.ylabel('℃')
    plt.title("全球月平均SST折线图")
    plt.show()
