class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        L = 0
        W = 0

        for i in range(1, area):
            if area / i < i:
                break
            if area % i == 0:
                L = area // i
                W = i
        return [L, W]
