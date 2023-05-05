from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1
        a = []
        for k in d.keys():
            if d[k] == 1:
                a.append(k)
        return a
