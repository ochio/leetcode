class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        tmp = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                tmp.append(mat[i][j])

        ans = []
        t = []
        if r * c != len(tmp):
            return mat

        for k in range(r * c):
            if len(t) == c:
                ans.append(t)
                t = [tmp[k]]
            else:
                t.append(tmp[k])
        if len(t) > 0:
            ans.append(t)
        return ans
