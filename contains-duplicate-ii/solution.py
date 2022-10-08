class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in d:
                if i - d[num] <= k:
                    return True
                else:
                    d[num] = i
            else:
                d[num] = i

        return False
