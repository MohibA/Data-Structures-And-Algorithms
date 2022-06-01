class Solution:
    def minimumDeletions(self, s: str) -> int:
        result = 0
        b_count = 0
        
        for c in s:
            if c == "a":
                result = min(b_count, result + 1)
            else:
                b_count += 1
        
        return result
        