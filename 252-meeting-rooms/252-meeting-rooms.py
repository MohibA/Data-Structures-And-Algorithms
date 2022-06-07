class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda i: i[0])
        
        if len(intervals) == 0:
            return True
        
        result = [intervals[0]]
        
        for start,end in intervals[1:]:
            lastEnd = result[-1][1]
            
            if start < lastEnd:
                return False
            else:
                result.append([start,end])
        return True
            
        