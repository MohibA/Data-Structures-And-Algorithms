# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#left,right,root

'''
            1
          /   \
        2       3
       / \
      4   5  
      
     
stack [1,2,3]
result =[3,]
'''


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        
        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            temp = stack[-1].right
            if temp:
                root = temp
            else:
                temp = stack.pop()
                result.append(temp.val)
                while stack and temp == stack[-1].right:
                    temp = stack.pop()
                    result.append(temp.val)
        return result
                
    
            
            
                

        
        
        
        
        