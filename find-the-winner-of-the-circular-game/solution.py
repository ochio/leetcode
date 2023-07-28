from collections import deque


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        d = deque()

        for i in range(1, n + 1):
            d.append(i)

        c = 0
        while len(d) != 1:
            t = d.popleft()
            c += 1
            if c == k:
                c = 0
                continue
            else:
                d.append(t)

        return d[0]
