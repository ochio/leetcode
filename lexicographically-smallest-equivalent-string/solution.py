class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = {}

        def find(x):
            uf.setdefault(x, x)
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX > rootY:
                uf[rootX] = rootY
            else:
                uf[rootY] = rootX

        for i in range(len(s1)):
            union(s1[i], s2[i])

        res = []
        for c in baseStr:
            res.append(find(c))

        return "".join(res)
