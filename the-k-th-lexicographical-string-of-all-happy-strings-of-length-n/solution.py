class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        letters = ["a", "b", "c"]

        def rec(s):
            if len(s) == n:
                ans.append(s)
                return
            for i in range(len(letters)):
                if s[-1] != letters[i]:
                    rec(s + letters[i])

        for l in letters:
            rec(l)

        if len(ans) < k:
            return ""
        else:
            return ans[k - 1]
