class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        c = 0
        tmp = 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                tmp += 1
            else:
                c = max(c, tmp)
                tmp = 1
        return max(c, tmp)
