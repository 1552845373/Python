#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/1/27 16:59
# @Author : Cheng
# @File : 生成脚本文件.py
# @Software : PyCharm

import numpy as np

'''
写此程序的意义：
首先需明白的是这里的多波束数据的点密度远远高于卫星数据。且多波束有部分数据缺失，现需要用卫星数据数据进行修补，此程序要做的是对两类数据进行简单叠加。
现有同一范围内的卫星和多波束的高程数据，存储格式为.txt。现需要对卫星数据中的经纬度进行替换，替换成与其数值接近的多波束经纬度，以便后续数据处理以及作图。如不处理，则会出现白条现象（卫星数据导致）。
'''

# 从.txt中分别读取经纬度数据，返回浮点数列表
def getinfo(satellite, multi_beam):
    lon_slist, lat_slist, deeplist = [], [], []
    lon_mlist, lat_mlist, deepmlist = [], [], []
    # 提取卫星数据的经纬度
    with open(satellite, 'r') as f:
        for line in f.readlines():
            lon_s, lat_s, deep_s = line.split(',')
            lon_slist.append(lon_s), lat_slist.append(lat_s), deeplist.append(deep_s.replace('\n', ''))
    # 提取多波束数据的经纬度
    with open(multi_beam, 'r') as f:
        for line in f.readlines():
            lon_m, lat_m, deep_s = line.split()
            lon_mlist.append(lon_m), lat_mlist.append(lat_m), deepmlist.append(deep_s.replace('\n', ''))
    # 将列表中的字符串转换成浮点型
    lon_slistn = list(map(float, lon_slist))
    lon_mlistn = list(map(float, lon_mlist))
    lat_slistn = list(map(float, lat_slist))
    lat_mlistn = list(map(float, lat_mlist))
    deeplistn = list(map(float, deeplist))
    deepmlistn = list(map(float, deepmlist))
    return lon_slistn, lat_slistn, lon_mlistn, lat_mlistn, deeplistn, deepmlistn

# 卫星数据经纬度替换成与其相近的多波束经纬度（方便显示在同一行列，否则会有白条）
def modify(lon_slistn, lat_slistn, lon_mlistn, lat_mlistn):
    # 定义寻找数组中与给定值最近的值的函数
    def find_nearest(array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx]
    # 定义两个空列表，用来存储修正后的数据
    lon_modify, lat_modify = [], []
    for num in lon_slistn[:100]:
        near = find_nearest(lon_mlistn, num)
        lon_modify.append(near)
    for num in lat_slistn[:100]:
        near = find_nearest(lat_mlistn, num)
        lat_modify.append(near)
    return lon_modify, lat_modify

def savestxt(lon, lat, deep):
    with open('C:\\Users\\陌离\\Desktop\\数据合并\\卫星裁剪修正.txt', 'w') as f:
        for i in range(len(lon)):
            f.writelines(str(lon[i])+','+str(lat[i])+','+str(deep[i]))
            f.write('\n')
    f.close()

def savemtxt(lon, lat, deep):
    with open('C:\\Users\\陌离\\Desktop\\数据合并\\多波束修正.txt', 'w') as f:
        for i in range(len(lon)):
            f.writelines(str(lon[i])+','+str(lat[i])+','+str(deep[i]))
            f.write('\n')
    f.close()

if __name__ == '__main__':
    satellite = 'C:\\Users\\陌离\\Desktop\\数据合并\\gebco-裁剪.txt'
    multi_beam = 'C:\\Users\\陌离\\Desktop\\数据合并\\真实多波束深水.txt'
    lon_slistn, lat_slistn, lon_mlistn, lat_mlistn, deeplistn, deepmlistn = getinfo(satellite, multi_beam)
    lon_modify, lat_modify = modify(lon_slistn, lat_slistn, lon_mlistn, lat_mlistn)
    savestxt(lon=lon_modify, lat=lat_modify, deep=deeplistn)
    savemtxt(lon=lon_mlistn, lat=lat_mlistn, deep=deepmlistn)