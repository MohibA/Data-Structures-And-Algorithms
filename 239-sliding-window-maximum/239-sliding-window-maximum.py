class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = collections.deque()
        l=r= 0
        
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            
            if (r+1) >=k:
                result.append(nums[q[0]])
                l +=1 
            r+= 1
        return result
            
        
        
        
        
        
        
        
        
        
        
'''

        left = 0
        right = (left + k) -1
        result = []
        
        if k > len(nums):
            return None
        
        while right < len(nums):
            curr_max = nums[left]
            
            for i in range(left,right+1):
                curr_max = max(nums[i],curr_max)
            result.append(curr_max)
            right += 1
            left += 1
        return result




'''