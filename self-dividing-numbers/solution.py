class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        a = []
        for i in range(left, right + 1):
            j = str(i)

            f = True
            for k in j:
                l = int(k)
                if l == 0:
                    f = False
                    break
                if i % l != 0:
                    f = False
                    break
            if f:
                a.append(i)

        return a
