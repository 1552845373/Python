#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/8/20 14:05
# @Author : Cheng
# @File : 双立方插值.py
# @Software : PyCharm

from PIL import Image
import numpy as np
import math

# 产生16个像素点不同的权重
def BiBubic(x):
    global a
    a=0.5
    x=abs(x)
    if x<=1:
        return 1-(a+3)*(x**2)+(a+2)*(x**3)
    elif x<2:
        return a*(x**3)-5*a*(x**2)+8*a*x-4*a
    else:
        return 0

# 双三次插值算法
# dstH为目标图像的高，dstW为目标图像的宽
def BiCubic_interpolation(img,dstH,dstW):
    scrH,scrW,_=img.shape
    #img=np.pad(img,((1,3),(1,3),(0,0)),'constant')
    retimg=np.zeros((dstH,dstW,3),dtype=np.uint8)
    for i in range(dstH):
        for j in range(dstW):
            scrx=i*(scrH/dstH)
            scry=j*(scrW/dstW)
            x=math.floor(scrx)
            y=math.floor(scry)
            u=scrx-x
            v=scry-y
            tmp=0
            for ii in range(-1,2):
                for jj in range(-1,2):
                    if x+ii<0 or y+jj<0 or x+ii>=scrH or y+jj>=scrW:
                        continue
                    tmp+=img[x+ii,y+jj]*BiBubic(ii-u)*BiBubic(jj-v)
            retimg[i,j]=np.clip(tmp,0,255)
    return retimg

im_path='C:/Users/陌离/Desktop/11.jpg'
image=np.array(Image.open(im_path))
image2=BiCubic_interpolation(image,image.shape[0]*2,image.shape[1]*2)
image2=Image.fromarray(image2.astype('uint8')).convert('RGB')
image2.save('C:/Users/陌离/Desktop/11（双立方插值a='+str(a)+')'+'.jpg')
