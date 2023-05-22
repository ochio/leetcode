class Solution:
    def compress(self, chars: List[str]) -> int:
        c = 1
        t = chars[0]
        r = ""
        for i in range(1, len(chars)):
            if chars[i] != t:
                if c == 1:
                    r += t
                else:
                    r += t + str(c)

                t = chars[i]
                c = 1
            else:
                c += 1

        if c == 1:
            r += t
        else:
            r += t + str(c)

        for i in range(len(r)):
            chars[i] = r[i]
        del chars[len(r):]

        return len(r)
