class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        suf = [1] * len(nums)
        pre[0] = nums[0]
        suf[0] = nums[-1]
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i]
        for i in range(1, len(nums)):
            suf[i] = suf[i - 1] * nums[len(nums) - i - 1]

        ans = []
        for i in range(len(nums)):
            if i == 0:
                a = suf[-2]
            elif i == len(nums) - 1:
                a = pre[-2]
            else:
                a = pre[i - 1] * suf[len(nums) - i - 2]
            ans.append(a)
        return ans
