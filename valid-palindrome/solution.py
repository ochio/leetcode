class Solution:
    def isPalindrome(self, s: str) -> bool:
        replaced = ''
        s = s.lower()
        for str in s:
            if str.isalnum():
                replaced += str
            else:
                pass

        return replaced == replaced[::-1]
