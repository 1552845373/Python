#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/11/15 14:36
# @Author : Cheng
# @File : TD标准文件.py
# @Software : PyCharm

import os

## 航次信息
def ZS_3(z, path):
    a = " "
    station = z    # 站点名字
    s1,s2,s3,s4,s5 = "1","21","中船重工集团公司第七一五研究所","国家530专项","刘福臣"
    s6,s7,s8 = "南海","长和海洋科考船","SCS-E海洋声学调查"
    s9,s10,s11 = "20191214","20200302","1"
    s1,s2,s3,s4,s5 = s1.rjust(1,a),s2.rjust(2,a),s3.rjust(15,a),s4.rjust(16,a),s5.rjust(17,a)
    s6,s7,s8,s9,s10,s11 = s6.rjust(18,a),s7.rjust(13,a),s8.rjust(14,a),s9.rjust(8,a),s10.rjust(8,a),s11.rjust(10,a)
    Z_1 = s1+s2+s3+s4+s5+s6+s7+s8+s9+s10+s11+"\n" # 文本第一行

    ## 站位信息
    weiD = 19   # ZS-3:116.1091°E 19.2724°N  ZS-4: 118.8025°E 19.2986°N
    weiF = 16
    weiM = 20.64
    jinD = 116
    jinF = 6
    jinM = 32.76
    s1,s2,s3,s4 = "2",station,"1"," "
    s51,s52,s53 = f'{weiD}', f'{weiF}', f'{weiM}'    #实际站位，纬度,不知道这种写法对不对，长度要求能否满足？
    s6 = "N"
    s71,s72,s73 = f'{jinD}', f'{jinF}', f'{jinM}'
    s8,s9 = "E","0"
    s101,s102,s103 = f'{weiD}', f'{weiF}', f'{weiM}'
    s11 = "N"
    s121,s122,s123 = f'{jinD}', f'{jinF}', f'{jinM}'
    s13,s14 = "E","0"
    s15,s16 = "GPSMAP2108","7"
    s17 = "20200108"  #投放日期；86 8位 字符型；YYYYMMDD（年月日） 20200108  ZS-3: 2020-01-08 18:30 ZS-4: 2020-01-07 21:30
    s18 = "183000"  #投放时间: 94 6位 字符型；HHMMSS（时分秒）   183000
    s19 = "0"
    s20 = "20200113"  #回收日期；101 8 字符型；YYYYMMDD（年月日）：20200113   ZS-3: 2020-01-13 07:30 ZS-4: 2020-01-12 07:00
    s21 = "073000"  #回收时间: 109 6 字符型；HHMMSS（时分秒）   073000
    s22 = "0"
    s23 = "-0800"
    s24 = "2310"   # 水深，121 8位 浮点型；×××××.××ZS-3: 2310 ZS-4: 3550
    s25,s26 = "1","0"
    # s27 = "8888" #仪器投放深度 131 8 浮点型；×××××.××            这个从文件中读取 深度.txt
    s28 = "1" #采样间隔 139 5 整型 s                         写 0.5  （单位是秒）
    s29 = "240" #样本平均时间 144 5 整型 s                      写  150 （单位是秒）
    s30 = " " # 观测仪器型号 149 12 字符型；仪器的出厂型号       空着即可
    s31 = " " # 161 40 填写各传感器的序列号                   空着即可
    s32,s33 = "MATLAB","王城"

    s1,s2,s3,s4 = s1.rjust(1,a),s2.rjust(10,a),s3.rjust(1,a),s4.rjust(8,a)
    s51,s52,s53 = s51.rjust(2,a),s52.rjust(2,a),s53.rjust(5,a)
    s71,s72,s73 = s71.rjust(3,a),s72.rjust(2,a),s73.rjust(5,a)
    s101,s102,s103 = s101.rjust(2,a),s102.rjust(2,a),s103.rjust(5,a)
    s121,s122,s123 = s121.rjust(3,a),s122.rjust(2,a),s123.rjust(5,a)
    s17,s18 = s17.rjust(8,a),s18.rjust(6,a)
    s20,s21 = s20.rjust(8,a),s21.rjust(6,a)
    s24 = s24.rjust(8,a)
    s28,s29,s30,s31,s32,s33 = s28.rjust(5,a),s29.rjust(5,a),s30.rjust(12,a),s31.rjust(40,a),s32.rjust(30,a),s33.rjust(8,a)

    s01 = s1+s2+s3+s4+s51+s51+s53+s6+s71+s72+s73+s8+s9+s101+s102+s103+s11+s121+s122+s123+s13+s14+s15+s16+s17+s18+s19+s20

    Dict = {}
    with open(path + z + "\\" + z + '深度.txt') as f:
        for line in f.readlines():
            li = line.split()
            Dict[li[0]] = li[1]

    r_root = path + z
    for dirpath, dirnames, filenames in os.walk(r_root):
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.txt':  # 目录下包含.txt的文件
                if filename == z + "深度.txt":
                    continue
                input_path = os.path.join(dirpath, filename)
                out_root = path + z + "标准文件\\"
                os.makedirs(out_root, exist_ok=True)  # 检查路径文件夹是否存在，不存在则创建
                out_path = os.path.join(out_root,os.path.splitext(filename)[0]+'.txt')
                s27 = Dict[os.path.splitext(filename)[0][-4:]]
                s27 = s27.rjust(8,a)
                s02 = s21 + s22 + s23 + s24 + s25 + s26 + s27 + s28 + s29 + s30 + s31 + s32 + s33
                Z_2 = s01 + s02 + '\n'  # 文本第二行

                with open(input_path, 'r') as r:
                    lines = r.readlines()

                with open(out_path, 'w') as w:
                    w.write(Z_1)
                    w.write(Z_2)
                    for line in lines:
                        h = '3'+\
                            ' '+\
                            line[0:14]+\
                            ' '+\
                            '0'+\
                            ' '+\
                            '-0800'+\
                            ' '+\
                            line[23:30]+\
                            ' '+\
                            '0'+\
                            ' '+\
                            line[15:21]+\
                            ' '+\
                            '4'+\
                            ' '+\
                            '0'+\
                            ' '+\
                            ' '*11+\
                            '\n'
                        w.write(h)

