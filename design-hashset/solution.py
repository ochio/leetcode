class MyHashSet:

    def __init__(self):
        self.s = [None] * 10 ** 7

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        else:
            self.s[key] = True

    def remove(self, key: int) -> None:
        self.s[key] = None

    def contains(self, key: int) -> bool:
        return bool(self.s[key])

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
