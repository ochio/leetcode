class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total = len(garbage[0])

        for type in ["M", "P", "G"]:
            tmp = 0
            for i in range(1, len(garbage)):
                tmp += travel[i-1]
                if type in garbage[i]:
                    total += garbage[i].count(type)
                    total += tmp
                    tmp = 0

        return total
