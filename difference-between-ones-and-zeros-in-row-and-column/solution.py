class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        onesRow = []
        zerosRow = []
        onesCol = []
        zerosCol = []

        for i in range(m):
            o = grid[i].count(1)
            z = n - o
            onesRow.append(o)
            zerosRow.append(z)

        for i in range(n):
            o = 0
            z = 0
            for j in range(m):
                if grid[j][i] == 1:
                    o += 1
                else:
                    z += 1
            onesCol.append(o)
            zerosCol.append(z)

        for i in range(m):
            for j in range(n):
                grid[i][j] = onesRow[i] + onesCol[j] - \
                    zerosRow[i] - zerosCol[j]

        return grid
