from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q = deque()
        MAX_VALUE = m * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append([i, j])
                else:
                    mat[i][j] = MAX_VALUE
        d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while q:
            r, c = q.popleft()
            for dr, dc in d:
                x = r + dr
                y = c + dc
                if 0 <= x < m and 0 <= y < n and mat[x][y] > mat[r][c] + 1:
                    q.append([x, y])
                    mat[x][y] = mat[r][c] + 1

        return mat