def ZS_4(z, path):
    a = " "
    station = z    # 站点名字
    s1,s2,s3,s4,s5 = "1","21","中船重工集团公司第七一五研究所","国家530专项","刘福臣"
    s6,s7,s8 = "南海","长和海洋科考船","SCS-E海洋声学调查"
    s9,s10,s11 = "20191214","20200302","1"
    s1,s2,s3,s4,s5 = s1.rjust(1,a),s2.rjust(2,a),s3.rjust(15,a),s4.rjust(16,a),s5.rjust(17,a)
    s6,s7,s8,s9,s10,s11 = s6.rjust(18,a),s7.rjust(13,a),s8.rjust(14,a),s9.rjust(8,a),s10.rjust(8,a),s11.rjust(10,a)
    Z_1 = s1+s2+s3+s4+s5+s6+s7+s8+s9+s10+s11+"\n" # 文本第一行

    ## 站位信息
    weiD = 19   # ZS-3:116.1091°E 19.2724°N  ZS-4: 118.8025°E 19.2986°N
    weiF = 17
    weiM = 54.96
    jinD = 118
    jinF = 48
    jinM = 9
    s1,s2,s3,s4 = "2",station,"1"," "
    s51,s52,s53 = f'{weiD}', f'{weiF}', f'{weiM}'    #实际站位，纬度,不知道这种写法对不对，长度要求能否满足？
    s6 = "N"
    s71,s72,s73 = f'{jinD}', f'{jinF}', f'{jinM}'
    s8,s9 = "E","0"
    s101,s102,s103 = f'{weiD}', f'{weiF}', f'{weiM}'
    s11 = "N"
    s121,s122,s123 = f'{jinD}', f'{jinF}', f'{jinM}'
    s13,s14 = "E","0"
    s15,s16 = "GPSMAP2108","7"
    s17 = "20200107"  #投放日期；86 8位 字符型；YYYYMMDD（年月日） 20200108  ZS-3: 2020-01-08 18:30 ZS-4: 2020-01-07 21:30
    s18 = "213000"  #投放时间: 94 6位 字符型；HHMMSS（时分秒）   183000
    s19 = "0"
    s20 = "20200112"  #回收日期；101 8 字符型；YYYYMMDD（年月日）：20200113   ZS-3: 2020-01-13 07:30 ZS-4: 2020-01-12 07:00
    s21 = "070000"  #回收时间: 109 6 字符型；HHMMSS（时分秒）   073000
    s22 = "0"
    s23 = "-0800"
    s24 = "3550"   # 水深，121 8位 浮点型；×××××.××ZS-3: 2310 ZS-4: 3550
    s25,s26 = "1","0"
    # s27 = "8888" #仪器投放深度 131 8 浮点型；×××××.××            这个从文件中读取 深度.txt
    s28 = "1" #采样间隔 139 5 整型 s                         写 0.5  （单位是秒）
    s29 = "240" #样本平均时间 144 5 整型 s                      写  150 （单位是秒）
    s30 = " " # 观测仪器型号 149 12 字符型；仪器的出厂型号       空着即可
    s31 = " " # 161 40 填写各传感器的序列号                   空着即可
    s32,s33 = "MATLAB","王城"

    s1,s2,s3,s4 = s1.rjust(1,a),s2.rjust(10,a),s3.rjust(1,a),s4.rjust(8,a)
    s51,s52,s53 = s51.rjust(2,a),s52.rjust(2,a),s53.rjust(5,a)
    s71,s72,s73 = s71.rjust(3,a),s72.rjust(2,a),s73.rjust(5,a)
    s101,s102,s103 = s101.rjust(2,a),s102.rjust(2,a),s103.rjust(5,a)
    s121,s122,s123 = s121.rjust(3,a),s122.rjust(2,a),s123.rjust(5,a)
    s17,s18 = s17.rjust(8,a),s18.rjust(6,a)
    s20,s21 = s20.rjust(8,a),s21.rjust(6,a)
    s24 = s24.rjust(8,a)
    s28,s29,s30,s31,s32,s33 = s28.rjust(5,a),s29.rjust(5,a),s30.rjust(12,a),s31.rjust(40,a),s32.rjust(30,a),s33.rjust(8,a)

    s01 = s1+s2+s3+s4+s51+s51+s53+s6+s71+s72+s73+s8+s9+s101+s102+s103+s11+s121+s122+s123+s13+s14+s15+s16+s17+s18+s19+s20

    Dict = {}
    with open(path+z+"\\"+z+'深度.txt') as f:
        for line in f.readlines():
            li = line.split()
            Dict[li[0]] = li[1]

    r_root = path + z
    for dirpath, dirnames, filenames in os.walk(r_root):
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.txt':  # 目录下包含.txt的文件
                if filename==z+"深度.txt":
                    continue
                input_path = os.path.join(dirpath, filename)
                out_root = path + z + "标准文件\\"
                os.makedirs(out_root, exist_ok=True)  # 检查路径文件夹是否存在，不存在则创建
                out_path = os.path.join(out_root,os.path.splitext(filename)[0]+'.txt')
                s27 = Dict[os.path.splitext(filename)[0][-4:]]
                s27 = s27.rjust(8,a)
                s02 = s21 + s22 + s23 + s24 + s25 + s26 + s27 + s28 + s29 + s30 + s31 + s32 + s33
                Z_2 = s01 + s02 + '\n'  # 文本第二行

                with open(input_path, 'r') as r:
                    lines = r.readlines()

                with open(out_path, 'w') as w:
                    w.write(Z_1)
                    w.write(Z_2)
                    for line in lines:
                        h = '3'+\
                            ' '+\
                            line[0:14]+\
                            ' '+\
                            '0'+\
                            ' '+\
                            '-0800'+\
                            ' '+\
                            line[23:30]+\
                            ' '+\
                            '0'+\
                            ' '+\
                            line[15:21]+\
                            ' '+\
                            '4'+\
                            ' '+\
                            '0'+\
                            ' '+\
                            ' '*11+\
                            '\n'
                        w.write(h)

if __name__ == '__main__':
    path = "C:\\Users\\陌离\\Desktop\\data_fin\\"
    z = "ZS-3"
    ZS_3(z,path)
    z = "ZS-4"
    ZS_4(z,path)