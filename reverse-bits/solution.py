class Solution:
    def reverseBits(self, n: int) -> int:
        n = format(n, 'b').zfill(32)[::-1]
        return int(n, 2)
