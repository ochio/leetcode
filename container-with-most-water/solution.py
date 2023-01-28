class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        v = 0
        while left < right:
            h = min(height[left], height[right])
            v = max((right - left) * h, v)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return v
