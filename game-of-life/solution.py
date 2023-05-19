class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        t = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                t[i][j] = board[i][j]

        diff = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(m):
            for j in range(n):
                c = 0
                for d in diff:
                    x = d[0] + j
                    y = d[1] + i
                    if x < 0 or x >= n or y < 0 or y >= m:
                        continue
                    if board[y][x] == 1:
                        c += 1

                if board[i][j] == 1 and c < 2:
                    t[i][j] = 0
                elif board[i][j] == 1 and 2 <= c <= 3:
                    t[i][j] = 1
                elif board[i][j] == 1 and 3 < c:
                    t[i][j] = 0
                elif board[i][j] == 0 and c == 3:
                    t[i][j] = 1

        for i in range(m):
            for j in range(n):
                board[i][j] = t[i][j]
