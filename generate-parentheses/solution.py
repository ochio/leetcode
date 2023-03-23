class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a = []

        def dfs(open, close, s):
            if len(s) == n * 2:
                a.append(s)
                return

            if open < n:
                dfs(open + 1, close, s + "(")
            if open > close:
                dfs(open, close + 1, s + ")")

        dfs(0, 0, "")
        return a
