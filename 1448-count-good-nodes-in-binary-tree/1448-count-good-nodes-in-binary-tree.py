# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        
        def dfs(node,maxValue):
            if not node:
                return 0
            
            result = 1 if node.val >= maxValue else 0
            maxValue = max(maxValue,node.val)
            
            result += dfs(node.left,maxValue)
            result += dfs(node.right,maxValue)
            
            return result
        
        return dfs(root,root.val)