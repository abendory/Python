"""
gooby = [5,7,3,8,2,4,6,9,1]
   [5,7,3,8,2]         [4,6,9,1]
[5,7,3]    [8,2]      [4,6]   [9,1]
[5,7] [3] [8] [2]    [4][6]  [9][1]
[5][7]

[5,7] [3]  [8] [2]  [4][6]  [1][9]
[3,5,7]     [2,8]    [4,6]   [1,9]
    [2,3,5,7,8]        [1,4,6,9]
        [1,2,3,4,5,6,7,8,9]

"""

def merge_sort(alist):
	if len(alist) > 1: 
		mid = len(alist) // 2
		left = alist[:mid] 
		right = alist[mid:]

		merge_sort(left)
		merge_sort(right)

		i=j=k=0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				alist[k] = left[i]
				i+=1
			else:
				alist[k] = right[j]
				j+=1
			k+=1

		while i < len(left):
			alist[k] = left[i]
			i+=1
			k+=1

		while j < len(right):
			alist[k] = right[j]
			j+=1
			k+=1
