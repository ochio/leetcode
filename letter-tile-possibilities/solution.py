import itertools


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        s = set()
        tiles = list(tiles)

        for i in range(1, len(tiles) + 1):
            permutations = itertools.permutations(tiles, i)
            for p in permutations:
                s.add(p)

        return len(s)
