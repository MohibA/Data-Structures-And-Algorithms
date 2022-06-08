class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        #rec(x1) < rec(y1) and rec1(y1) < rec2(y2) and rec2(x1) < rec1(x2) and rec2(y1) < rec1(y2)
        return (rec1[0] < rec2[2] and rec1[1] < rec2[3] and rec2[0] <rec1[2] and rec2[1] < rec1[3])
        
        