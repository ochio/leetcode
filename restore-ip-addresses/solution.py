class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.a = []

        for a in range(3):
            for b in range(a + 1, min(a + 4, len(s))):
                for c in range(b + 1, min(b + 4, len(s))):
                    for d in range(c + 1, min(c + 4, len(s))):
                        i1 = s[:a + 1]
                        i2 = s[a + 1: b + 1]
                        i3 = s[b + 1: c + 1]
                        i4 = s[c + 1: d + 1]
                        ip = i1 + "." + i2 + "." + i3 + "." + i4

                        if i1 == "" or i2 == "" or i3 == "" or i4 == "":
                            continue

                        if len(i1) + len(i2) + len(i3) + len(i4) != len(s):
                            continue

                        if (len(i1) > 1 and i1.startswith('0')) or (len(i2) > 1 and i2.startswith('0')) or (len(i3) > 1 and i3.startswith('0')) or (len(i4) > 1 and i4.startswith('0')):
                            continue

                        if 0 <= int(i1) <= 255 and 0 <= int(i2) <= 255 and 0 <= int(i3) <= 255 and 0 <= int(i4) <= 255:
                            self.a.append(ip)

        return self.a
