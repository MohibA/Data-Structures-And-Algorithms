# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        n = 0
        
        #edge case of no root
        if root is None:
            return []
        
        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            n+= 1
            if n ==k:
                return root.val
            root = root.right
        return None
        