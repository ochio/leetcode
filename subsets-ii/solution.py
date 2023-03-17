class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        r = []
        nums.sort()

        def rec(i, comb):
            r.append(comb)
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                rec(j + 1, comb + [nums[j]])

        rec(0, [])

        return r
