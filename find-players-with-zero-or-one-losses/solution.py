from collections import defaultdict


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        person = set()
        l = defaultdict(int)

        for winner, loser in matches:
            person.add(winner)
            person.add(loser)
            l[loser] += 1

        a1 = []
        a2 = []

        for p in person:
            if l[p] == 0:
                a1.append(p)
            elif l[p] == 1:
                a2.append(p)
        a1.sort()
        a2.sort()
        return [a1, a2]
