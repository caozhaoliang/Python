#! /usr/bin/python
# coding=utf-8

def printme(str):
	print str;
	return;
# return
def sum(arg1,arg2):
	total = arg1+arg2
	print "函数内total:",total;
	return total;

# 局部变量和全局变量
total = 0; # global

def sum1( arg1, arg2):
	total = arg1+ arg2; #local
	print "局部变量total的值：",total;
	return 
sum1(10,30);
print "全局变量total的值", total


'''
total = sum(10,20)
print "函数外total:",total;

printme("func do");
printme("do again");
'''
