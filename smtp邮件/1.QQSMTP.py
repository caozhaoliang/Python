#! /usr/bin/python
#coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '1073810085@qq.com'
my_pass = 'zhgvwvveevrcibbh'
mu_user = '1073810085@qq.com'

def mail():
	ret = True
	try:
		msg = MIMEText('填写邮件内容','plain','utf-8')
		msg['From']=formataddr(["zhaoliang.cao",my_sender])
		msg['To']=formataddr(["FK",my_user])
		msg['Subject']="Title for Test"

		server = smtplib.SMTP_SSL("smtp.qq.com",465)
		server.login(my_sender,my_pass)
		server.sendmail(my_sender,[my_user,],msg.as_string())
		server.quit()
	except Exception:
		ret = False
	return ret
ret = mail()
if ret:
	print "邮件发送成功"
else:
	print "邮件发送失败"
		

