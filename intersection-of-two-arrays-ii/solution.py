from collections import defaultdict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(int)
        d2 = defaultdict(int)
        for i in range(len(nums1)):
            d[nums1[i]] += 1
        for i in range(len(nums2)):
            d2[nums2[i]] += 1

        ans = []
        for k in d:
            if d[k] > 0 and d2[k] > 0:
                c = min(d[k], d2[k])
                l = [k] * c
                ans += l

        return ans
