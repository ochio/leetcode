class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = [nums[0]]
        for i in range(1, len(nums)):
            sum.append(sum[i - 1] + nums[i])

        for i in range(len(nums)):
            left = sum[i] - nums[i]
            right = sum[-1] - sum[i]

            if left == right:
                return i

        return -1
