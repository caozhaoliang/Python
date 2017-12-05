#! /usr/bin/python
#coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@runoob.com'
receivers = ['1073810085@qq.com']

message = MIMEText("Python 邮件发送测试...","plain","utf-8")
message['From']=Header("Linux测试",'utf-8')
message['To'] = Header('测试','utf-8')

subJect = "Python SMTP 有检测试"
message['Subject'] = Header(subJect,'utf-8')

try:
	smtpObj = smtplib.SMTP('localhost')
	smtpObj.sendmail(sender,receivers,message.as_string())
	print "邮件发送成功"
except smtplib.SMTPException:
	print "Error: 无法发送邮件"

	

