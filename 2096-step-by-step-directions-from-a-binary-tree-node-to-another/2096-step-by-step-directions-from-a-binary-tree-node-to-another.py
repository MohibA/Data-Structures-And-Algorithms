# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        #First convert tree into graph
        graph = collections.defaultdict(list)
        
        queue = collections.deque([root])
        
        while queue:
            curr_node = queue.popleft()
            
            if curr_node.left:
                graph[curr_node.left.val].append((curr_node.val,'U'))
                graph[curr_node.val].append((curr_node.left.val,'L'))
                
                queue.append(curr_node.left)
                
            if curr_node.right:
                graph[curr_node.right.val].append((curr_node.val,'U'))
                graph[curr_node.val].append((curr_node.right.val,'R'))
                
                queue.append(curr_node.right)
        
        q = collections.deque([(startValue,"")])
        seen = set()
        
        while q:
            curr_node,path = q.popleft()
            
            if curr_node in seen:
                continue
            seen.add(curr_node)
            
            if curr_node == destValue:
                return path
            else:
                for child,direction in graph[curr_node]:
                    if child not in seen:
                        q.append(([child,path+direction]))