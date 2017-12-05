#! /usr/bin/python
# coding=utf-8

fo = open("./a.txt","r+")
#fo.write("abcdefg");
str = fo.read(10);
print "读取的字符串是：",str

position = fo.tell();
print "当前位置：",position
position = fo.seek(0,0)
str = fo.read(10)
print "重新读取字符串：",str
fo.close()
'''
print "文件名：",fo.name
print "is Closed:",fo.closed
print "访问模式：",fo.mode
print "末尾是否强制加空格",fo.softspace
'''
