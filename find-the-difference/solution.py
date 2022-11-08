import collections


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_c = collections.Counter(s)
        t_c = collections.Counter(t)
        for k in t_c:
            if s_c[k] != t_c[k] or k not in s_c:
                return k
