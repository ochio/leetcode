class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = 0
        D = 0
        while True:
            tmp = ""
            for i in range(len(senate)):
                countR = senate[i:].count("R")
                countD = senate[i:].count("D")
                print(R, D, senate[i])
                if R > 0 and senate[i] == "D":
                    R -= 1
                    continue
                elif D > 0 and senate[i] == "R":
                    D -= 1
                    continue

                if senate[i] == "R":
                    R += 1
                else:
                    D += 1
                if senate[i] == "R" and countR == len(senate) - i and countR != 0 and tmp.count("D") == 0:
                    return "Radiant"
                if senate[i] == "D" and countD == len(senate) - i and countD != 0 and tmp.count("R") == 0:
                    return "Dire"
                tmp += senate[i]
            senate = tmp
