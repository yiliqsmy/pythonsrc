#! python3
#coding=utf-8
from selenium import webdriver
import time
start =time.clock()
driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.get('https://mp.weixin.qq.com/')
time.sleep(2)
driver.find_element_by_xpath("./*//input[@name='account']").clear()
driver.find_element_by_xpath("./*//input[@name='account']").send_keys('xxxxxxxxxxx@qq.com')
driver.find_element_by_xpath("./*//input[@name='password']").clear()

driver.find_element_by_xpath("./*//input[@name='password']").send_keys('xxxxxxxx')
time.sleep(20)# 拿手机扫二维码！#driver.get('https://mp.weixin.qq.com/')
html = driver.page_source
print(html)
print("保存成功")    
driver.find_element_by_xpath("./*//a[@data-id='10014']").click()
print("首页")
time.sleep(9)
html = driver.page_source
print(html)
driver.find_element_by_xpath("./*//a[@class='btn btn_primary']").click()
print("素材管理")
time.sleep(9)
html = driver.page_source
print(html)
driver.find_element_by_xpath("./*//div[@id='edui23_state']").click()
html = driver.page_source
print(html)
print("素材管理")
print('完成下载')
end = time.clock()
print('Running time: %s Seconds' % (end - start))
