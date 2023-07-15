class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        result = 0

        for i in range(len(bank)):
            curr = bank[i].count('1')
            result += prev * curr
            prev = prev if curr == 0 else curr

        return result
