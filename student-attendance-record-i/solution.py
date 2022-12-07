class Solution:
    def checkRecord(self, s: str) -> bool:
        a_count = 0
        l_count = 0
        f = False
        for i in s:
            if i == 'P':
                l_count = 0
                continue
            elif i == 'A':
                a_count += 1
                l_count = 0
            else:
                l_count += 1
            if l_count >= 3:
                f = True
                break
        return not f and a_count < 2
