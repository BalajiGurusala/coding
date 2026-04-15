'''
Kth Largest In A Stream
Given an initial list along with another list of numbers to be appended 
with the initial list and an integer k, return an array consisting of the 
k-th largest element after adding each element from the first list to the second list.

Input:
{
"k": 2,
"initial_stream": [4, 6],
"append_stream": [5, 2, 20]
}
Output:
[5, 5, 6]

'''

def kth_largest(k, initial_stream, append_stream):
    """
    Args:
     k(int32)
     initial_stream(list_int32)
     append_stream(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    heap = []
    result = []
    import heapq
 
    for num in initial_stream:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    for num in append_stream:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
        result.append(heap[0])
        
    return result

'''
The below solution is an improvement over the above solution where we are not adding 
the elements to the heap if they are less than or equal to the kth largest element 
in the heap. This will reduce the number of elements in the heap and thus reduce 
the time complexity of the algorithm. The time complexity of this algorithm is 
O(n log k) where n is the total number of elements in the initial stream and 
append stream and k is the value of k. The space complexity is O(k) for the heap.

'''
def kth_largest_optimal(k, initial_stream, append_stream):
    """
    Args:
     k(int32)
     initial_stream(list_int32)
     append_stream(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    heap = []
    result = []
    import heapq
 
    for num in initial_stream:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    for num in append_stream:
        if len(heap) == k and num <= heap[0]:
            result.append(heap[0])
            continue
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
        result.append(heap[0])
        
    return result
'''
This solution also handles the case where the initial stream is empty and we are 
only getting the append stream.'''

def kth_largest_optimal_empty_first_list(k, initial_stream, append_stream):
    """
    Args:
     k(int32)
     initial_stream(list_int32)
     append_stream(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    heap = []
    result = []
    import heapq
 
    for num in initial_stream:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    for num in append_stream:
        if len(heap) == k and num <= heap[0]:
            result.append(heap[0])
            continue
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
        if len(heap) == k:
            result.append(heap[0])
        
    return result