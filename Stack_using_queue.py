from queue import LifoQueue
stack = LifoQueue(maxsize=5)
stack.put(100)
stack.put(200)
print(stack.qsize())
print(stack.get())