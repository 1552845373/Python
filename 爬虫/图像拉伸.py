#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/11/12 11:21
# @Author : Cheng
# @File : 图像拉伸.py
# @Software : PyCharm

from PIL import Image
import requests
import os

'''https://ci.xiaohongshu.com/ 这个是小红书无水印拼接链接，后面只要传入：traceId 里面的参数即可'''


def fetchUrl(url):
    '''
    发起网络请求，获取网页源码
    '''
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 ',
        'cookie': 'xhsTrackerId=ec223d2a-1230-46c2-c6df-5787b5847112; xhsTracker=url=noteDetail&xhsshare=CopyLink; timestamp2=2021111202063864a8433b110f69806a; timestamp2.sig=5a-kCnN7HwR-3PVP1r-CtAq514PclSOz9iQVIa1iziU; extra_exp_ids=ranchipuar_clt1,commentshow_clt1,gif_clt1,ques_exp1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36',
    }

    r = requests.get(url, headers=headers)
    return r.text


def parsing_link(html):
    '''
    解析html文本，提取无水印图片的 url
    '''

    beginPos = html.find('imageList') + 11
    endPos = html.find(',"cover"')
    imageList = eval(html[beginPos: endPos])

    for i in imageList:
        picUrl = f"https://ci.xiaohongshu.com/{i['traceId']}"
        yield picUrl, i['traceId']


def download(url, root, filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36',
    }
    os.makedirs(root, exist_ok=True)
    with open(f'{root}{filename}.jpg', 'wb') as v:
        try:
            r = requests.get(url, headers=headers)
            v.write(r.content)
        except Exception as e:
            print('图片下载错误！')

def stretch(root):
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.jpg':  # 目录下包含.log的文件
                path = os.path.join(dirpath, filename)
                path1 = os.path.join(dirpath, os.path.splitext(filename)[0] + '(拉伸)' + '.jpg')
                im = Image.open(path)
                region = im.resize((1080, 1980))  ##重新设定大小
                region.save(path1)


if __name__ == '__main__':
    original_link = 'https://www.xiaohongshu.com/discovery/item/5d4e286c0000000027008258'
    root = 'C:\\Users\\陌离\\Desktop\\聊天背景1\\'
    html = fetchUrl(original_link)
    for url, traceId in parsing_link(html):
        print(f"download image {url}")
        download(url, root, traceId)
    print("Finished!")
    # stretch(root)
