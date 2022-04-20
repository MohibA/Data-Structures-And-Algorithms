class Solution(object):
    def expandAroundcenters(self, s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -=1 
                right += 1
            return s[left+1:right]
    def longestPalindrome(self, s):
        longestSub = ''
        for i in range(len(s)):
            center = self.expandAroundcenters(s,i,i) 
            inBetween = self.expandAroundcenters(s,i,i+1)

            longestSub = max(longestSub,center,inBetween, key = len)
        return longestSub
        

        
        