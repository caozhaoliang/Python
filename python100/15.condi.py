#! /usr/bin/python
# coding=utf-8

score = int(raw_input('输入分数：'))

if score >=90:
	grade = 'A'
elif score >=60:
	grade = 'B'
else:
	grade = 'C'

print '%d 属于%s'%(score,grade)



