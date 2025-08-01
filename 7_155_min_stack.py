class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 1000000

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = val if val < self.min else self.min

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()