# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #check if subroot is null if it is return True because it can be a sub tree of a node with no children
        if not subRoot:
            return True
        if root is None:
            return False
        
        if self.sameTree(root,subRoot):
            return True
        
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot))
    
    
    def sameTree(self,p,q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return (self.sameTree(p.left,q.left) and 
                    self.sameTree(p.right,q.right))
        return False
        
        
    
    
    
        