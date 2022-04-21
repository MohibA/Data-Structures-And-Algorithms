class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left,right,count = {},{},{}
        
        for i,x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            if x not in count:
                count[x] = 1
            else:
                count[x] += 1
        result = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                result = min(result, right[x] - left[x] + 1)

        return result