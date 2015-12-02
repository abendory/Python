#!/usr/local/bin/python3

import sys

# My solution
def mod10(a,b): 
    # Edge cases
    if a == 0 and b == 0: return "Error: Undefined"
    if a < 0 or b < 0: return "Error: Enter a positive integer"
    if b == 0: return 1
    
    if b%4 == 0: 
        return ((a%10)**4)%10    # to handle 4%4 = 0
    else: 
        return ((a%10)**(b%4))%10         

if __name__ == "__main__":
	# Test cases
	for a in range(10):
		for b in range(10):
			print ("mod10({0},{1}) = {2}".format(a, b, mod10(a,b)))
