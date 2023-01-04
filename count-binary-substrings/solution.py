class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        l = [1]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                l[-1] += 1
            else:
                l.append(1)

        c = 0
        for j in range(1, len(l)):
            c += min(l[j], l[j - 1])

        return c
