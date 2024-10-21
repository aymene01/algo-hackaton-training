from heaps.max_heap import MaxHeap

class PriorityQueue:
    def __init__(self) -> None:
        self.queue = MaxHeap()
    
    def append(self, value):
        self.queue.insert(value)
    
    def pop(self):
        return self.queue.extract_max()

    def peek(self):
        return self.queue.peek()

    def is_empty(self):
        return self.queue.is_empty()