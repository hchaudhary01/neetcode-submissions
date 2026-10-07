class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    max_area = max(max_area,self.dfs(grid, i,j))
        return max_area
    def dfs(self, grid, i, j):
        row = len(grid)
        col = len(grid[0])

        if i<0 or i>=row or j<0 or j>=col or grid[i][j]!=1:
            return 0
        grid[i][j] = 0
        return 1+ self.dfs(grid, i+1,j) +self.dfs(grid, i-1,j)+self.dfs(grid, i, j+1)+self.dfs(grid, i, j-1)
        