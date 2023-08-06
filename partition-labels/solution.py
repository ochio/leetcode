class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}

        for i in range(len(s)):
            d[s[i]] = i

        start = 0
        last_position = 0

        ans = []

        for i, c in enumerate(s):
            last_position = max(d[c], last_position)

            if i == last_position:
                cur_length = last_position - start + 1
                ans.append(cur_length)
                start = i + 1

        return ans
