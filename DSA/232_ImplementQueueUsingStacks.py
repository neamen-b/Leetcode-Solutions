'''
Implementation using a deque
'''

from collections import deque

class MyQueue:

    def __init__(self):
        self.queue = deque()
    
    def push(self, x: int) -> None:
        self.queue.append(x)
    
    def pop(self) -> int:
        return self.queue.popleft()

    def peek(self) -> int:
        return self.queue[0]

    def isEmpty(self) ->None:
        return True if len(self.queue) == 0 else False
    
    def showValues(self) -> None:
        if len(self.queue) == 0:
            return None
        
        for i in range(len(self.queue)):
            print(self.queue[i])

def createQueue() -> MyQueue:
    return MyQueue() 

queue = createQueue()
queue.push(1)
queue.showValues()

# Implementation using stacks
# Does not work, you are supposed to pop from 

class Queue:
    def __init__ (self):
        self.enqueue = []
        self.unqueu = []
    
    def push(self, x: int) -> None:
        self.enqueue.append(x)
    
    def peek(self) -> int:
        if len(self.unqueu) == 0:
            # Copy over elements from enqueue in reverse
            self.moveElements()
        return self.unqueu[-1]
    
    def pop(self) -> int:
        if len(self.unqueu) == 0:
            # Copy over elements from enqueue in reverse
            self.moveElements()
        return self.unqueu.pop()

    def empty(self) -> bool:
        return True if len(self.unqueu) == 0 and len(self.enqueue) == 0 else False
    
    def moveElements(self) -> None:
        if len(self.unqueu) == 0 and len(self.enqueue) == 0:
            return -1
        while self.enqueue:
            self.unqueu.append(self.enqueue.pop())

    