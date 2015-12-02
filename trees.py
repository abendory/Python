from pprint import pprint as pp

# Binary Tree Class 
class Tree:
    def __init__(self, data, left, right): 
        self.data = data
        self.left = left
        self.right = right

# Multiway Tree Class
class Tree2:
    def __init__(self, kids, next=None):
        self.kids = self.val = kids 
        self.next = next


# Sample Tree

"""           0

       1            2

   3       4             6

         9   10       11     
"""

t = Tree(2, Tree(7, Tree(2,None,None), Tree(6, Tree(5,None, None), Tree(11,None,None))), Tree(5,None,Tree(9, Tree(4,None,None), None)))


# Recursively traverse a binary tree
# ==================================
# Preorder traversal keeps traversing the left most part of the 
# tree until a leaf node (which has no child nodes) is encountered, 
# then it goes up the tree, goes to the right child node (if any), 
# and then goes up the tree again, and then as far left as possible, 
# and this keeps repeating until all of the nodes are traversed.
def preorder(node):
    if node is None:
        return
  
    print(node.data, end=" ")

    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)

def postorder(node):
    if node is None:
        return
  
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=" ")

title = "Preorder, Inorder, and Postorder Traversal of Binary Tree"
print(title)
print("="*len(title))

preorder(t); print()
inorder(t); print()
postorder(t); print()
