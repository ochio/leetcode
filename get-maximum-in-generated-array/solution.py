class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0

        nums = [0] * (n + 1)
        nums[1] = 1
        m = 1

        for i in range(1, n):
            if 2 * i <= n:
                nums[2 * i] = nums[i]
                m = max(m, nums[2 * i])

            if 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
                m = max(m, nums[2 * i + 1])

        return m
