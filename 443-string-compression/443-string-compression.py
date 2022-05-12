class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        index = 0
        
        while left < len(chars):
            right = left
            while right < len(chars) and chars[right] == chars[left]:
                right += 1
            size = right - left
            chars[index] = chars[left]
            index += 1
            
            if size > 1:
                for digit in str(size):
                    chars[index] = digit
                    index += 1
            left = right
        chars = chars[:index]
        return index
                   
            
        