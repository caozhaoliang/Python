#! /usr/bin/python
# coding=utf-8

rows = int(raw_input('输入列数：'))
i=j=k=1
print '打印等腰直角三角形'
for i in range(0,rows):
	for k in range(0,i+1):
		print "*",
		k +=1
	i+=1
	print '\n'
