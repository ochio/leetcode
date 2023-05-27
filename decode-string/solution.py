class Solution:
    def decodeString(self, s: str) -> str:
        n = 0
        c = ""
        stack = []

        for i in range(len(s)):
            if s[i].isdigit():
                n = n * 10 + int(s[i])
            elif s[i] == "[":
                stack.append(n)
                stack.append(c)
                n = 0
                c = ""
            elif s[i] == "]":
                p_c = stack.pop()
                p_n = stack.pop()
                c += p_c * p_n
            else:
                c += s[i]

        return c
