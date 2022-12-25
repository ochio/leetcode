class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[0:k])
        m = sum(nums[0:k])
        start = 1
        end = k + 1
        while end <= len(nums):
            s = s - nums[start] + nums[end]
            m = max(m, s)
            start += 1
            end += 1
        return m / k
