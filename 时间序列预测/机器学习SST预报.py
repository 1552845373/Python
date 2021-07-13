#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/5/25 12:54
# @Author : Cheng
# @File : 机器学习SST预报.py
# @Software : PyCharm

import netCDF4 as nc
from matplotlib import pyplot as plt
import numpy as np
import warnings
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsClassifier

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

"""
1、获取数据
2、数据集划分
3、特征工程（标准化）
4、机器学习
5、模型评估
"""

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


if __name__ == '__main__':
    y = readnc()
    x = [[i+1] for i in range(1560)]

    # 机器学习
    estimator = LinearRegression()
    estimator.fit(x, y)

    # 模型评估
    print("回归系数为:", estimator.coef_)
    print("偏置:", estimator.intercept_)

    print(estimator.predict([[100]]))
    plt.scatter(x, y)
    plt.plot(x, estimator.predict(x), color='red', linewidth=5)
    plt.show()
