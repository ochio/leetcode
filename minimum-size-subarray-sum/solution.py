from sys import maxsize


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = maxsize
        left, total = 0, 0

        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                res = min(res, i - left + 1)
                total -= nums[left]
                left += 1
        if res == maxsize:
            return 0
        else:
            return res
