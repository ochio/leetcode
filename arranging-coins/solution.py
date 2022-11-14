class Solution:
    def arrangeCoins(self, n: int) -> int:
        def f(n):
            return n * (n + 1) / 2

        l = 1
        r = n

        while l <= r:
            m = (l + r) // 2
            if f(m) < n:
                l = m + 1
            elif f(m) > n:
                r = m - 1
            else:
                return m
        return r
