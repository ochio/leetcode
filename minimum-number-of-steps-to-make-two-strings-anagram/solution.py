from collections import defaultdict


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for i in range(len(s)):
            d1[s[i]] += 1
            d2[t[i]] += 1

        result = 0
        for k in d1.keys():
            result += d1[k] - d2[k] if d1[k] > d2[k] else 0

        return result
