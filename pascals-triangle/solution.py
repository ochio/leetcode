class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        p = []

        for i in range(numRows):
            if i == 0:
                p.append([1])
            elif i == 1:
                p.append([1, 1])
            else:
                tmp = []
                l = p[i - 1]
                for j in range(i + 1):
                    if j - 1 < 0 or i - 1 < j:
                        tmp.append(1)
                    else:
                        tmp.append(l[j - 1] + l[j])
                p.append(tmp)

        return p
