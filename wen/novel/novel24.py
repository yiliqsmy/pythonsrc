#!python3
#coding=utf-8
#可用
#爬取小说--章节--内容
#诛仙
from bs4 import BeautifulSoup
import  urllib.request
import re
import time
start =time.clock()
title=[]    #小说名
href=[]     #链接
url = 'http://www.biquge.tw/26_26491/'
response = urllib.request.urlopen(url)
html_cont=response.read()
soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
hrefAndname = soup.find("div", {"id":"list"}).findAll("a")

#for item in hrefAndname:
# href.append(item['href'])

for item in hrefAndname: #保存小说名和链接
    if re.findall(re.compile(u"[\u4e00-\u9fa5]"),item.text):
        # print item.text.encode('utf-8')
       title.append(item.text)
       href.append(item['href'])

wen = []
for i in range(len(href)):
    try:
        print ("爬取第"+str(i+1)+"章中……")
        newurl = 'http://www.biquge.tw'+ href[i]
        response = urllib.request.urlopen(newurl)
        html_cont = response.read()
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        content = soup.find("div", {"id":"content"})
        cont=title[i]+str(content)
        cont = re.sub(r'<\s*script[^>]*>[^<]*<\s*/\s*script\s*>','',cont)
        cont = re.sub(r'</div>','',cont)    #删除br标签
        cont = re.sub(r'<div\s\S*>','',cont)
        cont = re.sub(r'<br/>','\n',cont)   #替换换行符
     #   f = open("E:/res/"+ str(i+1)+ ' .txt','w')
        wen.append(cont)
        # print(cont)
        # print(wen)
    except:
        print  ("错误， 爬取第"+str(i+1)+"章失败")

file_path=r"诛仙.txt"
fp = open(file_path, "w", encoding='utf-8')
print(wen)
for item in wen:
     fp.write(str(item) + "\n")  #list中一项占一行
fp.close()
print ("成功")
end = time.clock()
print('运行: %s 秒'%(end-start))
# 成功
# 运行: 387.54492952265264 秒
