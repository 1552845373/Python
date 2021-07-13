#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2020/10/15 21:16
# @Author : Cheng
# @File : l1.py
# @Software : PyCharm

import numpy as np
import pandas as pd

# 拉格朗日插值
def lagrange(x,y,X = None):              #x,y为样本点，X为试验（插值）点
    f = 0
    for i in range(len(x)):                    #外层循环实现对每一项l(x)*y的累加
        lx,ly = 1,0
        for j in range(len(x)):                   #内层循环实现每一项l(x)*y
            if i != j:
                lx *= np.poly1d([1,-x[j]])/(x[i] - x[j])
        ly = lx * y[i]
        f += ly
    if X is None:                          #判断是否有插值点，没有则输出插值多项式，有则输出由插值多项式的系数以及插值点对应函数值组成的元组
        return f
    else:
        return f,f(X)

if __name__ == '__main__':
    x = [0.32,0.34,0.36]
    y = [0.314567,0.333487,0.352274]
    X = [1,2,3]
    print(lagrange(x,y,X))


# 牛顿插值（向前差分）
def newtons_forward(x,y,X = None):              #x,y为样本点，X为试验（插值）点
    f = 1
    w = y
    for i in range(1,len(x)):                  #外层循环对内层循环累加得到前插多项书（这里的变量对应书中的t,而非x）
        w = pd.Series(w).diff()                  #对y进行差分，由于在外层循环中，实现N次差分
        pt = float(w[i])                          #取差分后的第i个值为f0的n次差分（列表中前i-1个为空）
        for j in range(i):                         #内层循环得到N(x0+th)中的每一项
            # pt *= np.poly1d([1,-j]) / (j+1)
            pt *= np.poly1d([j],True)/(j+1)
        f += pt
    if X is None:                               #判断是否有插值点，没有则输出插值多项式，有则输出由插值多项式的系数以及插值点对应函数值组成的元组
        return f
    else:                                          #将t转换成x
        def b(m):
            return (m - x[0]) / (x[1] - x[0])
        t = list(map(b,X))
        return f,f(t)

if __name__ == '__main__':
    x=[0.00,0.10,0.20,0.30,0.40,0.50]
    y=[1.00000,0.99500,0.98007,0.95534,0.92106,0.87758]
    X = [4,5,6]
    print(newtons_forward(x,y,X))


# 埃米尔特差分
def hermite_interp(x,y,m,X=None):               #x,y为样本点，m是导数值，X为试验（插值）点
#生成第v结点处的拉格朗日插值基函数
    def lagrange(v):
        lx=1
        for i in range(len(x)):
            if i != v:
                lx *= np.poly1d([1,-x[i]])/(x[v]-x[i])
        return lx
#计算基函数alpha(x)
    def hermite_aipha(v):
        pt=0
        for i in range(len(x)):
            if i != v:
                pt += 1/(x[v]-x[i])
        p_aipha=(1-2*pt*np.poly1d([1,-x[i]]))*pow(lagrange(v),2)
        return p_aipha
#计算基函数beta(x)
    def hermite_beta(v):
        p_beta=np.poly1d([1,-x[v]])*pow(lagrange(v),2)
        return p_beta
#计算埃尔米特插值多项式
    h = 0
    for i in range(len(x)):
        h += (y[i]*hermite_aipha(i)+m[i]*hermite_beta(i))
    if X is None:
        return h
    else:
        return h,h(X)

if __name__ == '__main__':
    x=[np.pi/6,np.pi/3]
    y=[1/2,np.sqrt(3)/2]
    m=[np.sqrt(3)/2,1/2]
    X=[5*np.pi/18,5*np.pi/18]
    print(hermite_interp(x,y,m))