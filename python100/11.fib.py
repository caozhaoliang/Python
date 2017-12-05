#! /usr/bin/python
# coding=utf-8

f1=1
f2=1
for r in range(1,22):
	print '%12ld %12ld'%(f1,f2),
	if(r%3) == 0:
		print ''
	f1=f1+f2
	f2=f1+f2



