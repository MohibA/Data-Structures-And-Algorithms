# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = self.inOrder(root)
        return result[k-1]
    def inOrder(self,root):
        if not root:
            return []
        
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)
                
        