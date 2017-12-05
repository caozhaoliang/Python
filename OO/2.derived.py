#! /usr/bin/python
# coding=utf-8
class Parent:
	parentAttr = 100
	def __init__(self):
		print "调用父类构造"
	def parentMethod(self):
		print "调用父类方法"
	def setAttr(self, attr):
		Parent.parentAttr = attr;

	def getAttr(self):
		print "父类属性：",Parent.parentAttr
	def over(self):
		print "over parent"

class Child(Parent):
	def __init__(self):
		print "调用子类构造"

	def childMethod(self):
		print "调用子类方法"
	def over(self):
		print "over child"

c=Child();
c.childMethod()

c.parentMethod()

c.setAttr(200)

c.getAttr()

c.over()

