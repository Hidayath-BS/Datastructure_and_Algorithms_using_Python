class ListNode:
    def __init__(self,  val=0):
        self.val = val
        self.next = None

def has_cycle(head):
    slow, fast =  head, head
    while fast and fast.next:
        slow =  slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = head.next
print("cycle detection", has_cycle(head))