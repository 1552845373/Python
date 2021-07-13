#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2020/10/15 20:59
# @Author : Cheng
# @File : fun.py
# @Software : PyCharm

import numpy as np
from numpy.polynomial import Polynomial as P

# def lagrange(x,y,x0=None):
#     M = len(x)
#     p = P([0])
#     for j in range(M):
#         # pt = P(y[j])  #使用类生成实例
#         pt = y[j]
#         for k in range(M):
#             if k == j:
#                 continue
#             fac = x[j]-x[k]
#             pt *= P([-x[k],1])/fac
#         p += pt
#     if x0 is None:
#         return p
#     else:
#         x0=np.asarray(x0)
#         return np.around(p(x0),6) #取小数点后六位


# x=[0.00,0.10,0.20,0.30,0.40,0.50]
# y=[1.00000,0.99500,0.98007,0.95534,0.92106,0.87758]
# def newtons_forward(x,y,x0=None):
#     M=len(x)
#     p=y[0]*P([1])
#     for i in range(1,M):
#         pt=P([1])*np.diff(y,i)[0]
#         for j in range(i):
#             pt *= P.fromroots(j)/(j+1)
#         p += pt
#     if x0 is None:
#         return p
#     else:
#         x0 = np.asarray(x0)
#         t = (x0 - x[0]) / (x[1] - x[0])
#         return np.around(p(t), 6)  # 取小数点后六位
# print(newtons_forward(x,y))


# def hermite_interp(x,y,m,x0=None):
#     if len(x) != len(y) or len(y) != len(m):
#         print('函数值与导数值不相等')
#     M=len(x)
#     h=P([0])
# #生成第i结点处的拉格朗日插值基函数
#     def lagrange(i):
#         pt=P([1])
#         for k in range(M):
#             if k == i:
#                 continue
#             fac = x[i]-x[k]
#             pt *= P([-x[k],1])/fac
#         return pt
# #计算基函数alpha(x)
#     def hermite_aipha(i):
#         pt=0
#         for k in range(M):
#             if k == i:
#                 continue
#             fac = x[i]-x[k]
#             pt += 1/fac
#         p_aipha=(1-2*pt*P([-x[i],1]))*lagrange(i)**2
#         return p_aipha
# #计算基函数beta(x)
#     def hermite_beta(i):
#         p_beta=P([-x[i],1])*lagrange(i)**2
#         return p_beta
# #计算埃尔米特插值多项式
#     for i in range(M):
#         h += (y[i]*hermite_aipha(i)+m[i]*hermite_beta(i))
#     if x0 is None:
#         return h
#     else:
#         x0=np.asarray(x0)
#         return np.around(h(x0),6) #取小数点后六位
#
# x=[np.pi/6,np.pi/3]
# y=[1/2,np.sqrt(3)/2]
# m=[np.sqrt(3)/2,1/2]
# x0=[5*np.pi/18,5*np.pi/18]
# print(hermite_interp(x,y,m,x0))