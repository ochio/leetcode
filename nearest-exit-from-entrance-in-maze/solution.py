from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        q = deque([entrance])
        maze[entrance[0]][entrance[1]] = "+"
        diff = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        step = 0
        while q:
            for i in range(len(q)):
                p = q.popleft()
                for d in diff:
                    dy = d[0] + p[0]
                    dx = d[1] + p[1]
                    if dy < 0 or m <= dy or dx < 0 or n <= dx or maze[dy][dx] == "+":
                        continue
                    if dy == 0 or dy == m - 1 or dx == 0 or dx == n - 1:
                        return step + 1
                    maze[dy][dx] = "+"
                    q.append([dy, dx])
            step += 1

        return -1
