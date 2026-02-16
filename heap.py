import heapq

def heap():
    heap = []

    heapq.heappush(heap, 5)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 8)
    heapq.heappush(heap, 3)
    print("Heap after pushes:", heap)

    smallest = heapq.heappop(heap)
    print("Popped smallest element:", smallest)
    print("Heap after pop:", heap)

    print("Current smallest element (peek):", heap[0])

    # Convert a list into a heap
    data = [7, 2, 9, 4]
    heapq.heapify(data)
    print("Heapified list:", data)

if __name__ == '__main__':
    heap()
