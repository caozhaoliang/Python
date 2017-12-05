#! /usr/bin/python
# coding=utf-8

h = 0
leap =1
from math import sqrt
from sys import stdout

def isLeap(n):
	k = int(sqrt(n+1))
	for i in range(2,k+1):
		if m%i ==0:
			return False
	else:
		return True

for m in range(101,201):
	b = isLeap(m)
	if b:
		print m
		h+=1
print h


'''
for m in range(101,201):
	k = int(sqrt(m+1))
	for i in range(2,k+1):
		if m % i==0:
			leap =0;
			break
	if leap == 1:
		print '%-4d'%m
		h+=1
		if h%10 ==0:
			print ''
	leap = 1
print 'total is %d'%h
'''

