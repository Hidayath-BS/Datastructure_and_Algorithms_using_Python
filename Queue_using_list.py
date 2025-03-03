class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "queue is empty"
    
    def front(self):
        return self.queue[0] if not self.is_empty() else "queue is empty"
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def display(self):
        print("queue (front -> rear):", self.queue)

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

print("Dequeed", q.dequeue())
print("front element", q.front())
print("queue size", q.size())