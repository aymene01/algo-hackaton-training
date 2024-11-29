class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
    

def print_ll(head):
    current = head

    while current:
        print(current.val)
        current = current.next
    

def reverse_ll(head):
    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev