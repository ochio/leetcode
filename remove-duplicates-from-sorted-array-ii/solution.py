from collections import defaultdict


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        d = defaultdict(int)

        for i in range(len(nums)):
            if j >= len(nums):
                return i
            d[nums[j]] += 1

            if d[nums[j]] <= 2:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            else:
                while j < len(nums) and d[nums[j]] >= 2:
                    d[nums[j]] += 1
                    j += 1
                if j >= len(nums):
                    return i
                d[nums[j]] += 1
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
