class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[1] * 5 for _ in range(n)]

        for i in range(1, n):
            for j in range(5):
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return sum(dp[-1])
