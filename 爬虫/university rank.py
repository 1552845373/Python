# -*- coding = utf-8 -*-

import requests
import bs4
# import openpyxl
# from bs4 import BeautifulSoup

# 2020中国大学排名
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 10)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        demo = r.text
        soup = bs4.BeautifulSoup(demo, 'lxml')
        return soup
    except:
        print('获取异常')

def fillUnivlist(soup):
    ulist = []
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string.replace('\n','').replace(' ',''),tds[1].text.replace('\n','').replace(' ',''),tds[4].string.replace('\n','').replace(' ','')])
    return ulist

def printUnivlist(ulist,num):
    tpl = '{0:^10}\t{1:{3}^15}\t{2:^10}'
    print(tpl.format('排名','学校名称','总分',chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tpl.format(u[0],u[1],u[2],chr(12288)))

# def save_to_excel(ulist):
#     wb = openpyxl.Workbook()
#     ws = wb.active
#     ws['A1'] = '排名'
#     ws['B1'] = '学校名称'
#     ws['C1'] = '总分'
#     for u in ulist:
#         ws.append(u)
#     wb.save('C:\\Users\\陌离\\Desktop\\中国大学排名.xlsx')

def main():
    url = 'http://www.shanghairanking.cn/rankings/bcur/2020'
    soup = getHTMLText(url)
    ulist = fillUnivlist(soup)
    printUnivlist(ulist,567)
    # save_to_excel(ulist)

if __name__ == '__main__':
    main()