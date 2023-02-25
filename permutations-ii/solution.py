class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        if len(nums) == 1:
            return [nums]
        else:
            res = []
            for i, val in enumerate(nums):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                rest = self.permuteUnique(nums[:i] + nums[i + 1:])
                for rest_perm in rest:
                    perm = [val] + rest_perm
                    res.append(perm)

            return res
