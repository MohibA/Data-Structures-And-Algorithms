class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        start = 0
        end = 0
        max_len = 0
        tracker = {}
        while end < len(s):
            tracker[s[end]] = end
            if len(tracker) > k:
                min_ind = min(tracker.values())
                start = min_ind + 1
                del tracker[s[min_ind]]
            max_len = max(max_len, end - start + 1)
            end += 1
        return max_len
            
        