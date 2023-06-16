class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def convert(num, base):
            result = ''

            while num > 0:
                result = str(num % base) + result
                num //= base

            return str(result)

        for i in range(2, int(n)-1):
            t = convert(int(n), i)
            if t != t[::-1]:
                return False

        return True
