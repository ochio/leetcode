class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        c = 0

        while i < len(nums) and j < len(nums):
            if nums[j] == 0:
                j += 1
                c += 1
            elif nums[j] != 0:
                nums[i] = nums[j]
                i += 1
                j += 1

        while c > 0:
            nums[len(nums) - c] = 0
            c -= 1
