class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s) - 1):
            t = s[:i + 1]
            f = True
            for j in range(i + 1, len(s), i + 1):
                u = s[j:j + i + 1]
                if t != u:
                    f = False
            if f:
                return True
        return False
