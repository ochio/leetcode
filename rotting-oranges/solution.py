from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        m = len(grid)
        n = len(grid[0])

        count = 0
        diff = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i, j])
                if grid[i][j] == 1:
                    fresh += 1

        while q and fresh:
            count += 1
            for _ in range(len(q)):
                y, x = q.popleft()

                for d in diff:
                    dy = d[0] + y
                    dx = d[1] + x
                    if dy < 0 or m <= dy or dx < 0 or n <= dx or grid[dy][dx] == 0 or grid[dy][dx] == 2:
                        continue
                    if grid[dy][dx] == 1:
                        grid[dy][dx] = 2
                        fresh -= 1
                        q.append([dy, dx])
        if fresh != 0:
            return -1
        return count
