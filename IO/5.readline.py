#! /usr/bin/python
#coding=utf-8

# 读取一行
'''
fileHandle = open('test.txt')

print fileHandle.readline()
fileHandle.close()
'''

# 读取多行
'''
fd = open('test.txt')

flist = fd.readlines()
for i in flist:
	print '>>',i

fd.close()
'''

#读取字节
fd = open('test.txt')
print fd.read(2)

fd.seek(4)
print fd.read(1)


