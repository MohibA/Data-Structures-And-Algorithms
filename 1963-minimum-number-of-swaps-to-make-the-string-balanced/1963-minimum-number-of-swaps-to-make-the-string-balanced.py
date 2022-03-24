class Solution:
    def minSwaps(self, s: str) -> int:
        extraClosedBrackets = 0
        minSwap = 0
        
        for c in s:
            if c == '[':
                extraClosedBrackets -= 1
            else:
                extraClosedBrackets += 1
            minSwap = max(minSwap,extraClosedBrackets)
        return (1+minSwap) //2

            
                
            
            
        