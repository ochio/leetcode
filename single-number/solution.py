class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t = {}
        for num in nums:
            if num in t:
                t[num] = False
            else:
                t[num] = True

        for k in t.keys():
            if t[k]:
                return k
