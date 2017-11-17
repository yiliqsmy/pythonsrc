#! python3
# -*- coding: utf-8 -*-
#pdf地址
#本地txt存入MySQL
import pymysql as mdb
import time
start=time.time()
def createTrain():
    try:
        #将con设定为全局连接
        con = mdb.connect(user="root", passwd="", host="localhost", db="test", charset="utf8")#
        with con:
            #获取连接的cursor，
            cur = con.cursor()
            #创建一个数据表 writers(id,name)
            cur.execute("drop table if exists t_pdf")
            cur.execute("create table t_pdf(id int auto_increment primary key,company varchar(20),disclosureTitle varchar(1000),destFilePath varchar(1000))CHARACTER SET utf8")
            #cur.execute("set names 'utf8'")
            f = open("pdfdownurl.txt", "r",encoding='utf-8')
            while True:
                line = f.readline()
                if line:
                    # 处理每行\n
                    line = line.strip('\n')
                    line = line.split(";")
                    print (line)
                    cur.execute("insert into t_pdf(id,company,disclosureTitle,destFilePath) values(NULL,%s,%s,%s)", [line[0], line[1], line[2]])
                else:
                    break
            f.close()


    except Exception as e:
        print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
    cur.close()
    con.commit()
    con.close()



createTrain()
print (time.time()-start)
print ('done')
#0.5541610717773438秒
