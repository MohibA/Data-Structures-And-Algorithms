class Solution:
    def reverseWords(self, s: str) -> str:
        left,right = 0, len(s)-1
        
        while left <= right and s[left] == ' ':
            left += 1
        
        while left <= right and s[right] == ' ':
            right -= 1
        
        
        q, word = deque(), []
        
        while left <= right:
            if s[left] == ' ' and word:
                q.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        q.appendleft(''.join(word))
        
        return ' '.join(q)
                
    
        
        
        
            
        
        