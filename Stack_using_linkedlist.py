class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.top= None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top  = new_node

    def pop(self):
        if self.top is None:
            return "stack is empty"
        data = self.top.data
        self.top = self.top.next
        return data
    
    def peek(self):
        return self.top.data if self.top else "stack is empty"
    
    def is_empty(self):
        return self.top is None

s = Stack()
s.push(5)
s.push(10)
print(s.pop())

