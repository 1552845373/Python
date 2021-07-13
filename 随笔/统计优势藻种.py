#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2020/11/7 14:22
# @Author : Cheng
# @File : 统计优势藻种.py
# @Software : PyCharm

import matplotlib.pyplot as plt

# fr=open(r'C:\Users\陌离\Desktop\优势藻种.txt','r',encoding='UTF-8')
# fd=open(r'C:\Users\陌离\Desktop\优势藻种_new.txt','w')
# for text in fr.readlines():
#     if text.split():
#         text = text.replace(' ','')
#         text = text.replace('\n','、')
#         fd.write(text)
# fd.close()
# fr.close()

with open(r'C:\Users\陌离\Desktop\优势藻种_new.txt','r') as f:
    data = f.read().split('、')
count = {}
for word in data:
    count[word] = count.get(word,0) + 1
ls = list(count.items())
ls.sort(key=lambda x:x[1], reverse=True)
x = []
y = []
for i in range(10):
    a,b = ls[i]
    x.append(a)
    y.append(b)

#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.bar(x,y)
# 调节x轴坐标的倾斜度数
# plt.xticks(rotation=10)
plt.title('优势藻种的出现次数')
plt.xlabel('优势藻种')
plt.ylabel('次数')
# 在柱状图的柱子上标值
for a, b in zip(x, y):
    plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=11)
# plt.savefig(r'C:\Users\陌离\Desktop\1.jpg')
plt.show()