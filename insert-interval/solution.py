class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        r = []
        for interval in sorted(intervals):
            if not r or r[-1][1] < interval[0]:
                r.append(interval)
            else:
                r[-1][1] = max(r[-1][1], interval[1])
        return r
