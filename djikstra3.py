from collections import namedtuple, deque
from pprint import pprint as pp
 
 
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

""" 
Let the node at which we are starting be called the initial node. 
Let the distance of node Y be the distance from the initial node to Y. 
Dijkstra's algorithm will assign some initial distance values and will try 
to improve them step by step.

1. Assign to every node a tentative distance value: set it to zero for our initial 
   node and to infinity for all other nodes.
2. Set the initial node as current. Mark all other nodes unvisited. Create a set of 
   all the unvisited nodes called the unvisited set.
3. For the current node, consider all of its unvisited neighbors and calculate their 
   tentative distances. Compare the newly calculated tentative distance to the 
   current assigned value and assign the smaller one. For example, if the current 
   node A is marked with a distance of 6, and the edge connecting it with a 
   neighbor B has length 2, then the distance to B (through A) will be 6 + 2 = 8. 
   If B was previously marked with a distance greater than 8 then change it to 8. 
   Otherwise, keep the current value.
4. When we are done considering all of the neighbors of the current node, mark the 
   current node as visited and remove it from the unvisited set. A visited node will 
   never be checked again.
5. If the destination node has been marked visited (when planning a route between 
   two specific nodes) or if the smallest tentative distance among the nodes in 
   the unvisited set is infinity (when planning a complete traversal; occurs when 
   there is no connection between the initial node and remaining unvisited nodes), 
   then stop. The algorithm has finished.
6. Otherwise, select the unvisited node that is marked with the smallest tentative 
   distance, set it as the new "current node", and go back to step 3.
"""

class Graph():
    def __init__(self, edges):
        self.edges = edges2 = [Edge(*edge) for edge in edges]
        self.vertices = set(sum(([e.start, e.end] for e in edges2), []))
 
    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))
        pp(neighbours)
        print()
 
        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:      # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
        pp(previous)
        print()
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s
 
 
graph = Graph([("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
               ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
               ("e", "f", 9)])
pp(graph.dijkstra("a", "e"))

#  Neighbors
#  {'a': {('b', 7), ('c', 9), ('f', 14)},
#   'b': {('d', 15), ('c', 10)},
#   'c': {('d', 11), ('f', 2)},
#   'd': {('e', 6)},
#   'e': {('f', 9)},
#   'f': set()}

#  Previous
#  {'a': None, 'b': 'a', 'c': 'a', 'd': 'c', 'e': 'd', 'f': 'c'}

#  Djikstra
#  deque(['a', 'c', 'd', 'e'])