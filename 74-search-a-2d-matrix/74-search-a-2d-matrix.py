class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        if rows == 0:
            return False
        
        left,right = 0, rows*cols -1
        
        while left <= right:
            middle = (left + right) //2
            
            middle_element = matrix[middle//cols][middle % cols]

            if target == middle_element:
                return True
            else:
                if target < middle_element:
                    right = middle -1
                else:
                    left = middle + 1
        return False
                
        
        