class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        l = sorted(list(s))
        if len(l) < 3:
            return max(l)
        else:
            return l[len(l) - 3]
