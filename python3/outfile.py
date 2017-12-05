#! /usr/local/bin/python3

man =[]
other=[]
try:
	data = open('sketch.txt')
	for each_line in data:
		try:
			(role,line_spoken)=each_line.split(':',1)
			line_spoken = line_spoken.strip()
			if role == 'Man said':
				man.append(line_spoken)
			elif role == 'Other Man said':
				other.append(line_spoken)
		except ValueError:
			pass
	data.close()
except IOError:
	print('The data file is missing')
'''
try:
	man_file = open('man_data.txt','w')
	other_file=open('other_data.txt','w')
	print(man,file=man_file)
	print(other,file=other_file)
	
except IOError:
	print('File error')
finally:
	man_file.close()
	other_file.close()
'''
try:
	with open('man_data.txt','w') as man_file:
		print(man,file=man_file)
	with open('other_data.txt','w') as other_file:
		print(other,file=other_file)
except IOError as err:
	print('Error:'+str(err))



	
