from collections import deque


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        stack = deque()
        i = 1

        u = s[0].upper()
        l = s[0].lower()
        if u == l:
            stack.append(u)
        else:
            stack.append(u)
            stack.append(l)

        while i < len(s):
            u = s[i].upper()
            l = s[i].lower()

            if u == l:
                for _ in range(len(stack)):
                    c = stack.popleft()
                    c += u
                    stack.append(c)
            else:
                for _ in range(len(stack)):
                    c = stack.popleft()
                    for p in [u, l]:
                        stack.append(c + p)

            i += 1

        return list(stack)
