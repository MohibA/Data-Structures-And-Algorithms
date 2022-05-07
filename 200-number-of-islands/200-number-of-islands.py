class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Nested loop to go over our Grid
        #use depth first traversal in second loop to explore neighbors
        
        visited = set()
        count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (self.explore(grid,row,col,visited)):
                    count +=1 
        return count
                
    def explore(self,grid,row,col,visited):
        #catch if we are out of bounds
        rowInbound = 0 <= row and row < len(grid)
        colInbound = 0 <= col and col < len(grid[0])
        
        if not rowInbound or not colInbound:
            return False
        
        #check if current is water
        position = grid[row][col]
        if (position == '0'):
            return False
        
        #check for visited 
        if (row,col) in visited:
            return False
        
        visited.add((row,col))
        
        self.explore(grid,row-1,col,visited)
        self.explore(grid,row+1,col,visited)
        self.explore(grid,row,col-1,visited)
        self.explore(grid,row,col+1,visited)
        
        #this true will sybolize that I am now exploring a new island
        
        return True
        
        
        