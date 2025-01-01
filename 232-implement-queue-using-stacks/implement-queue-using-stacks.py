class MyQueue:

    def __init__(self):
        self.q = []
        self.temp_q = []
        

    def push(self, x: int) -> None:
        self.q.append(x)
        # print(self.q)

    def pop(self) -> int:
        while self.q:
            self.temp_q.append(self.q.pop(-1))
        front_element = self.temp_q.pop(-1)
        while self.temp_q:
            self.q.append(self.temp_q.pop(-1))
        return front_element

    def peek(self) -> int:
        while self.q:
            self.temp_q.append(self.q.pop(-1))
        front_element = self.temp_q[-1]
        while self.temp_q:
            self.q.append(self.temp_q.pop(-1))
        # print(self.q)
        return front_element

    def empty(self) -> bool:
        # print(self.q)
        return False if self.q else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()