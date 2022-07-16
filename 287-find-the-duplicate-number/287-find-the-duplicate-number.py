class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numbers = set()
        
        for i in range(len(nums)):
            if nums[i] in numbers:
                return nums[i]
            numbers.add(nums[i])
        
        
        
        
        
        
        