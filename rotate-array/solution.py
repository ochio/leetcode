class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = []
        l = len(nums)

        for i in range(l):
            tmp.append(nums[(i + l - (k % l)) % l])

        for i in range(l):
            nums[i] = tmp[i]
