def max_subarray(A):
	
	if len(A)<1: return 0

	curr_max = global_max = A[0]

	for i in xrange(1,len(A)):
		if curr_max < 0:
			curr_max = A[i]
		else:
			curr_max += A[i]

		if global_max < curr_max:
			global_max = curr_max
		
		print curr_max, global_max
	return global_max

print max_subarray([-3,4,-2,2,3,4,5,-3,5,3])