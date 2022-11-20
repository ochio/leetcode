class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:]
        ans = ""
        for i in range(len(num)):
            if num[i] == '0':
                ans += "1"
            else:
                ans += "0"

        return int(ans, 2)
