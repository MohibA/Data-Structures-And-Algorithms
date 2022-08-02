class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total = 0
        
        for i in range(len(nums)):
            smallest = nums[i]
            largest = nums[i]
            
            for j in range(i+1, len(nums)):
                smallest = min(smallest, nums[j])
                largest = max(largest, nums[j])
                
                total += largest - smallest
        return total