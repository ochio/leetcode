class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        t = []
        r = []
        m = [False] * len(strs)

        for i in range(len(strs)):
            tmp = "".join(sorted(strs[i]))
            t.append(tmp)

        for i in range(len(strs)):
            if m[i]:
                continue
            c = [strs[i]]
            m[i] = True
            for j in range(i + 1, len(strs)):
                if t[i] == t[j]:
                    c.append(strs[j])
                    m[j] = True

            r.append(c)

        return r
