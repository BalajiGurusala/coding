'''
Merge K Sorted Linked Lists
Given k linked lists where each one is sorted in the ascending order, 
merge all of them into a single sorted linked list.
Input:
{
"lists": [
[1, 3, 5],
[3, 4],
[7]
]
}
Output:
[1, 3, 3, 4, 5, 7]
'''

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
'''
Space Complexity: O(n) where n is the total number of nodes in all the linked lists.and 
time complexity: O(n log n) where n is the total number of nodes in all the linked lists.'''
def merge_k_lists(lists):
    """
    Args:
     lists(list_LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    heap = []
    import heapq
    for row in range(len(lists)):
        col = lists[row]
        while col:
            heapq.heappush(heap, col.value)
            col = col.next
    head = None
    tail = None
    
    while len(heap):
        result = LinkedListNode(heapq.heappop(heap))
        if head == None:
            head = result
        else:
            tail.next = result
        tail = result
    return head

'''Below algorith has improvement where it takes only time complexity of O(nlogK)
and space complexity of O(n) where n is the total number of elements in all lists.'''

def merge_k_lists_optimal(lists):
    """
    Args:
     lists(list_LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    heap = []
    import heapq
    for row in range(len(lists)):
        col = lists[row]
        if col:
            heapq.heappush(heap, (col.value, row, col))

    head = None
    tail = None
    
    while len(heap):
        val, row, col = heapq.heappop(heap)
        result = LinkedListNode(val)
        if col.next:
            heapq.heappush(heap, (col.next.value, row, col.next))
            
        if head == None:
            head = result
        else:
            tail.next = result
        tail = result
    return head

'''
The below solution is space optimized where we are not creating 
new nodes for the result list but instead we are reusing the existing nodes 
from the input lists. This way we can achieve space complexity of O(1) 
excluding the space used by the heap which is O(k) 
where k is the number of linked lists. 
The time complexity remains O(n log k) where n is the total number of nodes 
in all the linked lists and k is the number of linked lists.
'''
def merge_k_lists_space_optimized(lists):
    """
    Args:
     lists(list_LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    heap = []
    import heapq
    for row in range(len(lists)):
        node = lists[row]
        if node:
            heapq.heappush(heap, (node.value, row, node))

    head = tail = LinkedListNode(0)
    while len(heap):
        val, row, node = heapq.heappop(heap)
        if node.next:
            heapq.heappush(heap, (node.next.value, row, node.next))
        
        tail.next = node
        tail = tail.next
        
    return head.next
