#!/usr/bin/python3

#gooby = [5|7,3,8,2,4,6,9,1]
#gooby = [5,7|3,8,2,4,6,9,1]
#gooby = [3,5,7|8,2,4,6,9,1]
#gooby = [3,5,7,8|2,4,6,9,1]
#gooby = [2,3,5,7,8|4,6,9,1]

def insertion_sort(alist):
	for i in range(1,len(alist)):
		current_value = alist[i]
		j = i
		while j>0 and alist[j-1] > current_value:
			alist[j] = alist[j-1]
			j = j-1
		alist[j] = current_value
