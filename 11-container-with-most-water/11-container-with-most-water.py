class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxSum =  0
        left_pointer = 0
        right_pointer = len(height) -1
        currMax = 0
        
        #lowerBound(lower value) times blocks = max
        #check if left is smaller than right --> lower += 1
        while left_pointer <= right_pointer:
            blocks = right_pointer - left_pointer
            if height[left_pointer] < height[right_pointer]:
                currMax = height[left_pointer] * blocks
                left_pointer += 1
            else:
                currMax = height[right_pointer] * blocks
                right_pointer -= 1
            maxSum = max(currMax,maxSum)
        return maxSum
            
            
            
                
                
            
            
            
            
            
            
            
            
            
# max = 7
#check lower value then multiply that with blocks
#height[left_pointer] * height[rightPointer]
#blocks = (right - left) = 7 
            
#[1,8,6,2,5,4,8,3,7]
#   L           R
#
            
        
        