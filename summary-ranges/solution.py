class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i, j = 0, 0

        while j < len(nums):
            left = nums[i]
            right = nums[j]

            if j + 1 < len(nums) and right + 1 == nums[j + 1]:
                j += 1
            else:
                if left == right:
                    ans.append(str(left))
                else:
                    tmp = str(left) + "->" + str(right)
                    ans.append(tmp)
                j += 1
                i = j

        return ans
