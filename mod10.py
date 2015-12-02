#!/usr/local/bin/python2

import sys

def mod10(a,b):
	# Edge cases
	if a==0 and b==0: return "Error: Divide by Zero" 
	if a < 0 or b < 0: return "Error: Enter a positive integer"
	if a==1 or b==0: return 1
	
	ones_digit = { 0: [0^1%10, 0^2%10, 0^3%10, 0^4%10], #[0,0,0,0]
				   1: [1^1%10, 1^2%10, 1^3%10, 1^4%10], #[1,1,1,1]
				   2: [2^1%10, 2^2%10, 2^3%10, 2^4%10], #[2,4,8,6]
				   3: [3^1%10, 3^2%10, 3^3%10, 3^4%10], #[3,9,7,1]
				   4: [4^1%10, 4^2%10, 4^3%10, 4^4%10], #[4,6,4,6] 
				   5: [5^1%10, 5^2%10, 5^3%10, 5^4%10], #[5,5,5,5]
				   6: [6] , 
				   7: [7,9,3,1],  
				   8: [8,4,2,6], 
				   9: [9,1] }

	if a % 10 == 0:
		return 0
	elif a % 10 == 1:
		return 1
		(a%10)^(b%4)%10,
	elif a % 10 == 2:
		return ones_digit[2][(b%4)-1]
	elif a % 10 == 3:
		return ones_digit[3][(b%4)-1]
	elif a % 10 == 4:
		return ones_digit[4][(b%2)-1]
	elif a % 10 == 5:
		return 5
	elif a % 10 == 6:
		return 6
	elif a % 10 == 7:
		return ones_digit[7][(b%4)-1]
	elif a % 10 == 8:
		return ones_digit[8][(b%4)-1]
	elif a % 10 == 9:
		return ones_digit[9][(b%2)-1]
	else: print "Unknown Error"

	#return (a**b)%10

if __name__ == "__main__":
	# Test cases

	for a in range(20):
		for b in range(20):
			print "{0}^{1} mod 10 = {2}".format(a, b, mod10(a,b))
	for a in range(20):
		print "{0}^{1} mod 10 = {2}".format(a, sys.maxint, mod10(a,sys.maxint))
	for b in range(20):
		print "{0}^{1} mod 10 = {2}".format(sys.maxint, b, mod10(sys.maxint,b))

	print "{0}^{1} mod 10 = {2}".format(sys.maxint, sys.maxint, mod10(sys.maxint,sys.maxint))

