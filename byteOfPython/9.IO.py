#! /usr/bin/python
# -*- coding:UTF-8 -*-

def reverse(text):
	return text[::-1]

def is_palindrome(text):
	lst=[]
	for i in text:
		if i.isalpha():
			lst.append(i)
	tmp = ''.join(lst)
	tmp = tmp.lower()
	print tmp
	return tmp == reverse(tmp)

something = raw_input("Enter text:")

if is_palindrome(something):
	print "Yes, it is a palindrome"
else:
	print 'No, is is not a palindrome'

