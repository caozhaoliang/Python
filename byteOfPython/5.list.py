#! /usr/bin/python
# -*- coding:UTF-8 -*-

shoplst = ['apple','mango','carrot','banana']
# 指向同一个对象
mylist = shoplst

del shoplst[0]

print shoplst
print mylist

# 对象切片，新的副本
mylist = shoplst[:]

del mylist[0]

print shoplst

print mylist


