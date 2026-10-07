class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count+=1
        return count
    def dfs(self, grid, i , j):
            row = len(grid)
            col = len(grid[0])
            if i <0 or i >=row or j < 0 or j>=col or grid[i][j] != "1":
                return
            grid[i][j] = "x"
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i , j-1)
        

        

        