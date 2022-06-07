class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = []
        end_times = []
        
        result, count = 0,0
        left,right = 0,0
        
        for start, end in intervals:
            start_times.append(start)
            end_times.append(end)
        
        start_times.sort()
        end_times.sort()

        while left < len(intervals):
            if start_times[left] < end_times[right]:
                left += 1
                count += 1
    
            else:
                right += 1
                count -= 1
            result = max(result,count)
        return result
                
                
                
            
        
        
        
        
        