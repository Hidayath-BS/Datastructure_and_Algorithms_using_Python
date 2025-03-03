class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear =-1

    def enqueue(self,data):
        if(self.rear + 1) % self.size == self.front:
            return "queue is full"
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            return "queue is empty"
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear =-1
        else:
            self.front = (self.front + 1) % self.size
        return data
    
    def display(self):
        if self.front ==  -1:
            print("queue is empty")
            return
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.display()
cq.dequeue()
cq.display()