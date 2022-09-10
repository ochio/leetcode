class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join([str(_) for _ in digits])
        num = int(s) + 1
        return list(str(num))
