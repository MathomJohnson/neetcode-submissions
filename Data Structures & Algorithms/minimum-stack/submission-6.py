class MinStack:

    def __init__(self):
        self.stack = []
        self.currMin = None
        

    def push(self, val: int) -> None:
        self.stack.append([val, self.currMin])
        if self.currMin == None:
            self.currMin = val
            print("hi")
        else:
            self.currMin = min(self.currMin, val)
        print(self.currMin)
        

    def pop(self) -> None:
        p = self.stack.pop()
        self.currMin = p[1]

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.currMin
        
