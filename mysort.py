#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 10:49:47 2017

@author: louis
"""
 

import random
def part1(list):

	length=len(list)
	count=0
# calculate interval
	while count<=length/3:
		count=count*3+1
	
	while count>=1:
#select value to be inserted 
		for i in range(count,length):
			tmp=list[i]
			for j in range(i,0,-count):
#shift element towards right
				if tmp<list[j-count]:
					list[j]=list[j-count]
				else:
					j+=count
					break
# insert the number at hole position 
			list[j-count]=tmp
#  calculate interval
		count=count//3
		print(list)
 
# make a series of number to be sorted
a=random.sample(range(50),12)
part1(a)
print("result:"+str(a))