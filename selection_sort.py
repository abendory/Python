#!/usr/bin/python3

#gooby = [5,7,3,8,2,4,6,9,1]
#gooby = [1,7,3,8,2,4,6,9,5]
#gooby = [1,2,3,8,7,4,6,9,5]
#gooby = [1,2,3,8,7,4,6,9,5]
#gooby = [1,2,3,4,7,8,6,9,5]

def selection_sort(alist): 
	for i in range(len(alist)):
		min_index = i
		for j in range(i+1, len(alist)):
			if alist[j] < alist[min_index]: 
				min_index = j
		alist[i], alist[min_index] = alist[min_index], alist[i]





