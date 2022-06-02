class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result, maxHeap = "", []
        
        for count,char in [(-a,"a"),(-b,"b"),(-c,"c")]:
            if count != 0:
                heapq.heappush(maxHeap,(count,char))
        
        while maxHeap:
            count,char = heapq.heappop(maxHeap)
            #check if most frequent char has been added twice before already
            if len(result) >1 and result[-1] == result[-2] == char:
                #check if second most character exists
                if not maxHeap:
                    break
                #get second most character and add to result
                count2,char2 = heapq.heappop(maxHeap)
                result += char2
                count2 += 1
                
                #if there is still occurence of the char, push back into heap
                if count2:
                    heapq.heappush(maxHeap,(count2,char2))
            #in the case we can add most frequent character
            else:
                result += char
                count += 1
            if count:
                heapq.heappush(maxHeap,(count,char))
        return result
                
                
                