class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ''
        alp = [chr(i) for i in range(65, 91)]

        while columnNumber > 0:
            columnNumber -= 1
            i = columnNumber % 26
            s = alp[i] + s
            columnNumber //= 26

        return s
