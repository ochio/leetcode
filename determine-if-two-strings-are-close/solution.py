class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        d1 = {}
        d2 = {}

        for w in word1:
            if w in d1:
                d1[w] += 1
            else:
                d1[w] = 1

        for w in word2:
            if w not in word1:
                return False
            if w in d2:
                d2[w] += 1
            else:
                d2[w] = 1

        c1 = {}
        c2 = {}
        for k in d1.keys():
            count = d1[k]
            if count in c1:
                c1[count].append(k)
            else:
                c1[count] = [k]

        for k in d2.keys():
            count = d2[k]
            if count in c2:
                c2[count].append(k)
            else:
                c2[count] = [k]

        for k in c1.keys():
            if k not in c2:
                return False
            if len(c1[k]) != len(c2[k]):
                return False

        return True
