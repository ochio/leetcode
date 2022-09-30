class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        pointer = len(columnTitle)
        alp = [chr(i) for i in range(65, 91)]
        sum = 0

        for i in range(len(columnTitle)):
            char = columnTitle[i]
            n = alp.index(char)
            sum += (26 ** (pointer - 1)) * (n + 1)
            pointer -= 1

        return sum
