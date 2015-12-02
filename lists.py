"""
Simple Data Structures
Includes Linked List, Queue, and Stack
Three implementations of Queue: Queue, Improved Queue, and Priority Queue
"""

import numpy as np
from pprint import pprint as pp
from random import randrange

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next  = next

    def __str__(self):
        return "node data = " + str(self.data)

    def print_list(self):
        current = self
        while current != None:
            if current.next == None:
                print (str(current.data),end="")
            else:
                print (str(current.data),end=", ")
            current = current.next

    def print_backward(self):
        if self.next != None:
            tail = self.next
            tail.print_backward()
        print (self.data),

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head   = None

    def __str__(self):
        return "head data = " + str(self.head.data)

    def is_empty(self):
        return (self.head is None)

    def insert(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length = self.length + 1

    def make_circular(self,data):
        node = Node(data)
        node.next = None
        if self.head == None:
            # if list is empty the new node goes first
            self.head = node
        else:
            # find the last node in the list
            last = self.head
            while last.next: last = last.next
            # append the new node
            last.next = node
            # point the new node to the head
            node.next = self.head
        self.length = self.length + 1

    def delete(self, data):
        prev = None
        current = self.head
        while current.data is not None:
            if current.data is data:
                break
            prev = current
            current = current.next

        # deleted node is not present
        if current.data is None:
            return self.head

        # deleted node is first node
        if current is self.head:
            return current.next

        # otherwise
        prev.next = current.next
        return self.head

    def delete_first(self):
        data = self.head.data
        self.head = self.head.next
        self.length = self.length - 1
        return data

    """Return True if linked list is circular, else False.
    This works by keeping two pointers, faster and slower. 
    Faster is incremented twice each iteration and slower 
    is incremented once. If there is a collision, then we 
    know it is a circular list, if faster is None, we know 
    the list is not circular."""
    def is_circular(self):
        slower = self.head
        faster = self.head.next
        while True:
            if faster is None or faster.next is None:
                return False  # list isn't circular 
            elif faster is slower or faster.next is slower:
                return True
            else:
                slower = slower.next       #advance once
                faster = faster.next.next  #advance twice

    def print_list(self):
        if not self.is_circular():   
            print ("[",end="")
            if self.head != None:
                self.head.print_list()
            print ("]")
        else:
            print ("Circular List")

    def print_backward(self):
        print ("["),
        if self.head != None:
            self.head.print_backward()
        print ("]")

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return (self.length == 0)

    def insert(self, data):
        node = Node(data)
        node.next = None
        if self.head == None:
            # if list is empty the new node goes first
            self.head = node
        else:
            # find the last node in the list
            last = self.head
            while last.next: last = last.next
            # append the new node
            last.next = node
        self.length = self.length + 1

    def remove(self):
        data = self.head.data
        self.head = self.head.next
        self.length = self.length - 1
        return data

    def print_queue(self):
        print ("[",end="")
        while not self.is_empty():
            if self.length==1:
                print (self.remove(),end="")
            else:
                print (str(self.remove()),end=", ")
        print ("]")

class ImprovedQueue(Queue):
    def __init__(self):
        self.length = 0
        self.head   = None
        self.tail   = None

    def is_empty(self):
        return (self.length == 0)

    def insert(self, data):
        node = Node(data)
        node.next = None
        if self.length == 0:
            # if list is empty, the new node is head and last
            self.head = self.tail = node
        else:
            # find the last node
            last = self.tail
            # append the new node
            last.next = node
            self.tail = node
        self.length = self.length + 1

    def remove(self):
        data = self.head.data
        self.head = self.head.next
        self.length = self.length - 1
        if self.length == 0:
            self.tail = None
        return data

# Inefficient (using linked list instead of binary heap)
class PriorityQueue(Queue):
    def __init__(self):
        self.items = []
        self.length = 0

    def is_empty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)
        self.length += 1

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]: maxi = i
        item = self.items[maxi]
        self.items[maxi:maxi+1] = []
        self.length -= 1
        return item

my_list = [1,7,4,2,9,3,6,8,0,5]
random_list = [randrange(100) for i in range(20)]

# Linked List
title = "Linked List"
print (title)
print ("=" * len(title))

ll = LinkedList()
for i in range(len(my_list)):
    ll.insert(my_list[i])

ll.print_list(); print()

# Queue
title = "Queue"
print (title)
print ("=" * len(title))

q = Queue()
for i in range(len(my_list)):
    q.insert(my_list[i])

q.print_queue(); print()

# IQueue
title = "Improved Queue"
print (title)
print ("=" * len(title))

iq = Queue()
for i in range(len(my_list)):
    iq.insert(my_list[i])

iq.print_queue(); print()

# PQueue
title = "Priority Queue"
print (title)
print ("=" * len(title))

pq = PriorityQueue()
for i in range(len(my_list)):
    pq.insert(my_list[i])

pq.print_queue(); print()

# Test for a circular linked list
title = "Print a circular linked list"
print (title)
print ("=" * len(title))

# create a circular list
ll = LinkedList()
for i in range(len(my_list)):
    ll.insert(my_list[i])
ll.make_circular(4)

ll.print_list()