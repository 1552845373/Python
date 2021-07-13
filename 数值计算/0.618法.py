#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2020/10/15 9:44
# @Author : Cheng
# @File : 0.618法.py
# @Software : PyCharm

import math
def f(x):
    return math.exp(x) - 5*x
a,b,u = 1,2,0.1
m = a + 0.382*(b - a)
n = a + 0.618*(b - a)
print('S320050011-王城')
while b - a >= u:
    if f(m) > f(n):
        if (b - m) <= u:
            print('{:^13.3f}'.format(n))
            break
        else:
            a,b,m = m,b,n
            # f(m) = f(n)
            n = a + 0.618*(b - a)
    else:
        if (n - a) <= u:
            print('{:^13.3f}'.format(m))
            break
        else:
            a,b,n = a,n,m
            # f(n) = f(m)
            m = a + 0.328*(b - a)