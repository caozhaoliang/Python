#! /usr/bin/python
# coding=utf-8

import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host,port))

s.listen(5)

while True:
	c,addr = s.accept()
	print '链接地址:',addr
	c.send("欢迎访问测试服务!")
	c.close()
