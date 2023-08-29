class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        t = [0] * n

        for i in range(k):
            t[i] = max(arr[: i + 1]) * (i + 1)

        for i in range(k, n):
            cur = []
            for j in range(k):
                cur.append(t[i - j - 1] + max(arr[(i - j) : (i + 1)]) * (j + 1))
            t[i] = max(cur)

        return t[-1]
