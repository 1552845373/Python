#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2022/1/7 10:58
# @Author : Cheng
# @File : 两列平均.py
# @Software : PyCharm

# with open("F:\\ctd\\O3.txt", "r") as f:
#     l1 = f.readlines()[:100]
#
# with open("F:\\ctd\\ZS4.txt", "r") as f:
#     l2 = f.readlines()[:100]
#
# with open("F:\\ctd\\1-3.txt", "w") as w:
#     for i in range(100):
#         w.write(l1[i][:8])
#         w.write(str(round((eval(l1[i][8:14])+eval(l2[i][8:14]))/2,3)).ljust(6,"0"))
#         w.write(" ")
#         w.write(str(round((eval(l1[i][15:22])+eval(l2[i][15:22]))/2,4)).ljust(7,"0"))
#         w.write(l1[i][22:])

with open("F:\\ctd\\O3N.txt", "r") as f:
    l1 = f.readlines()[:100]

with open("F:\\ctd\\ZS4N.txt", "r") as f:
    l2 = f.readlines()[:100]

with open("F:\\ctd\\2-4N.txt", "w") as w:
    for i in range(100):
        w.write(l1[i][:12])
        w.write(str(round((eval(l1[i][12:18])+eval(l2[i][12:18]))/2,3)).ljust(6,"0"))
        w.write(l1[i][18:23])
        w.write(str(round((eval(l1[i][23:30])+eval(l2[i][23:30]))/2,4)).ljust(7,"0"))
        w.write(l1[i][30:])