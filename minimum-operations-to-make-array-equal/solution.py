class Solution:
    def minOperations(self, n: int) -> int:
        avg = 0
        for i in range(n):
            avg += (2 * i) + 1
        avg //= n

        result = 0
        for i in range(n):
            if (2 * i) + 1 > avg:
                result += (2 * i) + 1 - avg
        return result
