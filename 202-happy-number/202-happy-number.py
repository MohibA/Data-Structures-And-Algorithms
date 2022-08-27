class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total = 0
            while number > 0:
                number, digit = divmod(number,10)
                total += digit **2
            return total
        
        slow_pointer = n
        fast_pointer = get_next(n)
        
        while fast_pointer != 1 and slow_pointer != fast_pointer:
            slow_pointer = get_next(slow_pointer)
            fast_pointer = get_next(get_next(fast_pointer))
        return fast_pointer == 1
        