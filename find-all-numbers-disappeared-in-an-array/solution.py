class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = sorted(list(set(nums)))
        i = 1
        j = 0
        a = []
        while i <= len(nums):
            if j >= len(s):
                a.append(i)
                i += 1
            elif s[j] == i:
                j += 1
                i += 1
            else:
                a.append(i)
                i += 1
        return a
