class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        setOne = set()
        intersection = set()
        for num in nums1:
            setOne.add(num)
        
        for num in nums2:
            if num in setOne:
                intersection.add(num)
        return intersection
            
        
        