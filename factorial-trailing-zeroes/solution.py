class Solution:
    def trailingZeroes(self, n: int) -> int:
        def prime_factorize(n):
            a = []
            while n % 2 == 0:
                a.append(2)
                n //= 2
            f = 3
            while f * f <= n:
                if n % f == 0:
                    a.append(f)
                    n //= f
                else:
                    f += 2
            if n != 1:
                a.append(n)
            return a

        five = 0
        two = 0
        for i in range(1, n+1):
            t = prime_factorize(i)
            two += t.count(2)
            five += t.count(5)

        return min(five, two)
