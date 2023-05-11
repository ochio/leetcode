class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        l = max(len(v1), len(v2))
        i = 0

        while i < l:
            if len(v1) <= i:
                n1 = 0
            else:
                n1 = int(v1[i])
            if len(v2) <= i:
                n2 = 0
            else:
                n2 = int(v2[i])

            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1
            i += 1

        return 0
