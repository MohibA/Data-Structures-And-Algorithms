class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elements = set()
        
        for i in nums:
            if i in elements:
                return True
            else:
                elements.add(i)
        return False
            
            
                
        
        