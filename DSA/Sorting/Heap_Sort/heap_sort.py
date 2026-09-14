''' Implement Heap Sort in place '''
''' Time Complexity: O(n log n) '''
''' Space Complexity: O(1) '''

def heap_sort(A, length):
    # Build max heap
    for i in range(length // 2 - 1, -1, -1):
        heapify(A, i, length)

    # Extract elements one by one
    for i in range(length - 1, 0, -1):
        A[i], A[0] = A[0], A[i]  # Swap
        heapify(A, 0, i)

def heapify(A, parent, length):
    largest = parent
    left = 2 * parent + 1
    right = 2 * parent + 2

    if left < length and A[left] > A[largest]:
        largest = left

    if right < length and A[right] > A[largest]:
        largest = right

    if largest != parent:
        A[parent], A[largest] = A[largest], A[parent]
        heapify(A, largest, length)

if __name__ == "__main__":
    A = [7, 5, 3, 1, 4, 2, 6]
    heap_sort(A, len(A))
    print(A)