class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i, j = 1, 0
        result = [[nums[0]]]

        while i < len(nums):
            if nums[i] == result[j][-1]:
                if j == len(result) - 1:
                    result.append([nums[i]])
                    j += 1
                else:
                    j += 1
                    result[j].append(nums[i])
            else:
                j = 0
                result[j].append(nums[i])

            i += 1

        return result
