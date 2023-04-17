from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1

        for k in d.keys():
            if d[k] != 3:
                return k