class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = 0
        hashmap = {}
        
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        for num in hashmap.keys():
            if k > 0 and num + k in hashmap:
                result += 1
            if k == 0 and hashmap[num] > 1:
                result += 1
        return result