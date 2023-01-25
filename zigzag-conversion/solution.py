class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        t = [""] * numRows
        c = 0
        r = False
        for i in range(len(s)):
            idx = c
            print(c, r)
            t[idx] += s[i]
            if r:
                c -= 1
            else:
                c += 1
            if c == numRows - 1:
                r = True
            elif c == 0:
                r = False

        return "".join(t)
