#!/usr/bin/python3

from pprint import pprint as pp
from collections import deque as dq


alist = [54,26,93,17,77,31,44,55,20]

agraph = {'A': set('BC'),
         'B': set('ADE'),
         'C': set('AF'),
         'D': set('B'),
         'E': set('BF'),
         'F': set('CE')}

aqueue = dq([2],4)
dq.enqueue(3)
print(aqueue)