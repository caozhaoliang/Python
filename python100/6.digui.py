#! /usr/bin/python
#coding=utf-8

def fin(n):
	if n==1 or n == 2:
		return 1
	return fin(n-1)+fin(n-2)

print fin(10)

