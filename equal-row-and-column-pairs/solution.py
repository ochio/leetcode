class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = {}

        for i in range(len(grid)):
            k = str(grid[i])
            if k in d:
                d[k] += 1
            else:
                d[k] = 1

        c = 0
        for i in range(len(grid)):
            k = []
            for j in range(len(grid)):
                k.append(grid[j][i])
            k = str(k)
            if k in d:
                c += d[k]
        return c
