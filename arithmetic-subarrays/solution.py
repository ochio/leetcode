class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            ary = sorted(nums[l[i]: r[i]+1])

            f = True
            if len(ary) > 1:
                tmp = ary[1] - ary[0]
                for j in range(1, len(ary)):
                    if ary[j] - ary[j-1] != tmp:
                        f = False
                        break
            result.append(f)

        return result
