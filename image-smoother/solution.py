import math


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        t = [[0 for j in range(len(img[0]))] for i in range(len(img))]
        d = [-1, 0, 1]
        for i in range(len(img)):
            for j in range(len(img[0])):
                s = 0
                c = 0
                for k in d:
                    for l in d:
                        if i + k < 0 or i + k >= len(img):
                            continue
                        elif j + l < 0 or j + l >= len(img[0]):
                            continue
                        else:
                            s += img[i + k][j + l]
                            c += 1
                t[i][j] = math.floor(s / c)
        return t
