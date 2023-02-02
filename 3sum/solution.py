class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while True:
                if left == right:
                    break

                n = nums[i] + nums[left] + nums[right]

                if n < 0:
                    left += 1
                elif n > 0:
                    right -= 1
                else:
                    l.append([nums[i], nums[left], nums[right]])
                    break
        return l
