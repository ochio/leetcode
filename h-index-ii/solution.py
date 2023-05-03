class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n - 1
        while left < right:
            middle = (right + left) // 2
            if n - middle == citations[middle]:
                return n - middle
            elif n - middle < citations[middle]:
                right = middle - 1
            else:
                left = middle + 1

        return n - left
