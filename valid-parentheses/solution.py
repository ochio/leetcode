class Solution:

    def isValid(self, s: str) -> bool:
        a = []
        for b in s:
            if b == ')' or b == '}' or b == ']':
                if len(a) == 0:
                    return False
                l = a.pop(len(a) - 1)

                f = (l == '(' and b == ')') or (l == '{' and b == '}') or (l == '[' and b == ']')

                if not f:
                    return False
            else:
                a.append(b)

        if len(a) == 0:
            return True
        else:
            return False
