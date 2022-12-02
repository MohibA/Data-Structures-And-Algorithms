class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        lenOfString = len(s)
        vowels = ('a','e','i','o','u','A','E','I','O','U')
        
        vowelCount = 0
        
        a = s[0:lenOfString//2]
        b = s[lenOfString//2:]
        
        for char in a:
            if char in vowels:
                vowelCount +=1
        for char in b:
            if char in vowels:
                vowelCount -=1
        return vowelCount == 0
        
        

        
        
        
        
        
        
        

        
        
#len of string is even
#a can equal len//2 so you can add to a 0-1
#b can start from a and go to the end of string
# can store vowels in a set
# then loop through a and then b and subtratc from count
        