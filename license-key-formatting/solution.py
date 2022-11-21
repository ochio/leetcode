class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        a = ""
        c = 0
        i = len(s) - 1
        while i >= 0:
            if c < k:
                if s[i] == '-':
                    i -= 1
                    continue
                else:
                    a = s[i] + a
                    c += 1
            else:
                if s[i] == '-':
                    c = 0
                    a = s[i] + a
                else:
                    a = s[i] + '-' + a
                    c = 1
            i -= 1

        j = 0
        while j < len(a):
            if a[j] != '-':
                break
            j += 1

        return a[j:]
