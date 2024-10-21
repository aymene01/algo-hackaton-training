from data_structures.heaps.max_heap import MaxHeap

max_heap = MaxHeap()

max_heap.insert(10)
max_heap.insert(1)
max_heap.insert(30)

print(max_heap.extract_max())