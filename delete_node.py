class Node(object):
	def __init__(self,data=None,next_node=None):
		self.data=data
		self.next_node=next_node

def delete_node(n):
   Node temp = n.next_node 
   n.data = temp.data
   n.next_node = temp.next_node
   del temp

a = Node(1)
b = Node(2)
c = Node(3)
a.next_node = b
b.next_node = c
delete_node(b)
print a.nextnode, b.next_node, c.next_node
