class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0, 1]
        for i in range(2, n + 1):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] | 1 << i - 1)
        return res
