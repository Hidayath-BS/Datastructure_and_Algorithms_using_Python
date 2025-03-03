class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.front:
            return "queue is empty"
        
        data = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return data
    
    def front_value(self):
        return self.front.data if self.front else "queue is empty"
    
q = Queue()
q.enqueue(5)
q.enqueue(10)
print(q.dequeue())