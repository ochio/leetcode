class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        m = 0
        tmp = 0
        while i < len(nums):
            if nums[i] == 1:
                tmp += 1
                m = max(tmp, m)
            else:
                tmp = 0
            i += 1
        return m
