class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        result = nums[0]
        leftPointer = 0
        rightPointer = len(nums) - 1
        
        while leftPointer <= rightPointer:
            if nums[leftPointer] < nums[rightPointer]:
                result = min(result,nums[leftPointer])
                break
            middle = (leftPointer + rightPointer) //2
            result = min(result,nums[middle])
            if nums[middle] >= nums[leftPointer]:
                leftPointer = middle + 1
            else:
                rightPointer = middle -1
        return result
                
        
        
        