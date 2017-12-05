#! /usr/bin/python
# coding = utf-8


import urllib2
import cookielib

filename = 'bdcookie.txt'

cookie = cookielib.MozillaCookieJar(filename)

handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)
'''
for item in cookie:
	print 'Name = '+item.name
	print 'Value= '+item.value
'''

'''
import cookielib
import urllib2

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)


'''
