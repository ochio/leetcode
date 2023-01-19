class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        a = -1

        for i in range(len(nums)):
            if nums[i] == m:
                a = i
            elif nums[i] * 2 > m:
                return -1

        return a
