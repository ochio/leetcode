class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        m_a = m
        m_b = n

        for i in range(len(ops)):
            a, b = ops[i]
            m_a = min(m_a, a)
            m_b = min(m_b, b)
        return m_a * m_b

