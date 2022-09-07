class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-value for value in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            stoneX = heapq.heappop(maxHeap)
            stoneY = heapq.heappop(maxHeap)
            
            if stoneX != stoneY:
                newStone = stoneX-stoneY
                heapq.heappush(maxHeap,newStone)
                
        maxHeap.append(0)
        return abs(maxHeap[0])
            
        