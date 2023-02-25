class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def lower():
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1

            return left if left < len(nums) and nums[left] == target else -1

        def upper():
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1

            return right if 0 <= right and nums[right] == target else -1

        return [lower(), upper()]
