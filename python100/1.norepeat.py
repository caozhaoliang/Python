#! /usr/bin/python
# coding = utf-8


'''
count = 0;

for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if( i != j) and (i != k)and (j != k):
				count = count + 1
				print i,j,k

print count
'''

from itertools import permutations
for i in permutations([1,2,3,4],3):
	k = ''
	for j in range(0,len(i)):
		k = k + str(i[j])
	print (int(k))



