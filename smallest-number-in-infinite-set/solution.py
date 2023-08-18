import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self.l = [i for i in range(1, 1001)]
        self.s = set(self.l)

    def popSmallest(self) -> int:
        o = heapq.heappop(self.l)
        self.s.remove(o)
        return o

    def addBack(self, num: int) -> None:
        if not num in self.s:
            heapq.heappush(self.l, num)
            self.s.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
