class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        sum = 0
        tmp = 0
        for i in s:
            if tmp < d[i]:
                sum = sum - tmp
            else:
                sum = sum + tmp
            tmp = d[i]
        sum = sum + tmp
        return sum
