class Solution:
    def isHappy(self, n: int) -> bool:
        SQUARE = dict([(c, int(c) ** 2) for c in "0123456789"])
        s = set()
        while (n > 1) and (n not in s):
            s.add(n)
            n = sum(SQUARE[d] for d in str(n))
        return n == 1
