class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        r = [x for x in range(0, len(score))]

        for i in range(len(score)):
            j = sorted_score.index(score[i])
            if j == 0:
                ans = "Gold Medal"
            elif j == 1:
                ans = "Silver Medal"
            elif j == 2:
                ans = "Bronze Medal"
            else:
                ans = str(j + 1)
            r[i] = ans

        return r
