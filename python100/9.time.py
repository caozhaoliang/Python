#! /usr/bin/python
# coding=utf-8
import time
import random

'''
myD = {1:'a',2:'b'}

for key,value in dict.items(myD):
	print key,value
	time.sleep(1)
'''

#打印，暂停时间在一定范围内随机

lst =['鹅鹅鹅','曲项向天歌','白毛浮绿水','红掌拨清波']
for item in lst:
	t=float("%.2f"%random.uniform(0,2))
	time.sleep(t)
	print item



