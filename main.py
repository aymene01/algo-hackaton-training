from data_structures.heaps.max_heap import MaxHeap
from data_structures.heaps.heap_sort import heap_sort

max_heap = MaxHeap()

max_heap.insert(10)
max_heap.insert(1)
max_heap.insert(30)

print(max_heap.extract_max())

print(heap_sort([1, 2, 1, 90, 34, 100]))