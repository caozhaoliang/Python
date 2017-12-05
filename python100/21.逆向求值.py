#! /usr/bin/python
# coding=utf-8

'''
x2=1
for day in range(9,0,-1):
	x1 = (x2+1)*2
	x2 = x1
print x2
'''

def taozi(n):
	if n==1:
		return 1
	else:
		return (taozi(n-1)+1)*2

print taozi(10)


