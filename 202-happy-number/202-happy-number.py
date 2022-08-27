class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(num):
            total = 0
            
            while num:
                num,digit = divmod(num,10)
                total += digit **2
            return total
        
        slow = n
        fast = getNext(n)
        
        while fast != 1 and slow != fast:
            slow = getNext(slow)
            fast = getNext(getNext(fast))
        return fast == 1
        