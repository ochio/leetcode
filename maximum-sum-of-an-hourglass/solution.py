class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        v = 0
        for i in range(m):
            for j in range(n):
                if i + 2 >= m or j + 2 >= n:
                    break
                s = (
                    grid[i][j]
                    + grid[i][j + 1]
                    + grid[i][j + 2]
                    + grid[i + 1][j + 1]
                    + grid[i + 2][j]
                    + grid[i + 2][j + 1]
                    + grid[i + 2][j + 2]
                )
                v = max(v, s)
        return v
