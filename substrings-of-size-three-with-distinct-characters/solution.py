class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0

        left = 0
        ans = 0

        for right in range(2, len(s)):
            t = set(list(s[left : right + 1]))

            if len(t) == 3:
                ans += 1

            left += 1

        return ans
