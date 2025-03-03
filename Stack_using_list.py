class Stack:
    def __init__(self):
        self.stack = []

    def push(self,  data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "stack is empty"
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        print("stack (top -> bottom):", self.stack[::-1])

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("popped", s.pop())
print("top element", s.peek())
print("stack size", s.size())