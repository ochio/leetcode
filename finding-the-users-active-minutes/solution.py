from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d = defaultdict(set)

        for id, time in logs:
            d[id].add(time)
        result = [0] * k

        for s in d.values():
            c = len(s)
            result[c-1] += 1

        return result
