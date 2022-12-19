class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return (n <= 1 and flowerbed[0] == 0) or (n == 0 and flowerbed[0] == 1)
        i = 0
        while n > 0 and i < len(flowerbed):
            if flowerbed[i] == 0:
                f = (i == 0 and flowerbed[i + 1] == 0) or (i == len(flowerbed) - 1 and flowerbed[i - 1] == 0) or (
                        (i + 1 < len(flowerbed) and i - 1 > 0) and
                        flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0)
                if f:
                    flowerbed[i] = 1
                    n -= 1
            i += 1
        return n == 0
