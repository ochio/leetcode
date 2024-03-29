class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []
        for i in range(1, len(triangle) + 1):
            a = [0 for _ in range(i)]
            dp.append(a)
        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j]
                elif j == len(triangle[i - 1]):
                    dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j])
        m = 10 ** 7
        for v in dp[-1]:
            m = min(m, v)

        return m
