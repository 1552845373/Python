#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/2/2 15:24
# @Author : Cheng
# @File : 九九乘法表.py
# @Software : PyCharm
#
# for i in range(10):
#     j = 1
#     while j <= i:
#         print(f'{j}*{i}={i*j}', end='\t')
#         # print('{}*{}={}'.format(j, i, i*j), end='\t')
#         # print('%d*%d=%d'%(j,i,i*j), end='\t')
#         j += 1
#     if i >=1 and j <= 9:
#         print()
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j}*{i}={j*i}',end=' ')
        print()