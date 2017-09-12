#! python3
#coding=utf-8
#读者杂志在线的版本
#可用， 批量下载文章，保存为txt格式。
import urllib.request
import os
from bs4 import BeautifulSoup

def urlBS(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    return soup

def main(url):
    soup = urlBS(url)
    link = soup.select('.booklist a')
    path = os.getcwd()+u'/读者文章201703保存/'
    if not os.path.isdir(path):
        os.mkdir(path)
    for item in link:
        newurl = baseurl + item['href']
        result = urlBS(newurl)
        title = result.find("h1").string
        writer = result.find(id="pub_date").string.strip()
        filename = path + title + '.txt'
        print (filename)
        new=open(filename,"w",encoding='gbk')
        new.write("<<" +str(title) + ">>\n\n")
        new.write(str(writer)+"\n\n")
        text = result.select('.blkContainerSblkCon p')
        for p in text:
            context = p.text
            new.write(str(context))
        new.close()

if __name__ == '__main__':
    year = input("请输入年份：")
    mouth = input("请输入月份：")
    time = year + "_" + mouth
    baseurl = 'http://www.52duzhe.com/' + time +'/'
    firsturl = baseurl + 'index.html'
    main(firsturl)
