#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2020/10/15 20:59
# @Author : Cheng
# @File : zhu.py
# @Software : PyCharm

import l1
import numpy as np

if __name__ == '__main__':
    x=[0.32,0.34,0.36]
    y=[0.314567,0.333487,0.352274]
    print(l1.lagrange(x, y))

    x=[0.00,0.10,0.20,0.30,0.40,0.50]
    y=[1.00000,0.99500,0.98007,0.95534,0.92106,0.87758]
    print(l1.newtons_forward(x, y))

    x=[np.pi/6,np.pi/3]
    y=[1/2,np.sqrt(3)/2]
    m=[np.sqrt(3)/2,1/2]
    X=[5*np.pi/18,5*np.pi/18]
    print(l1.hermite_interp(x, y, m))
