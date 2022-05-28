class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = [0] *26
        
        for char in s:
            counter[ord(char) - ord('a')] += 1
        
        for char in t:
            counter[ord(char) -ord('a')] -= 1
        print(counter)
        for i in counter:
            if i > 0:
                return False
        return True
        
        