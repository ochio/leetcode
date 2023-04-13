class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        check = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def dfs(i, j):
            if i < 0 or j < 0 or len(grid) <= i or len(grid[0]) <= j:
                return
            if check[i][j] or grid[i][j] == "0":
                return
            check[i][j] = True
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and check[i][j] == False:
                    dfs(i, j)
                    count += 1

        return count
