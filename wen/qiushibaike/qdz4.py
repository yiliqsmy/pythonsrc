#! python3
#coding=utf-8
#爬取糗事百科段子
#可用
import urllib.request
import re

class Spider_QSBK:
    def __init__(self):
        self.page_index = 2
        self.enable = False
        self.stories = []
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent':self.user_agent}

    def getPage(self, page_index):
        url = 'http://www.qiushibaike.com/hot/page/' + str(page_index)
        try:
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request)
            content = response.read().decode('utf-8')
            return content
        except urllib.error.URLError as e:
            print (e.reason)
            return None

    def getStories(self,page_index):
        content = self.getPage(page_index)
        pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div.*?span>(.*?)</span>(.*?)<div class="stats">.*?"number">(.*?)</i>'
                     ,re.S)
        items = re.findall(pattern,content)
        for item in items:
            haveImg = re.search("img", item[2])
            if not haveImg:
               self.stories.append([item[0], item[1], item[3]])
        return self.stories

    def ShowStories(self, page_index):
        self.getStories(page_index)
        fileHandle = open("dz4.txt", 'a')
        for st in self.stories:
            print (u"第%d页\t发布人:%s\t点赞数:%s\n%s" %(page_index, st[0], st[2], st[1]))
            fileHandle.write("第%d页\t发布人:%s\t点赞数:%s\n%s" %(page_index, st[0], st[2], st[1]))
        del self.stories

    def start(self):
        self.enable = True
#        while self.enable:
        self.ShowStories(self.page_index)
        self.page_index += 1


spider = Spider_QSBK()
spider.start()
