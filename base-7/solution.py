class Solution:
    def convertToBase7(self, num: int) -> str:
        def convert(X):
            if (int(X / 7)):
                return convert(int(X / 7)) + str(X % 7)
            return str(X % 7)

        if num < 0:
            num *= -1
            return '-' + convert(num)
        else:
            return convert(num)
