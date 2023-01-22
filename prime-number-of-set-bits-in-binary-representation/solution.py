class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        a = 0
        for i in range(left, right + 1):
            b = format(i, 'b')
            c = b.count('1')

            if c == 2:
                a += 1
                continue
            elif c == 0 or c == 1:
                continue

            f = True
            for j in range(2, c):
                if c % j == 0:
                    f = False
                    break
            if f:
                a += 1
        return a
