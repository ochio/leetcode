class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        n = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        a = []

        def dfs(i, s):
            if len(s) == len(digits):
                a.append(s)
                return
            for j in n[digits[i]]:
                dfs(i + 1, s + j)

        dfs(0, "")

        return a
