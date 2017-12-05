#! /usr/bin/python
# coding=utf-8

a=21
b=10
c=0
if( a==b ):
	print "a==b"
else:
	print "a!=b"
if( a!=b ):
	print "a!=b"
else:
	print "a==b"
if( a<>b ):
	print "a<>b"
else:
	print "a==b"
if( a>b ):
	print "a>b"
else:
	print "a <= b"
a=5
b=20
if( a<=b ):
	print "a<=b"
else:
	print "a>b"
if( b>=a ):
	print "b>=a"
else:
	print "b<a"

# bit opt
a = 60
b = 13
print a&b
print a|b
print a^b
print ~a

a=10
b=20
list = [1,2,3,4,5]
if( a in list ):
	print a
else:
	print "not at list"
if( b not in list):
	print "not b at list"
else:
	print b
a=2
if( a in list ):
	print a
else:
	print "a not in list"
