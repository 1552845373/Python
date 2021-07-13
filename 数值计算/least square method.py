#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2020/10/21 10:17
# @Author : Cheng
# @File : least square method.py
# @Software : PyCharm

# 最小二乘法
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

def least(x,y,n):              # x,y为样本点，n为给定的拟合次数
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

    # 绘制函数图像
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.scatter(x, y, color="red", label="样本点", linewidth=2)
    x = np.linspace(min(x),max(x),1000)
    plt.plot(x, np.poly1d(fac[0])(x), color="orange", label="拟合曲线", linewidth=2)
    # plt.title(np.poly1d(fac[0]))
    plt.legend()
    plt.show()

if __name__ == '__main__':
    x = np.array([0,1,2,3,-1,-2,-3])
    y = np.array([-1.21,1.9,3.2,10.3,2.2,3.71,8.7])
    n = 5
    least(x, y, n)

'''
# 用正交多项式实现最小二乘
import numpy as np

# 定义一个运算内积的函数
def fun(x, y):
    for i in range(m)

    return x * y

def least_square(x, y, n):
    if 0<n<len(x)-1:
        fi = np.ones(len(x))
        a = fun(fi,y)/fun(fi,fi)
        sum = a*fi

        ai = fun(np.poly1d([1])*fi,fi)/fun(fi,fi)


    else:
        print('给定次数超出范围')
    return sum

if __name__ == '__main__':
    x = []
    y = []
    m = len(x)
'''
