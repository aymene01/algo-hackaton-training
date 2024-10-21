class MaxHeap:
    def __init__(self) -> None:
        self.heap = []
    
    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)
    
    def extract_max(self):
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return max_value
    
    def _bubble_up(self, idx):
        parent_idx = (idx - 1) // 2
        while idx > 0 and self.heap[idx] > self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def _bubble_down(self, idx):
        smallest = idx
        left, right = idx * 2 + 1, idx * 2 + 2

        if left < len(self.heap) and self.heap[left] > self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] > self.heap[smallest]:
            smallest = right
        
        if smallest != idx:
            self.heap[smallest], self.heap[idx] = self.heap[idx], self.heap[smallest]
            self._bubble_down(smallest)
    
    def heapify(self):
        ...
