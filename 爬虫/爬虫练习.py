#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2020/10/29 12:23
# @Author : Cheng
# @File : 爬虫练习.py
# @Software : PyCharm

'''
import bs4
import requests
from lxml import etree

# xpath与lxml结合使用
html = etree.parse('file:///E:/%E5%93%88%E5%B0%94%E6%BB%A8%E5%B7%A5%E7%A8%8B%E5%A4%A7%E5%AD%A6/python/csdn%E5%AD%A6%E9%99%A2/150%E8%AE%B2%E8%BD%BB%E6%9D%BE%E6%90%9E%E5%AE%9APython%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/%E4%BB%A3%E7%A0%81/03%E6%95%B0%E6%8D%AE%E8%A7%A3%E6%9E%90/test.html')

print(html.xpath('//book/title/text()'))

# 从本地打开html
file = 'E:\哈尔滨工程大学\python\csdn学院\\150讲轻松搞定Python网络爬虫\代码\\03数据解析\\test.html'
with open(file) as f:
    html = f.read()
soup = bs4.BeautifulSoup(html,'lxml')
# print(soup.prettify())
print(soup.select('book > title')[0].get_text())
'''

'''
import threading
import time

glock = threading.Lock()

def coding():
    for i in range(3):
        glock.acquire()
        print('{} is coding'.format(threading.current_thread().name))
        glock.release()
        time.sleep(1)

def drawing():
    for i in range(3):
        glock.acquire()
        print('{} is drawing'.format(threading.current_thread().name))
        glock.release()
        time.sleep(1)

def muti_thread():
    th1 = threading.Thread(target=coding)
    th2 = threading.Thread(target=drawing)

    th1.start()
    th2.start()

if __name__ == '__main__':
    muti_thread()
'''

