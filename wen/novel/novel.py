#!python3
#coding=utf-8
#可用
#爬取网页文字内容
#一章节一个文件
from bs4 import BeautifulSoup
import  urllib.request
import re

title=[]    #小说名
href=[]     #链接
url = 'http://www.biquge.tw/26_26491/'
response = urllib.request.urlopen(url)
html_cont=response.read()
soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
hrefAndname = soup.find("div", {"id":"list"}).findAll("a")

#for item in hrefAndname:
#    href.append(item['href'])

for item in hrefAndname: #保存小说名和链接
    if re.findall(re.compile(u"[\u4e00-\u9fa5]"),item.text):
     #  print item.text.encode('utf-8')
       title.append(item.text)
       href.append(item['href'])

for i in range(len(href)):
    try:
        print ("爬取第"+str(i+1)+"章中……")
        newurl = 'http://www.biquge.tw'+ href[i]
        response = urllib.request.urlopen(newurl)
        html_cont = response.read()
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        content = soup.find("div", {"id":"content"})
        cont=str(content)
        cont = re.sub(r'<\s*script[^>]*>[^<]*<\s*/\s*script\s*>','',cont)
        cont = re.sub(r'</div>','',cont)    #删除br标签
        cont = re.sub(r'<div\s\S*>','',cont)
        cont = re.sub(r'<br/>','\n',cont)   #替换换行符
     #   f = open("E:/res/"+ str(i+1)+ ' .txt','w')
        f = open("d:/pythonsrc/wen/小说相关/"+title[i]+'.txt','w')
        f.write(cont)
        f.close
        print ("success")
    except:
        print  ("Sorry， 爬取第"+str(i+1)+"章失败")



