from collections import defaultdict


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for i in range(len(nums)):
            d[nums[i]] += 1

        keys = sorted(d.keys())
        if len(keys) < 2:
            return 0

        ans = 0
        for k in range(1, len(keys)):
            i = keys[k - 1]
            j = keys[k]
            if j - i > 1:
                continue
            ans = max(ans, d[i] + d[j])

        return ans
