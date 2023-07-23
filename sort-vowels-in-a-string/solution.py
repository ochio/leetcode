class Solution:
    def sortVowels(self, s: str) -> str:
        tmp = []
        for c in s:
            if c in ("a", "e", "i", "o", "u") or c in ("A", "E", "I", "O", "U"):
                tmp.append(c)
        tmp.sort(reverse=True)
        r = []
        for i in range(len(s)):
            if s[i] in ("a", "e", "i", "o", "u") or s[i] in ("A", "E", "I", "O", "U"):
                r.append(tmp.pop())
            else:
                r.append(s[i])
        return "".join(r)
