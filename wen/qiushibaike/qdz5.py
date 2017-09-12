#! python3
#coding=utf-8
#爬取糗事百科段子
#可用
#遇到编码问题会停止
import re
import urllib.request
from urllib.error import URLError,HTTPError
import sys

print(sys.getdefaultencoding())

url = 'http://www.qiushibaike.com/text/page/1'
# 给文件加入头信息，用以模拟浏览器访问
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
for i in range(1,30+1):
    try:
        #实现翻页翻页
        url = re.sub('page/\d+','page/%d'%i,url,re.S)
        print(url)
        #发送请求，获得返回信息
        req = urllib.request.Request(url,headers=headers)
        response = urllib.request.urlopen(req,timeout=5)
        content = response.read().decode('utf-8')
        #处理获取的web网页，并将信息处理了
        items = re.findall('<div class="content">(.*?)</div>',content,re.S)
        length = len(items)
        for j in range(0,length):
            #将信息写入文件中
            fileHandle = open("dz5.txt",'a')
            fileHandle.write(str(j+1)+": ")
            fileHandle.write(items[j])
            fileHandle.write("\n")
    except HTTPError as e:
        print("HTTPError")
    except URLError as e:
        print("URLError")
