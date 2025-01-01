class MinStack:

    def __init__(self):
        self.stack=[]
        self.minSoFarStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minSoFarStack:
            self.minSoFarStack.append(val)
        elif val <= self.minSoFarStack[-1]:
            self.minSoFarStack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minSoFarStack[-1]:
            self.minSoFarStack.pop(-1)
        return self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minSoFarStack[-1] if self.minSoFarStack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()