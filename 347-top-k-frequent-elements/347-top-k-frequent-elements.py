class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = {}
        
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        for key,val in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, [val,key])
            else:
                heapq.heappushpop(heap, [val, key])
        return [key for val,key in heap]
        