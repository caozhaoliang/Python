#! /usr/bin/python
# coding= utf-8

try:
	fh = open("testfile","w")
	fh.write("this is a test file ,just use test Exception")
except IOError:
	print "Error: no such file"
else:
	print " write success "
	fh.close()

