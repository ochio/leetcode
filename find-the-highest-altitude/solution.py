class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ary = [0]
        m = 0

        for a in gain:
            t = ary[-1] + a
            ary.append(t)
            m = max(m, t)
        return m