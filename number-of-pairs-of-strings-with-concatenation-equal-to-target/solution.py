from collections import defaultdict


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1

        count = 0
        for n in nums:
            i = target.find(n)
            if i != 0:
                continue
            d[n] -= 1
            r = target[i + len(n) :]

            if r in d:
                count += d[r]

            d[n] += 1

        return count
