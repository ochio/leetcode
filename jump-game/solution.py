class Solution:
    def canJump(self, nums: List[int]) -> bool:

        c = 0
        r = nums[::-1]
        for i in range(1, len(r)):
            if r[i] <= c:
                c += 1
            elif r[i] > c:
                c = 0

        return c == 0
