#! /usr/bin/python
# coding=utf-8

import string
s=raw_input('input a string:\n')
letters = space=digit= others=0

for c in s:
	if c.isalpha():
		letters+=1;
	elif c.isspace():
		space+=1;
	elif c.isdigit():
		digit +=1;
	else:
		others+=1
print 'char=%d,space=%d,digit=%d,others=%d'%(letters,space,digit,others)




