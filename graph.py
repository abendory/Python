import numpy as np
from pprint import pprint as pp

# Globals
a, b, c, d, e, f, g, h = range(8) 
inf = _ = float('inf')  # defining '_' as infinity

###### Adjacency Lists ########

# Adjacency Set Representation
N1 = [
        {b, c, d, e, f}, #a 
        {c, e},          #b 
        {d},             #c 
        {e},             #d 
        {f},             #e 
        {c, g, h},       #f 
        {f, h},          #g 
        {f, g}           #h
]

# Adjacency Lists
N2 = [
        [b, c, d, e, f], #a 
        [c, e],          #b 
        [d],             #c 
        [e],             #d 
        [f],             #e 
        [c, g, h],       #f 
        [f, h],          #g 
        [f, g]           #h
]

# Adjacency dicts with Edge Weights
N3 = [
        {b:2, c:1, d:3, e:9, f:4},  #a 
        {c:4, e:3},                 #b 
        {d:8},                      #c 
        {e:7},                      #d 
        {f:5},                      #e 
        {c:2, g:2, h:2},            #f 
        {f:1, h:6},                 #g 
        {f:9, g:8}                  #h
]

# Dict with Adjacency Sets
N4 = {
        'a': set('bcdef'), 
        'b': set('ce'), 
        'c': set('d'), 
        'd': set('e'), 
        'e': set('f'), 
        'f': set('cgh'), 
        'g': set('fh'), 
        'h': set('fg')
}

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

# Adjacency Matrices

# Adjacency Matrix, Implemented with Nested Lists
N5 = [[0,1,1,1,1,1,0,0], # a 
      [0,0,1,0,1,0,0,0], # b 
      [0,0,0,1,0,0,0,0], # c 
      [0,0,0,0,1,0,0,0], # d 
      [0,0,0,0,0,1,0,0], # e 
      [0,0,1,0,0,0,1,1], # f 
      [0,0,0,0,0,1,0,1], # g 
      [0,0,0,0,0,1,1,0]] # h

# Weight Matrix with Infinite Weight for Missing Edges

N6 = [[0,2,1,3,9,4,_,_], # a 
      [_,0,4,_,3,_,_,_], # b 
      [_,_,0,8,_,_,_,_], # c 
      [_,_,_,0,7,_,_,_], # d 
      [_,_,_,_,0,5,_,_], # e 
      [_,_,2,_,_,0,2,2], # f 
      [_,_,_,_,_,1,0,6], # g 
      [_,_,_,_,_,9,8,0]] # h

# Matrix using Numpy

"""array([[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
          [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
          [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
          [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
          [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
          [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
          [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
          [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
          [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
          [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])
""" 
N = np.zeros([10,10])


graph = {'A': set('BC'),
         'B': set('ADE'),
         'C': set('AF'),
         'D': set('B'),
         'E': set('BF'),
         'F': set('CE')}

pp(graph)
print()

# Depth-First Search (DFS)
title = "Depth-First Search (DFS)"
print (title)
print ('*' * len(title))

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

print ("dfs(graph, 'A') = " + str(dfs(graph, 'A'))) # {'C', 'D', 'F', 'A', 'B', 'E'}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

print ("dfs(graph, 'C') = " + str(dfs(graph, 'C'))) # {'C', 'D', 'F', 'A', 'B', 'E'}

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

print ("list(dfs_paths(graph, 'A', 'F')) = " + str(list(dfs_paths(graph, 'A', 'F')))) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])

print ("list(dfs_paths(graph, 'C', 'F')) = " + str(list(dfs_paths(graph, 'C', 'F')))) # [['C', 'F'], ['C', 'A', 'B', 'E', 'F']]

print()

# Breadth-First Search (BFS)
title = "Breadth-First Search (BFS)"
print (title)
print ('*' * len(title))

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

print ("bfs(graph, 'A') = " + str(bfs(graph, 'A'))) # {'B', 'C', 'A', 'F', 'D', 'E'}

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

print ("list(bfs_paths(graph, 'A', 'F')) = " + str(list(bfs_paths(graph, 'A', 'F')))) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

print ("shortest_path(graph, 'A', 'F') = " + str(shortest_path(graph, 'A', 'F'))) # ['A', 'C', 'F']


