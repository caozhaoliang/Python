#! /usr/bin/python
# coding=utf-8

import time;

ticks = time.time()
print "当前时间戳为：",ticks
'''
localtime = time.localtime(time.time())
print "本地时间为：",localtime
'''
asctime = time.asctime(time.localtime(time.time()))
print "本地时间易读：",asctime

# 格式化成YYYY-MM-DD HH:mm:ss形式
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

# 格式化成 Sat Mar 28 22:24:20 2017 格式
print time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())

# 将字符串转换为时间戳
a = "Tue Nov 14 11:17:00 2017"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))


