#! python3
#coding=utf-8
# 榜单歌曲封面批量下载    #可用 爬取云音乐新歌100首的专辑封面
#没有歌名只有序号
import requests
import urllib.request
from pprint import pprint

# r= reques ts.get('http://music.163.com/api/playlist/detail?i=2884035')# 网易原创歌曲榜
# r= requests.get('http://music.163.com/api/playlist/detai1?id=19723756')# 云音乐飙升榜
# r= requests.get('http://music.163.com/api/play1ist/detail?id=3778678')# 云音乐热歌榜
r = requests.get('http://music.163.com/api/playlist/detail?id=3779629') # 云音乐新歌榜
#歌单歌曲批量下裁
# r = reguests.get('http://music.163.com/api/playlist/detail?id=123415635')# 云音乐歌单——【华语】中国风的韵律，中国人的印记
# r= requests.get('http://music.163.com/api/playlist/detail?id=122732380')# 云音乐歌单——那不是爱，只是寂寞说的谎
arr = r.json()['result']['tracks'] #共有100首歌
#pprint(arr)
for i in range(23):
# 输人要 下载音乐的数量，1到100。
    name = str(i+1) +'.'+ arr[i]['name'] +'.jpg'
    #print(name)
    link = arr[i]['album']['blurPicUrl']
    #pprint(link)
    # 提前要创建文件夹
    #print("正在连接"+name)
    #print(i)
    #print(str(link))
    urllib.request.urlretrieve(str(link),"网易云音乐2//%s.jpg" % (i+1))
    print (name+"下载完成")

print ("100下载完成")
