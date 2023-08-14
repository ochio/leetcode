from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        index = deque(range(len(deck)))
        ans = [None] * len(deck)

        for card in deck:
            ans[index.popleft()] = card
            if index:
                i = index.popleft()
                index.append(i)

        return ans
