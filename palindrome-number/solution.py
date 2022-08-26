class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        r = s[::-1]
        return s == r