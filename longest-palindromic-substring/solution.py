class Solution:
    def longestPalindrome(self, s: str) -> str:

        a = s[0]

        for i in range(1, len(s)):
            j = 1
            t = s[i]
            while i - j >= 0 and i + j < len(s):
                if s[i - j] == s[i + j]:
                    t = s[i - j: i + j + 1]
                    a = t if len(t) > len(a) else a
                    j += 1
                else:
                    break

        for i in range(1, len(s)):
            j = i
            k = i - 1
            while k >= 0 and j < len(s):
                if s[k] == s[j]:
                    t = s[k: j + 1]
                    a = t if len(t) > len(a) else a
                    j += 1
                    k -= 1
                else:
                    break

        return a
