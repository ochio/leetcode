class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = 0
        for i in jewels:
            for j in stones:
                if i == j:
                    s += 1

        return s