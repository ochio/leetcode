class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0] * n

        for i in range(0, n - 1):
            for j in range(nums[i]):
                if i + j + 1 >= n:
                    break
                if s[i + j + 1] == 0:
                    s[i + j + 1] = s[i] + 1

        return s[-1]
