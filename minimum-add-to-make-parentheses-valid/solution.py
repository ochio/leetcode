class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for i in range(len(s)):
            stack.append(s[i])

            while True:
                if len(stack) < 2:
                    break
                s1 = stack.pop()
                s2 = stack.pop()

                ok = s1 == ")" and s2 == "("

                if not ok:
                    stack.append(s2)
                    stack.append(s1)
                    break

        return len(stack)
