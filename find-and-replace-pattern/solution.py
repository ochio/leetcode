from collections import defaultdict


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        d = defaultdict(int)
        c = 0
        p = ""

        for i in range(len(pattern)):
            if pattern[i] in d:
                p += d[pattern[i]]
            else:
                d[pattern[i]] = str(c)
                p += d[pattern[i]] + ","
                c += 1

        result = []
        for word in words:
            d = defaultdict(int)
            c = 0
            w = ""
            for i in range(len(word)):
                if word[i] in d:
                    w += d[word[i]]
                else:
                    d[word[i]] = str(c)
                    w += d[word[i]] + ","
                    c += 1
            if w == p:
                result.append(word)

        return result
