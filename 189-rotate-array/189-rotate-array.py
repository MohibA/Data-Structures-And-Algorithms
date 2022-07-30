class Solution:
    def reverse_arr(self,l,r,nums):
        while l < r:
            nums[l],nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums
            
            
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        
        l,r = 0, len(nums)-1
        self.reverse_arr(l,r,nums)
        
        l,r = 0, k -1
        self.reverse_arr(l,r,nums)
        
        l,r = k, len(nums)-1
        self.reverse_arr(l,r,nums)
        
            
            
        