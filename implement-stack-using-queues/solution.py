class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        i = len(self.stack) - 1
        if i < 0:
            return None
        else:
            return self.stack.pop(i)

    def top(self) -> int:
        i = len(self.stack) - 1
        if i < 0:
            return None
        else:
            return self.stack[i]

    def empty(self) -> bool:
        i = len(self.stack)
        if i == 0:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
