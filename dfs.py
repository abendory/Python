#!/usr/local/bin/python3.4

from pprint import pprint as pp

graph = {'A': set('BC'),
         'B': set('ADE'),
         'C': set('AF'),
         'D': set('B'),
         'E': set('BF'),
         'F': set('CE')}

def dfs(graph, start='A'):
    visited, stack = set(), [start]  # start = ['A']
    while stack:
        # print ("stack = " + str(stack))
        # print ("visited = " + str(visited))
        vertex = stack.pop()   # vertex = 'A'  remove last item in list
        if vertex not in visited:
            visited.add(vertex)  # visited = ['A']
            stack.extend(graph[vertex] - visited)   # append ['B', 'C'] - ['A'] to stack 
    return visited

def dfs_r(graph, start='A', visited=None):
    # print ("visited = " + str(visited))
    # print ("start = " + str(start))
    if visited is None:
        visited = set()
    visited.add(start)
    # print ("graph[start] - visited = " + str(graph[start] - visited))
    for n in graph[start] - visited:  # call dfs_r on each child node
        dfs_r(graph, n, visited)
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        # print ("stack = " + str(stack))
        (vertex, path) = stack.pop(); 
        # print ("vertex, path = {}, {}".format(vertex, path))
        # print ("graph[vertex] = {}".format(graph[vertex]))
        # print ("set(path) = {}".format(set(path)))
        for n in graph[vertex] - set(path):
            if n == goal:
                yield path + [n]
            else:
                stack.append((n, path + [n]))

pp(graph)

print ()
print ("dfs(graph) = " + str(dfs(graph)))

print ()
print ("dfs_r(graph) = " + str(dfs_r(graph)))

print ()
print ("list(dfs_paths(graph, 'A', 'F')) = " + str(list(dfs_paths(graph, 'A', 'F')))) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]




