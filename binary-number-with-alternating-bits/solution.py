class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)[2:]
        if len(b) == 1:
            return True
        for i in range(1, len(b)):
            if b[i] == b[i - 1]:
                return False
        return True
