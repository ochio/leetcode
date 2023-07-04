class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        e = [False] * n

        for f, t in edges:
            g[f].append(t)

        for i in range(len(g)):
            for j in g[i]:
                e[j] = True

        result = []
        for i in range(len(e)):
            if not e[i]:
                result.append(i)

        return result
