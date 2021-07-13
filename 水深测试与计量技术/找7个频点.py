#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/3/29 10:19
# @Author : Cheng
# @File : 找7个频点.py
# @Software : PyCharm

import xlrd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

# 打开xls文件：
def F6():
    """
    求解发射换能器的谐振峰，-3dB带宽和半功率带宽
    """
    work_book = xlrd.open_workbook('E:\\哈尔滨工程大学\\研一课程\\水声测试与计量技术\\导纳数据\\发射曲线数据.xls')
    # 按sheet表名称获取sheet对象，名称分大小写
    sheet_1 = work_book.sheet_by_name('Sheet1')
    # 根据列索引获取某一列的值
    x = sheet_1.col_values(0)
    y = sheet_1.col_values(1)
    # 找出y的最大值
    m = max(y)
    # y最大时对应的x
    f0 = x[y.index(max(y))]
    print("谐振频率：", f0)
    # -3dB点对应的G
    # print(0.707*m)
    plt.plot(x,y)
    # x1 = [50000, 209000]
    # y1 = [0.004033, 0.02323]
    x1 = [50000, 500000]
    y1 = [0.004033, 0.0585]
    plt.plot(x1, y1)
    x2 = [50000, 500000]
    y2 = [0.004033+0.4469, 0.0585+0.4469]
    plt.plot(x2, y2)
    plt.xlabel("Hz")
    plt.ylabel("ms")
    plt.title("发射换能器导纳曲线")
    plt.show()

def J6():
    """
    求解接收换能器的谐振峰，-3dB带宽和半功率带宽
    """
    work_book = xlrd.open_workbook('E:\\哈尔滨工程大学\\研一课程\\水声测试与计量技术\\导纳数据\\接收曲线数据.xlsx')
    # 按sheet表名称获取sheet对象，名称分大小写
    sheet_1 = work_book.sheet_by_name('Sheet1')
    # 根据列索引获取某一列的值
    x = sheet_1.col_values(0)
    y = sheet_1.col_values(1)
    # 找出y的最大值
    m = max(y)
    # y最大时对应的x
    f0 = x[y.index(max(y))]
    print("谐振频率：", f0)
    # -3dB点对应的G
    # print(0.707*m)
    plt.plot(x,y)
    # x1 = [88000, 358000]
    # y1 = [0.279448, 0.934527]
    x1 = [50000, 500000]
    y1 = [0.12131, 1.21311]
    plt.plot(x1, y1)
    x2 = [50000, 500000]
    y2 = [0.12131+4.30881, 1.21311+4.30881]
    plt.plot(x2, y2)
    plt.xlabel("Hz")
    plt.ylabel("ms")
    plt.title("接收换能器导纳曲线")
    plt.show()

if __name__ == '__main__':
    # F6()
    J6()
