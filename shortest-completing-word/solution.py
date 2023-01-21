import re
from collections import defaultdict


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_plate = licensePlate.lower()
        l = re.findall(r'[a-zA-Z]+', license_plate)
        c = "".join(l)

        t = defaultdict(int)

        for i in range(len(c)):
            t[c[i]] += 1

        a = []
        m = 1001
        for i in range(len(words)):
            f = True
            d = t.copy()
            for j in range(len(words[i])):
                d[words[i][j]] -= 1
            for k in d.keys():
                if d[k] > 0:
                    f = False
                    break
            if f:
                m = min(m, len(words[i]))
                a.append(words[i])

        for i in a:
            if len(i) == m:
                return i
