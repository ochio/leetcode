class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = []
        nums.sort()

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        l.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1

                        while nums[left] == nums[left - 1] and left < right:
                            left += 1
                    elif total > target:
                        right -= 1
                    else:
                        left += 1
        return l
