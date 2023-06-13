from collections import defaultdict
from functools import cmp_to_key


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(int)

        def cmp(a, b):
            if d[a] == d[b]:
                return -1 if a > b else 1
            return -1 if d[a] > d[b] else 1

        def cmpdict(a, b):
            return cmp(a, b)

        s = set()
        for word in words:
            d[word] += 1
            s.add(word)

        return sorted(list(s), key=cmp_to_key(cmpdict))[:k]
