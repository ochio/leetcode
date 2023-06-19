from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        ans = []

        for i in range(len(groupSizes)):
            d[groupSizes[i]].append(i)
            if len(d[groupSizes[i]]) == groupSizes[i]:
                ans.append(d[groupSizes[i]])
                d[groupSizes[i]] = []

        return ans
