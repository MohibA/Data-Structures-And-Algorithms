# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        q = collections.deque()
        q.append(root)
        
        if not root:
            return result
        
        while q:
            qLen = len(q)
            level = []
            
            for i in range(qLen):
                root = q.popleft()
                level.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            result.append(level)
        return result
                