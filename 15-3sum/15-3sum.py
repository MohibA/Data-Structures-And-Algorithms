class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #O(logn) + O(n^2) = O(n^2)
        #Space could be O(1) or O(n)
        nums.sort()
        result = []
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) -1 
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                if currSum > 0:
                    right -= 1
                elif currSum < 0:
                    left += 1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left +=1
        return result
                    
            
            