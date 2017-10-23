#! python3
#coding=utf-8
#爬取果壳网科学新闻
#可用，会有遗漏，数组无法存放太多元素
#多线程
import requests
import json

from multiprocessing import Pool
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from requests.exceptions import ConnectionError




def get_index(offset):
    base_url = 'http://www.guokr.com/apis/minisite/article.json?'
    data = {
        'retrieve_type': "by_subject",
        'limit': "20",
        'offset': offset
    }
    params = urlencode(data)
    url = base_url + params
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.text
        return None
    except ConnectionError:
        print('Error.')
        return None

def parse_json(text):
    try:
        result = json.loads(text)
        if result:
            for i in result.get('result'):
                # print(i.get('url'))
                yield i.get('url')
    except:
        pass

def get_page(url):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            # print(resp.text)
            return resp.text
        return None
    except ConnectionError:
        print('Error.')
        return None

def parse_page(text):
    try:
        soup = BeautifulSoup(text, 'lxml')
        content = soup.find('div', class_="content")
        title = content.find('h1', id="articleTitle").get_text()
        author = content.find('div', class_="content-th-info").find('a').get_text()
        article_content = content.find('div', class_="document").find_all('p')
        all_p = [i.get_text() for i in article_content if not i.find('img') and not i.find('a')]
        article = '\n'.join(all_p)
        # print(title,'\n',author,'\n',article)
        data = {
            'title': title,
            'author': author,
            'article': article
        }
        return data
    except:
        pass



def main(offset):
    text = get_index(offset)
    all_url = parse_json(text)
    urls = []
    file_path = r"果壳网科学新闻.doc"
    fp = open(file_path, "w", encoding='utf-8')
    for url in all_url:
        resp = get_page(url)
        data = parse_page(resp)
        if data:
            print(data["title"])
            #urls.append(data)
            fp.write(str(data))


if __name__ == '__main__':
    pool = Pool()
    offsets = ([0] + [i*20+18 for i in range(2)])
    pool.map(main, offsets)
    pool.close()
    pool.join()
