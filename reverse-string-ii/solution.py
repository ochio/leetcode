class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ary = list(s)

        for i in range(0, len(s), 2 * k):
            ary[i:i + k] = reversed(ary[i:i + k])
        return "".join(ary)
