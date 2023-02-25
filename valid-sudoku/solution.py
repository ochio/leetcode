class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            t = [False for _ in range(0, 9)]
            for j in range(len(board[0])):
                if board[i][j] == '.': continue
                num = int(board[i][j]) - 1
                if t[num]:
                    return False
                else:
                    t[num] = True

        for i in range(len(board[0])):
            t = [False for _ in range(0, 9)]
            for j in range(len(board)):
                if board[j][i] == '.': continue
                num = int(board[j][i]) - 1
                if t[num]:
                    return False
                else:
                    t[num] = True

        for k in [0, 3, 6]:
            for l in [0, 3, 6]:
                t = [False for _ in range(0, 9)]
                for i in [0, 1, 2]:
                    for j in [0, 1, 2]:
                        if board[i + k][j + l] == '.': continue
                        num = int(board[i + k][j + l]) - 1
                        if t[num]:
                            return False
                        else:
                            t[num] = True
        return True
