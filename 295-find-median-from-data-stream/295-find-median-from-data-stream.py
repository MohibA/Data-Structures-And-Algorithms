class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    #Store smaller part of the list in a maxHeap and larger part in a minHeap
    def addNum(self, num: int) -> None:
        #by Default add to maxHeap
        heapq.heappush(self.maxHeap, -1*num)
        
        #make sure all elements in maxHeap <= all in minHeap
        if (self.maxHeap and self.minHeap) and(-1*self.maxHeap[0]) > self.minHeap[0]:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,val)
        
        #Check for uneven size, difference greater than 1?
        if len(self.maxHeap) > 1 + len(self.minHeap):
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,val)
            
        if len(self.minHeap) > 1 + len(self.maxHeap):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap,-1*val)
            

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -1* self.maxHeap[0]
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        
        #even number of elements
        return (-1*self.maxHeap[0] + self.minHeap[0]) /2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()