class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = 10 ** 5 * -1
        cnt = 0

        for l, r in intervals:
            if l < prev:
                cnt += 1
                if prev < r:
                    continue
            prev = r

        return cnt
