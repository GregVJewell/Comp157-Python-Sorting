from heapq import heappush, heappop

def heapSort(iterable):
  # Create Container for Heap
  heap = []

  # Push Values from input onto Heap
  for value in iterable:
    heappush(heap, value)

  # Pop Heap until empty, resulting in sorted return
  return [heappop(heap) for i in range(0, len(heap))]