#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2020/10/16 20:11
# @Author : Cheng
# @File : fun1.py
# @Softare : PyCharm

def difference_quotient1(x,y):
    import numpy as np
    if len(x)!=len(y):
        print('数据输入错误，请检查输入数据')
    n=len(x)
    y1=np.zeros((n,n))
    y1[:,0]=y
    #x=np.asarray(x)
   #y=np.asarray(y)
    for i in range(1,n):
        for j in range(i,n):
            y1[j,i]=(y1[j,i-1]-y1[j-1,i-1])/(x[j]-x[j-i])
    np.set_printoptions(suppress=True)
    return y1

x=[0.00,0.10,0.20,0.30,0.40,0.50]
y=[1.00000,0.99500,0.98007,0.95534,0.92106,0.87758]
print(difference_quotient1(x,y))