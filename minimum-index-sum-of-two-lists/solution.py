from collections import defaultdict


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        self.d = defaultdict(list)
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    self.d[i + j].append(list1[i])

        j = min([k for k in self.d.keys()])
        return self.d[j]
