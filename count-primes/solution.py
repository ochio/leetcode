class Solution:
    def countPrimes(self, n: int) -> int:

        if n <= 2:
            return 0

        isprime = [True] * n

        isprime[0], isprime[1] = False, False

        for i in range(2, n):
            if not isprime[i]:
                continue

            q = i * 2
            while q < n:
                isprime[q] = False
                q += i

        return sum(isprime)
