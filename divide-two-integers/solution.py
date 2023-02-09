class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        isPositive = (dividend < 0 and divisor < 0) or (dividend >= 0 and divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        a = 0
        while dividend >= divisor:
            i = 0
            while dividend >= divisor << (i + 1):
                i += 1
            dividend -= divisor << i
            a += 2 ** i

        if not isPositive:
            a *= -1

        if a > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif a < -2 ** 31:
            return -2 ** 31

        return a
