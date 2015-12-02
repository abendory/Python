#!/usr/local/bin/python3.4

from pprint import pprint as pp

graph = {'A': set('BC'),
         'B': set('ADE'),
         'C': set('AF'),
         'D': set('B'),
         'E': set('BF'),
         'F': set('CE')}

def bfs(graph, start='A'):
	visited, queue = set(), [start]  # start = ['A']
	while queue:
		# print ("queue = " + str(queue))
		# print ("visited = " + str(visited))
		vertex = queue.pop(0)   # vertex = 'A' remove first item in list
		if vertex not in visited:
			visited.add(vertex)  # visited = ['A']
			queue.extend(graph[vertex] - visited)   # append ['B', 'C'] - ['A'] to queue 
	return visited


pp(graph)
print()
print ("bfs(graph) = " + str(bfs(graph)))