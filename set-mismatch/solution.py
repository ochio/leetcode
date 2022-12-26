from collections import defaultdict


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1

        ans = [0, 0]
        for k in range(1, len(nums) + 1):
            if d[k] == 2:
                ans[0] = k
            elif d[k] == 0:
                ans[1] = k
        return ans
