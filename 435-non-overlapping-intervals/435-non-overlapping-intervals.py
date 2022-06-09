class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #[1,2],[1,3],[2,3],[3,4]
        intervals.sort(key = lambda i: i[0])
        count = 0
        lastEnd = intervals[0][1]
        for start,end in intervals[1:]:
            if start >= lastEnd:
                lastEnd = end
            else:
                count += 1
                lastEnd = min(end,lastEnd)
        return count
                
                
                
        