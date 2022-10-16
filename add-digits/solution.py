class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)

        while True:
            if len(num) == 1:
                return num
            tmp = 0
            for i in range(len(num)):
                tmp += int(num[i])

            num = str(tmp)
