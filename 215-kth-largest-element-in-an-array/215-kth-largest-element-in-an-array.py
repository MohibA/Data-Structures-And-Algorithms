class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        for n in range(len(nums)):
            if len(nums) > k:
                heapq.heappop(nums)
        return heapq.heappop(nums)
            
                
        