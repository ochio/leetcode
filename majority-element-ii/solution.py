from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = len(nums) // 3 + 1
        d = defaultdict(int)
        for v in nums:
            d[v] += 1
        a = []
        
        for k in d.keys():
            if d[k] >= c:
                a.append(k)
        return a
