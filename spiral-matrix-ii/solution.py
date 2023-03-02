class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        r = [[0 for _ in range(n)] for __ in range(n)]

        top, right, bottom, left = 0, n - 1, n - 1, 0
        c = 1

        while top <= bottom and left <= right:

            for i in range(left, right + 1):
                r[top][i] = c
                c += 1

            top += 1

            for i in range(top, bottom + 1):
                r[i][right] = c
                c += 1

            right -= 1

            for i in range(right, left - 1, -1):
                r[bottom][i] = c
                c += 1

            bottom -= 1

            for i in range(bottom, top - 1, -1):
                r[i][left] = c
                c += 1

            left += 1

        return r
