class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ans = False

        def dfs(i, j, k):
            if k == len(word):
                self.ans = True
                return
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return

            tmp, board[i][j] = board[i][j], "-"
            dfs(i + 1, j, k + 1)
            dfs(i - 1, j, k + 1)
            dfs(i, j + 1, k + 1)
            dfs(i, j - 1, k + 1)
            board[i][j] = tmp

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0][0]:
                    dfs(i, j, 0)

        return self.ans
