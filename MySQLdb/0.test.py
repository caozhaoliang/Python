#! /usr/bin/python
# coding=utf-8

import MySQLdb

db = MySQLdb.connect("localhost","root","1234","python_test")

# 0 获取游标
cursor = db.cursor()
# 1 执行查询
cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print "Database version:%s" % data

# 关闭连接
db.close()
