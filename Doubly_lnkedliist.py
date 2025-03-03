class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinnkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        temp =  self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def delete(self, key):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        if temp is None:
            return
        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev
        if temp == self.head:
            self.head = temp.next
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="<->")
            temp = temp.next
        print("None")

dll = DoublyLinnkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display()
dll.delete(2)
dll.display()
