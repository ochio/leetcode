class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        c = 1
        left = 0
        right = 0

        while right < len(nums):
            if nums[right] - nums[left] > k:
                c += 1
                left = right
            right += 1

        return c
