class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        a = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    a[i][j] = True

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if a[i][j]:
                    for k in range(len(matrix)):
                        matrix[k][j] = 0
                    for k in range(len(matrix[0])):
                        matrix[i][k] = 0
