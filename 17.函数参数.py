#! /usr/bin/python
# coding=utf-8

# python 的传值不能说是值传递还是引用传递，只能说是传可变对象
#与不可变对象

def ChangeInt(a):
	a = 10;

# 传可变对象
def ChangeMe( mylist1 ):
	mylist1.append([1,2,3,4]);
	print "函数内取值：",mylist1
	return

# 参数顺序可以不同
def PrintInfo(name ,age):
	print "Name:",name;
	print "Age:",age;
	return

# 缺省参数
def PrintMiss( name, age = 35):
	print "Name:",name;
	print "Age:",age;
	return

# 不定长参数
def function(arg1,*vartuple):
	print arg1
	for var in vartuple:
		print var
	return

function(10);
function(70,60,50);
'''
PrintMiss(age=50,name = "liang");
PrintMiss(name = "liang");

PrintInfo(age=13,name="liang");

mylist = [10,20,30];
ChangeMe(mylist);
print "函数外取值：",mylist

b=2;
ChangeInt(b)
print b; # 依然是2
'''
