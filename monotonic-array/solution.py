class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True

        return all(nums[i - 1] <= nums[i] for i in range(1, len(nums))) or all(
            nums[i - 1] >= nums[i] for i in range(1, len(nums)))

