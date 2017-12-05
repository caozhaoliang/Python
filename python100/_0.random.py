#! /usr/bin/python
# coding=utf-8
import random
'''
# 生成0到1之前的随机浮点数
print random.random()

# 生成两个数之间的浮点数
print random.uniform(0,5) 

#生成 两个数之间的随机整数
print random.randint(0,10)

#生成范围内带步长的随机数
print random.randrange(0,20,2)
'''

#从特定序列中取一个元素 可以是字符串，列表 元组等
'''
string = 'nice to meet you'
tup = ('nice','to','meet','you')
lst = ['nice','to','meet','you']
dic = {'a':1,'b':2,'c':3}

print random.choice(string)
print random.choice(tup)
print random.choice(lst)
print random.choice(dic.values())
'''

# 将列表中元素打乱 
'''
lst = ['1','2','3','4','5','6']
random.shuffle(lst)
print lst
'''

# 从序列中取出指定长度片段 打乱，原序列不变
list = [1,2,3,4,5,6,7]
slist = random.sample(list,5)
print slist
print list






















