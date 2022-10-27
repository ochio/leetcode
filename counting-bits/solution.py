class Solution:
    def countBits(self, n: int) -> List[int]:
        a = []
        for i in range(0, n + 1):
            c = bin(i)[2:]
            count = 0
            for j in range(len(c)):
                if c[j] == '1':
                    count += 1
            a.append(count)
        return a
