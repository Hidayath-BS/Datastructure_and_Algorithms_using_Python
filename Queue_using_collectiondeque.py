from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.popleft if self.queue else "queue is empty"
    
    def front(self):
        return self.queue[0] if self.queue else "queue is empty"
    
    def is_empty(self):
        return not self.queue
    
    def size(self):
        return len(self.queue)
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
print(q.front())
