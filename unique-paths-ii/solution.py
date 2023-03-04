class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        grid = [[-1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0

        if grid[0][0] == 0:
            return 0
        else:
            grid[0][0] = 1

        for i in range(1, m):
            if grid[i][0] == 0:
                while i < m:
                    grid[i][0] = 0
                    i += 1
                break
            else:
                grid[i][0] = 1

        for j in range(1, n):
            if grid[0][j] == 0:
                while j < n:
                    grid[0][j] = 0
                    j += 1
                break
            else:
                grid[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == -1:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
                elif grid[i][j] == 0:
                    continue
        return grid[m - 1][n - 1]
