class Solution:
    def minFlips(self, target: str) -> int:
        stack = []
        t = target[0]

        for i in range(1, len(target)):
            if target[i] == target[i - 1]:
                t += target[i]
            else:
                stack.append(t)
                t = ""
                t += target[i]

        if t != "":
            stack.append(t)

        if len(stack) == 1:
            if stack[0][0] == "0":
                return 0
            else:
                return 1
        else:
            if stack[0][0] == "0":
                for i in range(len(stack)):
                    if stack[i][0] == "1":
                        return len(stack) - i
            return len(stack)
