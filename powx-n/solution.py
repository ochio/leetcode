class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(b, e):

            if e == 0:
                return 1
            elif e % 2 == 0:
                return rec(b * b, e / 2)
            else:
                return b * rec(b, e - 1)

        num = rec(x, abs(n))
        return num if n >= 0 else 1 / num
