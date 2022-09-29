from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for i in range(len(nums)):
            d[nums[i]] += 1

        m = None
        for key in d.keys():
            if m is None:
                m = key
                continue

            if d[key] > d[m]:
                m = key

        return m
