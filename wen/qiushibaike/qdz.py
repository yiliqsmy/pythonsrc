#! python3
#coding=utf-8
#爬取糗事百科段子
#可用
import urllib.request
import re
def parse_html():
    page = 1
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    try:
            request = urllib.request.Request(url,headers = headers)
            response = urllib.request.urlopen(request)
            content = response.read().decode('utf-8')

            pattern_author = re.compile(u'<h2>(.*?)\s*</h2>',re.S)
            pattern_content = re.compile(u'<div class="content">\s*(.*?)\s*</div>', re.S)
            pattern_comment = re.compile(u'<i class="number">(\d*)</i>\s*好笑',re.S)

            find_author = re.findall(pattern_author,content)
            find_content = re.findall(pattern_content,content)
            find_comment = re.findall(pattern_comment,content)

            if find_author:
                fileHandle = open("qdz.txt", 'w')
                for i in range(len(find_author)):
                    content = find_content[i].replace("<br/>",",")
                    contenta= content.replace("<span>", "")
                    contentb = contenta.replace("</span>", "")
                    #print(contentb)
                    result = str(i)+" "+find_author[i]+" "+contentb+" "+str(find_comment[i])
                    fileHandle.write(result)
                    print (result)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print (e.code)
        if hasattr(e,"reason"):
            print (e.reason)
parse_html()
