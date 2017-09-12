#! python3
#coding=utf-8
#爬取糗事百科段子
#可用， 批量下载文章，导入Excel文件。
import urllib.request
import requests
import re
from lxml.html.clean import Cleaner
#from lxml import etree
from lxml import cssselect
from bs4 import BeautifulSoup

url="https://www.qiushibaike.com/text/"
def do_get_request(self, url, headers=None, timeout=3, is_return_text=True, num_retries=2):
  if url is None:
    print('Downloading:', url)
  if headers is None:  # 默认请求头
    headers = {
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
  response = None
  try:
         response = requests.get(url, headers=headers, timeout=timeout)
         response.raise_for_status()  # a 4XX client error or 5XX server error response,raise requests.exceptions.HTTPError
         if response.status_code == requests.codes.ok:
            if is_return_text:
                 html = response.text
                 print(html)
            else:
                 html = response.json()
                 print(html)
         else:
            html = None
         print(html)
  except requests.Timeout as err:
          print('Downloading Timeout:', err.args)
          html = None
  except requests.HTTPError as err:
          print('Downloading HTTP Error,msg:{0}'.format(err.args))
          html = None
          if num_retries > 0:
            if 500 <= response.status_code < 600:
                 return self.do_get_request(url, headers=headers, num_retries=num_retries - 1)  # 服务器错误，导致请求失败，默认重试2次
  except requests.ConnectionError as err:
          print('Downloading Connection Error:', err.args)
          html = None

  return html
  print(html)

def duanzi_scrapter(html_doc, page_num=1):
      html_after_cleaner = cleaner.clean_html(html_doc)
      # 去除段子内容中的<br>
      pattern = re.compile('<br>|\n')
      html_after_cleaner = re.sub(pattern, '', html_after_cleaner)
      document = etree.fromstring(html_after_cleaner, parser)
      print('正在解析第%s页段子...' % str(page_num))
      try:
         sel = cssselect.CSSSelector('#content-left > div')
         for e in sel(document):

             try:
                 # a content  获取段子信息
                 a = e.find('.//a[@class="contentHerf"]')
                 a_href = a.attrib['href']  # 格式/article/105323928
                 spans = e.findall('.//a[@class="contentHerf"]/div/span')
                 if len(spans) > 1:  # 出现“查看全文”
                     urls.add_new_url(a_href)  # 保存段子链接
                 else:
                     duanzi_info = {}
                     duanzi_info['dz_url'] = 'https://www.qiushibaike.com' + a_href  # 段子链接地址
                     duanzi_info['dzContent'] = spans[0].text  # 段子内容

                     # div stats
                     spans = e.findall('.//div[@class="stats"]/span')
                     for span in spans:
                         i = span.find('.//i')
                         if span.get('class') == 'stats-vote':
                             duanzi_info['vote_num'] = i.text  # 投票数
                         elif span.get('class') == 'stats-comments':  # 评论数
                             duanzi_info['comment_num'] = i.text
                     collect_data(duanzi_info)

             except Exception as err:
                 print('提取段子异常，进入下一循环')
                 continue
         print('解析第%s页段子结束' % str(page_num))
         next_page(page_num + 1)  # 进入下一页
      except TimeoutException as err:
         print('解析网页出错:', err.args)
         return next_page(page_num + 1)   # 捕获异常，直接进入下一页
