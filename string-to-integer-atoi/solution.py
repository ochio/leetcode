class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        n = ""

        for i in range(len(s)):
            if i == 0 and (s[i] == '-' or s[i] == '+'):
                n += s[i]
                continue

            if s[i].isdigit():
                n += s[i]
            else:
                break

        try:
            int(n)
        except ValueError:
            return 0
        else:
            if -2 ** 31 <= int(n) <= 2 ** 31 - 1:
                return int(n)
            else:
                if int(n) < 0:
                    return -2 ** 31
                else:
                    return 2 ** 31 - 1
