import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        d = 0
        sq = math.ceil(math.sqrt(num))
        for i in range(1, sq):
            if num % i == 0:
                d += i
                if i * i != num:
                    d += num / i
        return d - num == num
