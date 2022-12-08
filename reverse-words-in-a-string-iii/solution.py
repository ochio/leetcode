class Solution:
    def reverseWords(self, s: str) -> str:
        ary = s.split()
        for i in range(len(ary)):
            ary[i] = ary[i][::-1]
        return " ".join(ary)
