from queue import Queue
q = Queue(maxsize=5)
q.put(100)
q.put(200)
print(q.qsize())
print(q.get())