class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        result = []
        P = [i + 1 for i in range(m)]

        for q in queries:
            i = P.index(q)
            result.append(i)
            tmp = P[i]
            for j in range(i, 0, -1):
                P[j] = P[j-1]
            P[0] = tmp

        return result
