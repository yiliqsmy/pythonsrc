#!/usr/bin/env python3   可用
#coding: utf-8  

import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msgFrom = 'xxxxxxxxx@163.com' #从该邮箱发送
msgTo = 'xxxxxxxxxx@qq.com' #发送到该邮箱
smtpSever='smtp.163.com' # 163邮箱的smtp Sever地址
smtpPort = '25' #开放的端口
sqm='xxxxx'  # 在登录smtp时需要login中的密码应当使用授权码而非账户密码

msg['from'] = msgFrom
msg['to'] = msgTo
msg['subject'] = 'Python自动邮件-'
content = '''
你好:
    这是一封python3发送给qq的邮件
'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)
smtp = smtplib
smtp = smtplib.SMTP()
'''
smtplib的connect（连接到邮件服务器）、login（登陆验证）、sendmail（发送邮件）
'''
smtp.connect(smtpSever, smtpPort)
smtp.login(msgFrom, sqm)
smtp.sendmail(msgFrom, msgTo, str(msg))
print('发送成功')
# s = smtplib.SMTP("localhost")
# s.send_message(msg)
smtp.quit()
