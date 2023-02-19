class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 1:
            return [nums]
        else:
            res = []
            for i, val in enumerate(nums):
                rest = self.permute(nums[:i] + nums[i + 1:])
                for rest_perm in rest:
                    perm = [val] + rest_perm
                    res.append(perm)

        return res
