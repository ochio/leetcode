class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        n = len(graph)

        def dfs(i, comb):
            if i == n-1:
                result.append(comb)
                return

            for j in graph[i]:
                dfs(j, comb+[j])

        dfs(0, [0])
        return result
