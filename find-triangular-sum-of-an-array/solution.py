class Solution:
    def triangularSum(self, nums: List[int]) -> int:

        while len(nums) != 1:
            tmp = []
            for i in range(1, len(nums)):
                tmp.append((nums[i-1] + nums[i]) % 10)
            nums = tmp
        else:
            return nums[0]
