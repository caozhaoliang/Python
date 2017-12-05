#! /usr/bin/python
# coding=utf-8

for i in range(1,10001):
	sum = 0;
	lst = []
	for j in range(1,i):
		if i%j ==0:
			sum +=j
			lst.append(j)
	if sum ==i:
		print i
		print lst

