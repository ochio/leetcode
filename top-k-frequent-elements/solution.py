from collections import defaultdict
from functools import cmp_to_key


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def cmp(a, b):
            if d[a] == d[b]:
                return 0
            return -1 if d[a] < d[b] else 1

        def cmpnum(a, b):
            return cmp(a, b)
        d = defaultdict(int)

        for n in nums:
            d[n] += 1

        keys = list(set(nums))

        return sorted(keys, key=cmp_to_key(cmpnum), reverse=True)[:k]
