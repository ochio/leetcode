class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = 10 ** 5
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == target:
                    return target
                elif total > target:
                    right -= 1
                else:
                    left += 1

                if abs(total - target) < abs(n - target):
                    n = total

        return n
