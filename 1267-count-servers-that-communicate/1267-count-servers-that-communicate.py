class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        result = 0
        
        #create two arrays of size of rows and col to store number of servers in each
        rows = [0] * len(grid)
        col = [0] * len(grid[0])
        
        #Loop thrugh Grid and update number of servers in the row and col
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows[i] += 1
                    col[j] += 1        
        print(rows)
        print(col)
        #Loop through in size of grid in rows and col again
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #check if the current position is a server and make sure that either the row or col has more than one server which means they can communicate, so result += 1
                if grid[i][j] == 1 and (rows[i] > 1 or col[j] > 1):
                    result += 1
        return result