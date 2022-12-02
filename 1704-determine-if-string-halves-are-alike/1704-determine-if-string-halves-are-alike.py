class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        leftPointer = 0
        rightPointer = len(s)-1
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        
        vowelCount = 0
        
        for i in range(len(s)//2):
            if s[leftPointer] in vowels:
                vowelCount += 1
            if s[rightPointer] in vowels:
                vowelCount -=1
            leftPointer +=1
            rightPointer -=1
        
        return vowelCount == 0
        
        
        
        

        
        
        
        
        
        
        

        
        
#len of string is even
#a can equal len//2 so you can add to a 0-1
#b can start from a and go to the end of string
# can store vowels in a set
# then loop through a and then b and subtratc from count
        