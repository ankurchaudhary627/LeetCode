import heapq

class FreqStack:

    def __init__(self):
        self.frequency = dict()
        self.maxFrequency = 0
        self.groupStack=dict()

    def push(self, val: int) -> None:
        self.frequency[val] = self.frequency.get(val,0)+1
        self.maxFrequency=max(self.maxFrequency,self.frequency[val])
        if self.groupStack.get(self.frequency[val],0):
            self.groupStack[self.frequency[val]].append(val)
        else:
            self.groupStack[self.frequency[val]] = [val]

    def pop(self) -> int:
        # print(self.frequency)
        # print(self.maxFrequency)
        # print(self.groupStack)
        topValue = self.groupStack[self.maxFrequency].pop(-1)
        self.frequency[topValue]-=1
        if not self.groupStack[self.maxFrequency]:
            self.maxFrequency-=1
        return topValue


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()