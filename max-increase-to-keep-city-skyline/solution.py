class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        total = 0
        r = []
        c = []

        for i in range(len(grid)):
            r.append(max(grid[i]))

        for i in range(len(grid[0])):
            m = 0
            for j in range(len(grid)):
                m = max(m, grid[j][i])
            c.append(m)

        for i in range(len(r)):
            for j in range(len(c)):
                total += min(r[i], c[j]) - grid[i][j]

        return total
