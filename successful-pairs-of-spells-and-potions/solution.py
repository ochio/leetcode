class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []

        for i in range(len(spells)):
            left = 0
            right = len(potions) - 1
            while left <= right:
                middle = (left + right) // 2

                if potions[middle] * spells[i] >= success:
                    right = middle - 1
                elif potions[middle] * spells[i] < success:
                    left = middle + 1

            ans.append(len(potions) - 1 - right)

        return ans
