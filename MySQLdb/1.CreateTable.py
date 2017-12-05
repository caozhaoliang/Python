#! /usr/bin/python
# coding=utf-8

import MySQLdb

db = MySQLdb.connect("localhost","root","1234","python_test")

cursor = db.cursor()
# 创建表
'''
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql = """CREATE TABLE EMPLOYEE (
			FIRST_NAME CHAR(20) NOT NULL,
			LAST_NAME CHAR(20),
			AGE INT,
			SEX CHAR(1),
			INCOME FLOAT)"""
'''
# 插入数据
'''
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
		VALUES('Mac','Mo',20,'M',3000)"""
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()

'''
# 查询数据
'''
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'"%(1000)
try:
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		fname = row[0]
		lname = row[1]
		age = row[2]
		sex = row[3]
		income = row[4]
		print "fname=%s,lname=%s,age=%d,sex=%s,income=%s"%(fname,lname,age,sex,income)
except:
	print "Error: unable to fecth data"
'''
# 更新数据库
'''
sql = "UPDATE EMPLOYEE SET AGE = AGE+1 WHERE SEX = '%c'"%('M')
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()
'''
# 删除数据
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'"%(20)
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()


#cursor.execute(sql)
db.close()







