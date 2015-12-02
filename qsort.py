#!/usr/bin/python3

def qsort(alist):
	if len(alist)< 2:
		return alist
	else:
		pivot = alist[0]
		low = [i for i in alist if i < pivot]
		mid = [i for i in alist if i == pivot]
		high = [i for i in alist if i > pivot]
		return qsort(low) + mid + qsort(high)

