class MinStack:

    def __init__(self):
        self.arr=[]
        
    def push(self, value: int) -> None:
        if not self.arr:
            self.arr.append((value,value))
            
        else:
            self.arr.append((value,min(value,self.arr[-1][1])))
        
    def pop(self) -> None:
        return self.arr.pop()
    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()