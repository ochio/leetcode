from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for i in range(len(s)):
            d[s[i]] += 1

        c = 0
        o = 0
        for k in d:
            c += (d[k] // 2) * 2
            if d[k] % 2 == 1:
                o = 1

        return c + o
