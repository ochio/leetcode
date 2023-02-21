class Solution:
    def permute(self, nums):

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


a = Solution()
print(a.permute([1, 2, 3]))
