class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c = 0
        s = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                c = 0
            else:
                c += 1
                s += c

        return s
