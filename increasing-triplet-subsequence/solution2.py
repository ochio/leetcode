class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        m_r = [0] * len(nums)
        m_r[-1] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            m_r[i] = max(m_r[i + 1], nums[i + 1])

        m_l = nums[0]
        for i in range(1, len(nums)):
            if m_l < nums[i] < m_r[i]:
                return True
            m_l = min(m_l, nums[i])
        return False
