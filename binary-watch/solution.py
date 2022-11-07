class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for h in range(0, 12):
            for m in range(0, 60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    if m < 10:
                        time = f'{h}:0{m}'
                    else:
                        time = f'{h}:{m}'
                    ans.append(time)
        return ans
