#! /usr/bin/python
# -*- coding:UTF-8 -*-

import pickle

shoplistfile = 'shoplist.data'

shoplist=['apple','mango','carrot','eggs']

dic = ()
dic = shoplist

f = open(shoplistfile,'wb')

pickle.dump(dic,f)
f.close()

del dic

f = open(shoplistfile,'rb')
storedic = pickle.load(f)
print storedic


'''
f = open(shoplistfile,'wb')

pickle.dump(shoplist,f)
f.close()

del shoplist

f=open(shoplistfile,'rb')
storedlist = pickle.load(f)
print storedlist
'''



