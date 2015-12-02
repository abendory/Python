#!/usr/bin/env python3
# Addie Bendory, Python Code Samples

import random

array = [2,4,5,7,9,10]


def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if alist[mid] == item:
            found = True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return found

def bubbleSort(alist):
  list_sorted = False
  while not list_sorted: 
    list_sorted = True
    for cur in range(len(alist) - 1):
      if alist[cur] > alist[cur + 1]:
        list_sorted = False
        alist[cur], alist[cur + 1] = alist[cur + 1], alist[cur] 

def selectionSort(alist):
  for cur in range(len(alist)):
    min_pos = cur
    for list_pos in range(cur + 1,len(alist)):
      if (alist[list_pos] < alist[min_pos]):
        min_pos = list_pos
    if alist[cur] != alist[min_pos]:
      alist[cur], alist[min_pos] = alist[min_pos], alist[cur]

def insertionSort(alist, start=0, gap=1):
  for cur in range(start+gap, len(alist), gap):
    current_value = alist[cur]
    pos = cur
    while (pos >= gap and alist[pos-gap] > current_value):  # scan from right to left
      alist[pos] = alist[pos-gap]
      pos -= gap
    alist[pos] = current_value

def shellSort(alist):
  sublist = len(alist) // 2
  while sublist > 0:
    for start in range(sublist):
      insertionSort(alist, start, sublist)
    sublist //= 2

def mergeSort(alist):
  if len(alist)>1:
    mid = len(alist)//2
    lefthalf = alist[:mid]
    righthalf = alist[mid:]
    mergeSort(lefthalf)
    mergeSort(righthalf)

    i=j=k=0 # lefthalf (i), righthalf (j), and alist (k) indices
    while (i < len(lefthalf) and j < len(righthalf)):
      if lefthalf[i] < righthalf[j]:
        alist[k]=lefthalf[i]
        i=i+1
      else:
        alist[k]=righthalf[j]
        j=j+1
      k=k+1

    while i < len(lefthalf):
      alist[k]=lefthalf[i]
      i=i+1
      k=k+1

    while j < len(righthalf):
      alist[k]=righthalf[j]
      j=j+1
      k=k+1

def heapSort(alist):
  pass

def quickSort(alist):
  # set a pivot to first element 
  pivot = alist[0]
  left = alist[1]
  right = alist[-1]
  if left < pivot: pivot = alist[1]

def quick3Sort(alist):
  pass

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

##################### TEST FUNCTIONS ####################

def create_random():
    alist = [random.randrange(100) for i in range(10)]
    return alist

def print_list(alist):
    for item in alist:
        print("{:3}".format(item), end="")
    print()

def print_sort(sort, alist):
    print ("Random List: ", end=""); print_list(alist)
    sort(alist)
    print ("Sorted List: ", end=""); print_list(alist)
    print ("*"*43)

def print_search(search, alist, item):
    print ("Random List: ", end=""); print_list(alist)
    print ("Searching for " + str(item))
    found = search(alist, item)
    print ("Was item found? " + str(found))
    print ("*"*43)

# Run the algorithms

print ("Binary Search")
print ("-------------")
print_search(binarySearch, sorted([22,41,57,11,68,83,36,70,45]), random.randrange(100))

print ("Bubble Sort")
print ("-----------")
print_sort(bubbleSort, create_random())

print ("Selection Sort")
print ("--------------")
print_sort(selectionSort, create_random())

print ("Insertion Sort")
print ("--------------")
print_sort(insertionSort, create_random())

print ("Shell Sort")
print ("----------")
print_sort(shellSort, create_random())

print ("Merge Sort")
print ("----------")
print_sort(mergeSort, create_random())

print ("Heap Sort")
print ("---------")
print_sort(heapSort, create_random())

print ("Quick Sort")
print ("----------")
print_sort(quickSort, create_random())

print ("Quick3 Sort")
print ("-----------")
print_sort(quick3Sort, create_random())