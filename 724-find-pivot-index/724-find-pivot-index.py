class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        leftSum = 0
        
        for index,num in enumerate(nums):
            if leftSum == (s-leftSum-num):
                return index
            leftSum += num
        return -1
        