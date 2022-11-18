class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        H = len(grid)
        W = len(grid[0])
        c = 0
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for h in range(H):
            for w in range(W):
                if grid[h][w] == 1:
                    c += 4
                    for i, j in d:
                        if h + i >= H or h + i < 0 or w + j >= W or w + j < 0:
                            continue
                        elif h + i < h and w + j < w and grid[h + i][w + j] == 1:
                            c -= 2
        return c
