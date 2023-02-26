class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        i, j = 0, 0
        t, r, b, l = 0, len(matrix[0]) - 1, len(matrix) - 1, 0
        a = [matrix[j][i]]
        to = "r" if len(matrix[0]) >= 2 else "b"
        while len(a) != len(matrix) * len(matrix[0]):
            if to == "r":
                i += 1
                p = matrix[j][i]
                a.append(p)
                if i == r:
                    t += 1
                    to = "b"
            elif to == "b":
                j += 1
                p = matrix[j][i]
                a.append(p)
                if j == b:
                    r -= 1
                    to = "l"
            elif to == "l":
                i -= 1
                p = matrix[j][i]
                a.append(p)
                if i == l:
                    b -= 1
                    to = "t"
            else:
                j -= 1
                p = matrix[j][i]
                a.append(p)
                if j == t:
                    l += 1
                    to = "r"
        return a
