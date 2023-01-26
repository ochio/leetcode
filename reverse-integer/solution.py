class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            s = "-" + s[:0:-1]
        else:
            s = s[::-1]

        if -2 ** 31 <= int(s) <= 2 ** 31 - 1:
            return int(s)
        else:
            return 0
