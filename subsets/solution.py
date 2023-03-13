class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r = []

        def rec(i, comb):
            r.append(comb)
            for j in range(i, len(nums)):
                rec(j + 1, comb + [nums[j]])

        rec(0, [])

        return r
