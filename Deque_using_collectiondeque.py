from collections import deque
dq = deque()
dq.append(10)
dq.append(20)
dq.append(5)
print("deque", dq)
print("popped from front", dq.pop())
print("popped from front", dq.popleft())
print("front element", dq[0])
print("deque size", len(dq))

