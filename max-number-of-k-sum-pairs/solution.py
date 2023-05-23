from collections import defaultdict


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        left, right = 0, len(nums)-1
        total = 0

        while left < right:
            if nums[left] + nums[right] == k:
                total += 1
                left += 1
                right -= 1
            elif k <= nums[right]:
                right -= 1
            elif k <= nums[left] + nums[right]:
                right -= 1
            else:
                left += 1
        return total
