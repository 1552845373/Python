#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/8/19 16:18
# @Author : Cheng
# @File : 双线性插值.py
# @Software : PyCharm

from PIL import Image
import numpy as np
import math
def BiLinear_interpolation(img,dstH,dstW):
    scrH,scrW,_=img.shape
    img=np.pad(img,((0,1),(0,1),(0,0)),'constant')
    retimg=np.zeros((dstH,dstW,3),dtype=np.uint8)
    for i in range(dstH):
        for j in range(dstW):
            scrx=(i+1)*(scrH/dstH)-1
            scry=(j+1)*(scrW/dstW)-1
            x=math.floor(scrx)
            y=math.floor(scry)
            u=scrx-x
            v=scry-y
            retimg[i,j]=(1-u)*(1-v)*img[x,y]+u*(1-v)*img[x+1,y]+(1-u)*v*img[x,y+1]+u*v*img[x+1,y+1]
    return retimg
im_path='C:/Users/陌离/Desktop/11.jpg'
image=np.array(Image.open(im_path))
image2=BiLinear_interpolation(image,image.shape[0]*2,image.shape[1]*2)
image2=Image.fromarray(image2.astype('uint8')).convert('RGB')
image2.save('C:/Users/陌离/Desktop/11(双线性插值).jpg')