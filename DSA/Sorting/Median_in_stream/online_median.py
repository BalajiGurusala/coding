'''
Online Median

Given a list of numbers, the task is to insert these numbers into a stream 
and find the median of the stream after each insertion. If the median is a 
non-integer, consider it’s floor value.
The median of a sorted array is defined as the middle element when the 
number of elements is odd and the mean of the middle two elements 
when the number of elements is even.


Input:
{
"stream": [3, 8, 5, 2]
}
output:
[3, 5, 5, 4]

Iteration	Stream	Sorted Stream	Median
1	[3]	[3]	3
2	[3, 8]	[3, 8]	(3 + 8) / 2 => 5
3	[3, 8, 5]	[3, 5, 8]	5
4	[3, 8, 5, 2]	[2, 3, 5, 8]	(3 + 5) / 2 => 4
'''
def online_median(stream):
    """
    Args:
     stream(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    heap1 = []
    heap2 = []
    result = []
    import heapq
    
    for num in stream:
        if len(heap2) == 0:
            heapq.heappush(heap2, num)
        else:
            if num > heap2[0]:
                heapq.heappush(heap2, num)
            else:
                heapq.heappush(heap1, -num)
                
        if (len(heap1)-len(heap2) ==2):
            heapq.heappush(heap2, -1 * heapq.heappop(heap1))
            
        elif (len(heap2) - len(heap1) == 2):
            heapq.heappush(heap1, -1 * heapq.heappop(heap2))
        
        if len(heap1) == len(heap2):
            result.append(((-1 * heap1[0]) + heap2[0])//2)
        elif (len(heap2) > len(heap1)):
            result.append(heap2[0])
        else:
            result.append(-1*heap1[0])

    return result

'''
Time Complexity: O(Nlog N) total, O(log N) per insertion.
Space Complexity: O(N) to store the elements in the heaps.
'''

def online_median_optimal(stream):
    """
    Args:
     stream(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    maxheap = []
    minheap = []
    result = []
    median = 0
    import heapq
    
    for num in stream:
        if num > median:
            heapq.heappush(minheap, num)
            
            if (len(minheap)-len(maxheap) == 2):
                heapq.heappush(maxheap, -1 * heapq.heappop(minheap))

        else:
            heapq.heappush(maxheap, -num)
            
            if (len(maxheap)-len(minheap) == 2):
                heapq.heappush(minheap, -1* heapq.heappop(maxheap))

        if len(minheap) == len(maxheap):
            median = (-1*maxheap[0] + minheap[0])//2
        
        elif len(maxheap) > len(minheap):
            median = (-1 * maxheap[0])
        else:
            median = minheap[0]
            
        result.append(median)
                
    return result