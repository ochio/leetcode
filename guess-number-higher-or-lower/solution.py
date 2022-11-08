# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        m = (l + r) // 2
        while guess(m) != 0:
            f = guess(m)
            if f == -1:
                r = m - 1
            if f == 1:
                l = m + 1
            m = (l + r) // 2
        return m
