class MinStack:
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if self.min == None:
            self.min = val
        elif val < self.min:
            self.min = val
        self.stack.append(val)

    def pop(self) -> None:
        curr = self.stack.pop()
        if self.stack == []:
            self.min = None
        elif curr == self.min:
            # How else would one even do this?
            # This becomes amortized O(1) time, I *think*.
            self.min = min(self.stack)
        
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