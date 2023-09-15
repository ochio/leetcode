class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1

        for i in range(n):
            c = 0
            for j in range(m):
                if grid[j][i] == 0:
                    c += 1
            if c > m // 2:
                for j in range(m):
                    grid[j][i] ^= 1

        s = 0
        for b in grid:
            s += int("".join(map(str, b)), 2)

        return s
