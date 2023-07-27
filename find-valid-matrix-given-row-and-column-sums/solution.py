class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        grid = [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))]

        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                m = min(rowSum[i], colSum[j])
                grid[i][j] = m
                rowSum[i] -= m
                colSum[j] -= m

        return grid
