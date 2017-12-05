#! /usr/bin/python
# coding=utf-8

Tn = 0;

n = int(raw_input('n= '))
a = int(raw_input('a= '))

def num(n,time):
	l = []
	c = 0
	while time >0:
		l.append(str(n))
		time -=1
	for i in l:
		c = c*10+int(i)
	return c

for i in range(a+1):
	j = num(n,i)
	Tn +=j
print Tn
	
	


