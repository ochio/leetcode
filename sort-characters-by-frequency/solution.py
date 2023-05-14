from collections import defaultdict
from functools import cmp_to_key


class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        l = []
        for c in s:
            d[c] += 1
            l.append(c)

        def cmp(a, b):
            if d[a] == d[b]: return -1 if a < b else 1
            return -1 if d[a] < d[b] else 1

        def cmpstr(a, b):
            return cmp(a, b)

        return "".join(sorted(l, key=cmp_to_key(cmpstr), reverse=True))
