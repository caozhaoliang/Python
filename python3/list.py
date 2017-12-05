#! /usr/local/bin/python3
'''
movies=["The Holy Grail","The Life of Brian","The Meaning of Life"]
for item in movies:
	print(item)
	print(len(item))
movies.append("Galaxy Of Heart")
print(movies)
#print(movies.pop())
movies.remove('Galaxy Of Heart')
#movies.insert(0,'Galaxy Of Heart')
print(movies)
movies.insert(1,1975);
movies.insert(3,1979);
movies.insert(5,1983);
print(movies)
'''

def print_lol(the_list,indent=False,level=0):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item,indent,level+1)
		else:
			if indent:
				for tab in range(level):
					print("\t",end=' ')
#				print("\t",* level,end=' ')
			print(each_item)

movies=['The Holy Grail',1975,'Terry Jones & Terry Gilliam',91,
['Graham Chapman',['Michael Pailin','John Cleese','Terry Gilliam','Eric Idle','Terry Jones']]]

#print(movies)
print_lol(movies,True,1)


