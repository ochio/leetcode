class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        m = 0

        for i in range(1, len(points)):
            m = max(points[i][0] - points[i - 1][0], m)

        return m
