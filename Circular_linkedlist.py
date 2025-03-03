class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = CNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def display(self):
        temp = self.head
        if not temp:
            return
        while True:
            print(temp.data, end="->")
            temp = temp.next
            if temp == self.head:
                break
        print("head")
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.display()