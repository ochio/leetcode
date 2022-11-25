class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            p = nums2.index(nums1[i])
            self.f = True
            for j in range(p + 1, len(nums2)):
                if nums1[i] < nums2[j]:
                    ans.append(nums2[j])
                    self.f = False
                    break
            if self.f:
                ans.append(-1)
        return ans
