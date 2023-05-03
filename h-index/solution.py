class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        a = 0
        for i in range(n):
            a = max(min(n - i, citations[i]), a)
        return a
