class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l = 0
        r = len(s) - 1
        t = ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O']
        while l < r:
            if s[l] in t and s[r] in t:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            if s[l] not in t:
                l += 1
            if s[r] not in t:
                r -= 1
        return "".join(s)
