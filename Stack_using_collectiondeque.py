from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()
    def push(self, data):
        self.stack.append(data)
    def pop (self):
        return self.stack.pop() if self.stack else "stack is empty"
    def peek(self):
        return self.stack[-1] if self.stack else "stack is empty"
    def is_empty(self):
        return not self.stack
    def size(self):
        return len(self.stack)

s =  Stack()
s.push(1)
s.push(2)
print(s.pop())
print(s.peek())