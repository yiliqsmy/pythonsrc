#! python3
#coding=utf-8
#测试findall
from bs4 import BeautifulSoup
import lxml

if __name__ == '__main__':
    s = BeautifulSoup(open('test.html'), "html.parser")
    print  (s.prettify())
    print  ("------------------------------")
    print (s.find('p'))
    print (s.find_all('p'))
    print ("------------------------------")
    print (s.find('p', id='one'))
    print (s.find_all('p', id='one'))
    print ("------------------------------")
    print (s.find('p', id="two"))
    print (s.find_all('p', id="two"))
    print ("------------------------------")
    print (s.find('p', id="three"))
    print (s.find_all('p', id="three"))
    print ("------------------------------")
    print (s.find('p', id="four"))
    print (s.find_all('p', id="four"))
    print ("------------------------------")
