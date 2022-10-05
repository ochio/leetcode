class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        e = {}
        for i in range(len(s)):
            if t[i] in e and s[i] != e[t[i]]:
                return False

            if s[i] in d and t[i] != d[s[i]]:
                return False

            if s[i] not in d:
                d[s[i]] = t[i]
                e[t[i]] = s[i]

        return True
