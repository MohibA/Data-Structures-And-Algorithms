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
        up_to = (n//2) - 1
        
        print("values", values)
        i = 0
        while curr:
            if i > up_to:
                break
            twin_node = n - 1 - i
            max_sum = max(max_sum,curr.val + values[twin_node])
            i += 1
            curr = curr.next
        return max_sum
            
            
            
        