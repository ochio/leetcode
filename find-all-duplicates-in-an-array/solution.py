from collections import defaultdict


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        a = []

        for n in nums:
            d[n] += 1
            if d[n] == 2:
                a.append(n)

        return a
