class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        pointer = 0
        
        while pointer < len(nums):
            num = nums[pointer]
            
            if num < len(nums) and num != pointer:
                nums[pointer],nums[num] = nums[num],nums[pointer]
            else:
                pointer += 1
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        
        return len(nums)
                