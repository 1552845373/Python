#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/1/13 13:31
# @Author : Cheng
# @File : SST绘制.py
# @Software : PyCharm

import netCDF4 as nc
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
from mpl_toolkits.basemap import Basemap
from scipy import interpolate
import warnings
from PIL import Image

def readnc(openfilepath = 'D:\\sst.mon.mean.nc',month=None):
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
    sst = f.variables['sst'][month]
    # 关闭nc文件
    f.close()
    return lon, lat, sst

def Interpolation(lon, lat, sst, times=1):
    sst[sst>50] = 20
    # sst=np.squeeze(sst)
    func = interpolate.interp2d(lon,lat,sst,kind='linear')
    lon_new = np.linspace(min(lon),max(lon),360*times)
    lat_new = np.linspace(min(lat),max(lat),180*times)
    sst_new = func(lon_new,lat_new)#xnew, ynew是一维的，输出znew是二维的
    return lon_new, lat_new, sst_new

def drawing(lon_new, lat_new, sst_new, savefilepath='D:\\中国近海sst分布图\\未处理\\sst.png'):
    # 定位到具体经纬度
    map = Basemap(llcrnrlon = 114.5, llcrnrlat = 20.5, urcrnrlon = 130.5, urcrnrlat = 34.5)
    lon, lat = np.meshgrid(lon_new, lat_new)
    plt.figure(figsize=(9, 7.88)) # 设置画布大小
    ax = plt.gca()
    plt.style.use('classic')
    # # 绘制经纬线
    # map.drawparallels(np.arange(-90., 91., 5.), labels=[1,0,0,0], fontsize=10)  # 纬线
    # map.drawmeridians(np.arange(-180., 181., 5.), labels=[0,0,0,1], fontsize=10)  # 经线

    # m.drawmapboundary(fill_color = 'aqua')
    # map.fillcontinents(color = 'white', lake_color = 'white')
    # map.drawcoastlines()
    map.readshapefile('C:\\Users\\陌离\\Desktop\\全球海岸线shape\\GSHHS_h_L1', name='country', color='w')
    # D:\\ArcGIS10.3\\海岸线数据\\全球海岸线\\海岸线
    # C:\\Users\\陌离\\Desktop\\全球海岸线shape\\GSHHS_h_L1
    for shp in map.country:
        poly = Polygon(xy=shp, facecolor='w') # 填充
        ax.add_patch(poly)
    # 添加Colorbar
    # cmap = plt.get_cmap('rainbow')
    colormesh = map.pcolormesh(lon, lat, sst_new)
    # cb = map.colorbar(colormesh, location='bottom', label="contour lines", pad="10%")

    # 去掉图片边框
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, hspace = 0, wspace = 0) # 让图片铺满画布
    # 添加标题、单位
    # cb.set_label("℃")
    # plt.title('Sea Surface Temperature')

    plt.savefig(savefilepath)
    # plt.show()

def setalpha(openfilepath = 'D:\\中国近海sst分布图\\未处理\\sst.png', savefilepath = 'D:\\中国近海sst分布图中国近海sst分布图\\透明化\\sst_alpha.png'):
    # 将图片中的白色改为透明色
    img = Image.open(openfilepath)  # 读取照片
    img = img.convert('RGBA')    # 转换格式，确保像素包含alpha通道
    width, height = img.size     # 长度和宽度
    for i in range(0,width):     # 遍历所有长度的点
        for j in range(0,height):       # 遍历所有宽度的点
            data = img.getpixel((i,j))  # 获取一个像素
            if (data.count(255) == 4):  # RGBA都是255，改成透明色
                img.putpixel((i,j),(255,255,255,0))
    img.save(savefilepath)  # 保存图片

if __name__ == '__main__':
    for i in range(3):
        lon, lat, sst = readnc(month=i+1548)
        lon_new, lat_new, sst_new = Interpolation(lon, lat, sst, times=20)
        drawing(lon_new, lat_new, sst_new, savefilepath='D:\\中国近海sst分布图\\未处理\\2020.'+str(i+1)+'.png')
        setalpha(openfilepath='D:\\中国近海sst分布图\\未处理\\2020.'+str(i+1)+'.png', savefilepath='D:\\中国近海sst分布图\\透明化\\2020.'+str(i+1)+'.png')
        print('已完成{}月sst的绘制'.format(i+1))