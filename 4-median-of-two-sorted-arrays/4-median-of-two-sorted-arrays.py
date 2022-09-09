class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        heapq.heapify(nums1)
        heapq.heapify(nums2)
        
        minHeap = []
        
        while nums1 or nums2:
            if (nums1 and nums2) and nums1[0] < nums2[0]:
                val = heapq.heappop(nums1)
                minHeap.append(val)
                if nums2[0] < nums1[0]:
                    val = heapq.heappop(nums2)
                    minHeap.append(val)
                    
            if nums1:
                val = heapq.heappop(nums1)
                minHeap.append(val)
            if nums2:
                val = heapq.heappop(nums2)
                minHeap.append(val)
        '''
        
        sortedArr = sorted(nums1+nums2)
        if len(sortedArr) ==1:
            return sortedArr[0]
        
        
        return self.findMedian(sortedArr)
    
    
    def findMedian(self,arr):
        left = 0
        right = len(arr)-1
        
        if len(arr) % 2 == 0:
            while not left+1 == right:
                left += 1
                right-= 1
            return (arr[left] + arr[right])/2
        while not left+2 == right:
            left += 1
            right-=1
        return arr[left+1]
        
    '''      
    def findMedian(self,arr):
        minHeap = []
        maxHeap = []
        
        for num in arr:
            heapq.heappush(maxHeap,-1*num)
            
            #check to see that nums in maxHeap are smaller than minHeap
            if (minHeap and maxHeap) and -1*maxHeap[0] < minHeap[0]:
                val = -1 * heapq.heappop(maxHeap)
                heapq.heappush(minHeap,val)
            #check lens
            if len(maxHeap) > 1+ len(minHeap):
                val = -1 * heapq.heappop(maxHeap)
                heapq.heappush(minHeap,val)
            
            if len(minHeap) > 1 + len(maxHeap):
                val = heapq.heappop(self.minHeap)
                heapq.heappush(maxHeap, -1*val)
        
        if len(minHeap) > len(maxHeap):
            return minHeap[0]

        if len(maxHeap) > len(minHeap):
            return -1* maxHeap[0]
        
        return (-1* maxHeap[0] + minHeap[0])/2
    '''        
        