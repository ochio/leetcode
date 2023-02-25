class Solution:
    def countAndSay(self, n: int) -> str:
        def rec(num):
            if num == 1:
                return "1"

            s = rec(num - 1)
            t = s[0]
            c = 1
            a = ""
            for i in range(1, len(s)):
                if s[i] == t:
                    c += 1
                    continue
                else:
                    a += str(c) + str(s[i - 1])
                    t = s[i]
                    c = 1
            if c > 0:
                a += str(c) + str(s[-1])
            return a

        return rec(n)
