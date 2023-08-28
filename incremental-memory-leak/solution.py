class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        i = 1
        while memory1 - i >= 0 or memory2 - i >= 0:
            if memory1 >= memory2:
                memory1 -= i
            else:
                memory2 -= i
            i += 1

        return [i, memory1, memory2]
