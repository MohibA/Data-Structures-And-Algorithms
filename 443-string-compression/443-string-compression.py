class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        index = 0
        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1

            size = j - i
            chars[index] = chars[i]
            index += 1
            if size > 1:
                for digit in str(size):
                    chars[index] = digit
                    index += 1
            i = j
        chars = chars[:index]
        return index
                
            
            
        