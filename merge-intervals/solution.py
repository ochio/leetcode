class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        s, e = intervals[0][0], intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            cs, ce = intervals[i]
            if cs < s and ce < s:
                s = cs
            if e >= cs and ce >= e:
                e = ce
            elif e < cs:
                res.append([s, e])
                s = cs
                e = ce

        res.append([s, e])
        return res
