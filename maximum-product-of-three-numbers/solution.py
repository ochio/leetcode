class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        else:
            return max(nums[0] * nums[1] * nums[len(nums) - 1],
                       nums[len(nums) - 1] * nums[len(nums) - 2] * nums[len(nums) - 3])
