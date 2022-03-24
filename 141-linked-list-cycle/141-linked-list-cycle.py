# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPointer = fastPointer = head
        
        
        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            
            if slowPointer == fastPointer:
                return True
        return False