class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        o = ""
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            elif s[i] == "+" or s[i] == "-" or s[i] == "*" or s[i] == "/":
                o = s[i]
                i += 1
            else:
                t = ""
                while i < len(s) and 48 <= ord(s[i]) <= 57:
                    t += s[i]
                    i += 1
                if o == "+" or o == "":
                    stack.append(int(t))
                elif o == "-":
                    t = int(t) * -1 if o == "-" else int(t)
                    stack.append(t)
                elif o == "*":
                    stack[-1] *= int(t)
                elif o == "/":
                    if stack[-1] < 0:
                        tmp = stack[-1] * -1
                        tmp //= int(t)
                        stack[-1] = tmp * -1
                    else:
                        stack[-1] //= int(t)
        return sum(stack)
