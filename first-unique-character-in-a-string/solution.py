class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                d[s[i]] = 10 ** 5

        ans = 10 ** 5
        for k in d:
            ans = min(ans, d[k])

        return -1 if ans == 10 ** 5 else ans
