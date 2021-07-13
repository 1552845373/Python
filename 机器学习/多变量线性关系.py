#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/6/29 10:12
# @Author : Cheng
# @File : 多变量线性关系.py
# @Software : PyCharm

from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

with open(r'C:\Users\陌离\Desktop\新建文件夹\well17vpjj1.txt','r') as f:
    data = f.read().split()
    x1 = list(map(eval, data))

with open(r'C:\Users\陌离\Desktop\新建文件夹\well17vpkx1.txt','r') as f:
    data = f.read().split()
    x2 = list(map(eval, data))

with open(r'C:\Users\陌离\Desktop\新建文件夹\well17vprlx1.txt','r') as f:
    data = f.read().split()
    x3 = list(map(eval, data))

with open(r'C:\Users\陌离\Desktop\新建文件夹\well17vp1.txt','r') as f:
    data = f.read().split()
    y = list(map(eval, data))

x = [[x1[i], x2[i], x3[i]] for i in range(len(x1))]

estimator = LinearRegression() # 实例化估计器
estimator.fit(x, y) # 使用fit方法训练模型

score = estimator.score(x, y)
y_predict = estimator.predict(x)
error = mean_squared_error(y, y_predict)
print("\t准确率为:", score)
print("\t回归系数为:", estimator.coef_)
print("\t偏置:", estimator.intercept_)
print("\t均方误差为:", error)
