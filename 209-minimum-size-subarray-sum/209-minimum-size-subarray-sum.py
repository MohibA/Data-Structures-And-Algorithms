class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, total = 0,0
        result = float("inf")
        
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                result = min(result,r-left + 1)
                total -= nums[left]
                left += 1
        return 0 if result == float("inf") else result
        
        
             
            
                
        
            
            
        