#红黑联盟安全资讯。每页15条新闻
# -*- coding: utf-8 -*-
import scrapy
import re
import os
from time import sleep
import pymysql  # python3连接数据库的模块pymysql
from doubanbook.items import DoubanbookItem

class DbbookSpider(scrapy.Spider):
    name = "dbbook"
    #allowed_domains = ["https://www.2cto.com/news/safe/1318.html]
    start_urls = (
        'https://www.2cto.com/news/safe/index.html',
    )
    count =1
    filename = "news.txt"
    if os.path.exists(filename) == True:
        os.remove(filename)


    def database(self,filename):  # 调用这个自定义函数来实现对数据库的操作
        connect = pymysql.connect(
            user="root",
            passwd="",  # 连接数据库，不会的可以看我之前写的连接数据库的文章
            port=3306,
            host="127.0.0.1",
            db="news",
            charset="utf8"
        )
        con = connect.cursor()  # 获取游标
        # con.execute("create database news")  # 创建数据库，！！！！这一条代码仅限第一次使用，有了数据库后就不用再使用了
        con.execute("use news")  # 使用数据库
        con.execute("drop table if exists t_redblack")  # 判断是否存在这个数据库表
        sql = '''create table t_redblack(id int auto_increment primary key,tag varchar(244),title varchar(100),web varchar(1000))CHARACTER SET utf8 '''
        con.execute(sql)  # 执行sql命令  创建t_freebuf表来保存信息
        with open(filename, "r",encoding="utf8") as f:  # 打开path本地文档
            while True:
                info = f.readline()  # 一行一行的读取文档信息
                if info:
                    info = info.strip()  # 去掉换行符
                    info = info.split(";")  # 以;来分割将信息变换为列表形式
                    web= info[0]
                    title = info[1]
                    tag= info[2]
                    con.execute("insert into t_redblack(id,tag,title,web)values(NULL,%s,%s,%s)",[tag, title, web])
                    # 这一句就是将信息保存至t_freebuf表中
                else:
                    break
        connect.commit()  # 我们需要提交数据库，否则数据还是不能上传的
        con.close()  # 关闭游标
        connect.close()  # 关闭数据库
        print("导入数据结束!!!!!!!!!")


    def parse(self, response):
        #print response.body
        #item = DoubanbookItem()
        self.count += 1
        self.filename = "news.txt"
        URL = 'https://www.2cto.com'
        selector = scrapy.Selector(response)
        books = selector.xpath('//li[@class="clearfix"]')#每条新闻
        # 每一页有15条新闻
        for each in books:
            tag =""
            author=[]
            auth= each.xpath('div/p[@class="tags"]/a').xpath('string(.)').extract()
            for i in range(len(auth)):
                tag = tag+auth[i]+","
            author.append(tag)
            title  = each.xpath('a/text()').extract()
            web = each.xpath('a/@href').extract()
            #print(title)
            with open(self.filename, "a",encoding="utf8") as f:
                # 将我们获取到的信息保存到本地
                #for i in range(len(web)):  # 以某个属性的长度来循环
                     # 我们将这些信息保存起来，并用;来分隔
                    f.write(web[0] + ";")
                    f.write(title[0]+ ";")
                    f.write(author[0] + "\n")
        #yield item
        print("爬取一页")
        sleep(0.1)
        nextPage = selector.xpath('//div[@class="text-c"]/a[contains(text(),"下一页")]/@href').extract()[0]
        if self.count<=1317:
                next=URL+nextPage
                yield scrapy.http.Request(next, callback=self.parse)
        else:
                self.database(self.filename)  # 当超过20页时跳出返回，调用database函数存信息到数据库
