#!python3
#coding=utf-8
#可用
#爬取网页文字内容
import urllib.request
from bs4 import BeautifulSoup
import re
import os
url = "http://www.duanwenxue.com/article/673911.html"
a = urllib.request.urlopen(url)

htmlstr = a.read().decode('GB18030')

soup = BeautifulSoup(htmlstr, 'html.parser')

y = re.compile(r'<p>([\s\S]*?)</p>')
text = y.findall(str(soup))  # 第一次正则表达式筛选所有<p></p>中的内容

x = ''
print(len(text))
for i in range(0, len(text)):
    x = x + text[i]

text1 = re.sub("</?\w+[^>]*>", '', x)  # 去掉html标签

text2 = text1.replace("。", '。\n\n\0\0')  # 让文本更好看
print(text2)
path = os.getcwd()+u'/word/'
if not os.path.isdir(path):
        os.mkdir(path)
filename = path + 'word.txt'
new = open(filename, "w", encoding='gbk')
new.write(str(text2))
print("下载完成")
