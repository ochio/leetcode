class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = []
        n = []

        for num in nums:
            if num > 0:
                p.append(num)
            else:
                n.append(num)

        result = []

        for i in range(len(p)):
            result.append(p[i])
            result.append(n[i])

        return result
