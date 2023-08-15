from itertools import combinations


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.comb = list(combinations(characters, combinationLength))
        self.i = -1

    def next(self) -> str:
        self.i += 1
        return "".join(self.comb[self.i])

    def hasNext(self) -> bool:
        return self.i + 1 < len(self.comb)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
