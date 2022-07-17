# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        route = []

        def dfs(node, currSum, route):
            if not node:
                return []

            route.append(node.val)
            currSum += node.val
            #print(route)
            
            if not node.left and not node.right and currSum == targetSum:
                result.append(route[:])
                # print("result = ", result)

            dfs(node.left, currSum, route)
            dfs(node.right, currSum, route)
            
            route.pop()
            return result

        return dfs(root, 0, route)