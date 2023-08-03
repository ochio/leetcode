class Solution:
    def partitionString(self, s: str) -> int:
        t = ""
        count = 1

        for c in s:
            if c in t:
                t = c
                count += 1
            else:
                t += c
        return count
