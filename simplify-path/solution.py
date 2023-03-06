class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        i, ary = 0, [""] * 3000

        for p in path:
            if p == '.':
                continue
            elif p == "..":
                if i - 1 >= 0:
                    i -= 1
                    ary[i] = ""
            elif p != "":
                ary[i] = p
                i += 1
        s = ""
        for j in range(len(ary)):
            if ary[j] != "":
                s += "/" + ary[j]

        return s if s != "" else "/"
