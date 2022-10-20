# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            middle = (left + right) // 2

            if isBadVersion(middle):
                right = middle - 1
                continue
            else:
                left = middle + 1
                continue
        return left
