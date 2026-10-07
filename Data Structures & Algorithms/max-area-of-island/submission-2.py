class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    area = [0]
                    self.dfs(grid, i, j, area)
                    count = max(count, area[0])
        return count
    def dfs(self, grid, i , j, area):
        row = len(grid)
        col = len(grid[0])
        if i <0 or i >=row or j < 0 or j>=col or grid[i][j] != 1: 
            return
        grid[i][j] = "x"
        area[0] += 1
        self.dfs(grid, i+1, j, area)
        self.dfs(grid, i-1, j, area)
        self.dfs(grid, i, j+1, area)
        self.dfs(grid, i , j-1, area)
        