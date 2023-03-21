class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        a = [0] * (len(num1) + len(num2))
        p = len(a) - 1

        for n1 in reversed(num1):
            t = p
            for n2 in reversed(num2):
                a[t] += int(n1) * int(n2)
                a[t - 1] += a[t] // 10
                a[t] = a[t] % 10
                t -= 1
            p -= 1

        c = 0
        for n in a:
            if n == 0:
                c += 1
            else:
                break

        return "".join(map(str, a[c:]))
