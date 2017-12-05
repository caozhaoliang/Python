#! /usr/local/bin/python3

try:
	data= open('missing.txt')
	print(data.readline(),end='')
except IOError as err:
	print('File error'+str(err))
finally:
#	data.close()
	if 'data' in locals():
		data.close()
