class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        ans = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                left = max(0, j - k)
                right = min(n - 1, j + k)
                top = max(0, i - k)
                bottom = min(m - 1, i + k)

                s = 0
                for x in range(top, bottom + 1):
                    for y in range(left, right + 1):
                        s += mat[x][y]
                ans[i][j] = s
        return ans
