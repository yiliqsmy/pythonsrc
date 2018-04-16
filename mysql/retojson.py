#! python3
#coding=utf-8
#获取txt转换为json
#可用
from pprint import pprint
import json
f = open("yyszu.txt", "r")
f2 = open('getuidata.txt', 'w+')
jsonData=[]
result = {}
while True:
  line = f.readline()
  if line:
                    # 处理每行\n
                    line = line.strip('\n')
                    line = line.split(";")
                    result["title"] = line[0]
                    result["tag"]=""
                    result["href"] = line[1]
                    result["time"] = "2017-11-23"
                    jsonData.append(result)
                    jsondatar = json.dumps(jsonData, ensure_ascii=False)  # 去除首尾的中括号
                    pprint(result)
                    print(",")
                    f2.write(str(result))


  else:
      break


#pprint(jsondatar)
f.close()
#pprint(jsonData)
print("重写完成")


# 写数据

# 关闭文件
f2.close()
