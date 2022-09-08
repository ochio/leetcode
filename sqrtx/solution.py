class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            mid = (r + l) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                r = mid - 1
            else:
                if (mid + 1) ** 2 > x:
                    return mid
                else:
                    l = mid + 1
