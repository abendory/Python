#!/usr/bin/python3

def bubble_sort(s):
	done = False
	while not done:
		done = True
		for i in range(0,len(s)-1):
			if s[i] > s[i+1]:
				s[i], s[i+1] = s[i+1], s[i]
				done = False

