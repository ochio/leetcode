import math


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        for x, y, r in queries:
            c = 0
            for px, py in points:
                d = math.sqrt(math.pow(x-px, 2) + math.pow(y-py, 2))
                if d <= r:
                    c += 1
            result.append(c)

        return result
