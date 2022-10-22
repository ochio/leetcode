class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        d2 = {}
        ary = s.split()
        if len(ary) != len(pattern):
            return False

        for i in range(len(pattern)):
            c = pattern[i]
            w = ary[i]

            if c not in d:
                d[c] = w
            else:
                if d[c] != w:
                    return False

            if w not in d2:
                d2[w] = c
            else:
                if d2[w] != c:
                    return False
        return True
