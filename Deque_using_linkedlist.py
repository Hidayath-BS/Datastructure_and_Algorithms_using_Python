class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = self.rear = None

    def append(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node

    def appendleft(self, data):
        new_node = Node(data)
        if not self.front:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def pop(self):
        if not self.rear:
            return "Deque is empty "
        data = self.rear.data
        self.rear = self.rear.prev
        if self.rear:
            self.rear.next = None
        else:
            self.front = None
        return data
    
    def popleft(self):
        if not self.front:
            return "deque is empty"
        data = self.front.data
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None
        return data
    
dq = Deque()
dq.append(10)
dq.appendleft(5)
print(dq.pop())
print(dq.popleft())