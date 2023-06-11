import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            middle = (left + right) // 2

            count = 0
            for i in range(len(piles)):
                count += math.ceil(piles[i] / middle)

            if count <= h:
                right = middle - 1
            else:
                left = middle + 1

        return left
