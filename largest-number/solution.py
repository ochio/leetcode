from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            if int(x + y) < int(y + x):
                return -1
            if int(x + y) > int(y + x):
                return 1
            return 0

        nums = [str(n) for n in nums]
        nums = sorted(nums, key=cmp_to_key(cmp), reverse=True)
        ans = "0" if nums[0] == "0" else "".join(nums)
        return ans
