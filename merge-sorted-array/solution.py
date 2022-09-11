class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1

        for k in range(m+n-1, -1, -1):
            if i == -1:
                l = nums2[j]
                j -= 1
            elif j == -1:
                l = nums1[i]
                i -= 1
            else:
                if nums1[i] < nums2[j]:
                    l = nums2[j]
                    j -= 1
                else:
                    l = nums1[i]
                    i -= 1
            nums1[k] = l
        

        
        