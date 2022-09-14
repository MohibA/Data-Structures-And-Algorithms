# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = float("-inf")
        n = 0
        curr = head
        values = []
        
        while curr:
            values.append(curr.val)
            n+= 1
            curr = curr.next
        curr = head
        
        N = len(values)
        for i in range(N):
            max_sum = max(max_sum,values[i] + values[n-i-1])
        
        return max_sum

#Try a soluton later with slow and fast pointer to reduce space complexity
            
            
        