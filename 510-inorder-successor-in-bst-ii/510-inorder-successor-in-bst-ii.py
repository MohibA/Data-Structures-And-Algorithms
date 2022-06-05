"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        curr_node = node
        root_node = None
        successor = None
        
        while curr_node:
            if curr_node.parent is not None:
                root_node = curr_node.parent
                curr_node = curr_node.parent
            else:
                root_node = curr_node
                break      
        while root_node:
            if node.val >= root_node.val:
                root_node = root_node.right
            else:
                successor = root_node
                root_node = root_node.left
        return successor
        
            
            
        
        