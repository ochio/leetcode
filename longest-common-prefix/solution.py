class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        s = strs[0]
        for i in range(len(s)):
            t = s[0:i+1]
            for j in range(len(strs)):
                if not strs[j].startswith(t):
                    return ans
            ans = t
        return ans
