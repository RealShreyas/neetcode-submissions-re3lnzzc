class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 1:
                return 0
            
            if (i, j) == (m-1, n-1):
                return 1
            
            grid[i][j] = 1
            ans = 0

            ans += dfs(i+1, j)
            ans += dfs(i, j+1)
            ans += dfs(i-1, j)
            ans += dfs(i, j-1)

            grid[i][j] = 0
            return ans
        
        return dfs(0,0)