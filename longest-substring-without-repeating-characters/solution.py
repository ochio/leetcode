class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        c = 0
        st = ""
        for i in range(len(s)):

            if s[i] in st:
                idx = st.index(s[i]) + 1
                st = st[idx:] + s[i]
            else:
                st += s[i]

            c = max(c, len(st))

        return c
