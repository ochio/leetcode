class Solution:
    def calPoints(self, operations: List[str]) -> int:
        t = []
        for i in range(len(operations)):
            o = operations[i]
            if o == "D":
                t.append(t[-1] * 2)
            elif o == "C":
                t.pop()
            elif o == "+":
                t.append(t[-1] + t[-2])
            else:
                t.append(int(o))
        return sum(t)
