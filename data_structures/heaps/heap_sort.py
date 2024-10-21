from .min_heap import MinHeap

def heap_sort(arr): 
    heap = MinHeap()
    heap.heapify(arr)

    sorted_array = []

    for _ in range(len(arr)):
        sorted_array.append(heap.extract_min())
    
    return sorted_array