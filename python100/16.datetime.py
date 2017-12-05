#! /usr/bin/python
# coding=utf-8

import datetime

if __name__ == '__main__':
	# 输出今日日期，格式为 dd/mm/yyyy
	print(datetime.date.today().strftime('%d/%m/%Y'))
	#创建日期对象
	mydate = datetime.date(1941,1,5)
	print(mydate.strftime('%d/%m/%Y'))

	#日期算数运算
	mydateNextday = mydate + datetime.timedelta(days=1)
	print(mydateNextday.strftime('%d/%m/%Y'))

	#日期替换
	myfdate = mydate.replace(year=mydate.year+1)
	print( myfdate.strftime('%d/%m/%Y'))




