from collections import deque


class Stack:

    def __init__(self):
        self.stack = deque()
    
    def push(self, x: int) -> None:
        self.stack.append(x)
    
    def pop(self) -> int:
        return self.stack.pop()
    
    def peek(self) ->None:
        return self.stack[-1]
    
    def empty(self):
        return len(self.stack)==0
    

stack = Stack()

stack.push(2)
stack.push(2)
stack.push(2)

print(stack.empty())
    



