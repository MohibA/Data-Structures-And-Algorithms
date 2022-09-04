class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        result = pos = neg = 0
        
        for i in nums:
            if i > 0:
                pos+= 1
                neg += 1 if neg else 0
            elif i < 0:
                pos,neg = 1+neg if neg else 0, 1+ pos
            else:
                pos = neg = 0
            result = max(result,pos)
        return result
                
            
            
        