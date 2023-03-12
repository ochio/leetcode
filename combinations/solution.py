class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        c = []

        def g(t, p):
            if len(t) == k:
                c.append(t)
            for i in range(p + 1, n + 1):
                g(t + [i], i)

        g([], 0)
        return c
