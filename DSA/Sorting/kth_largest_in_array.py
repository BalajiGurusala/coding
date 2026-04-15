'''
Kth Largest In An Array
Given an array of integers, find the k-th largest number in it.

Input:
{
"numbers": [5, 1, 10, 3, 2],
"k": 2
}
Output:
5

Tier,Algorithm,Time Complexity,Space Complexity,When to use?
Bronze,Sort and return arr[-k],O(NlogN),O(1) or O(N),"Baseline, lazy evaluation."
Silver,Min-Heap (Size K),O(Nlogk),O(k),"Standard Interview Answer. 
Safe, streaming-friendly."
Gold,QuickSelect,O(N) average,O(1),"The ""Final Boss"" answer."
'''
def kth_largest_in_an_array_minheap(numbers, k):
    """
    Args:
     numbers(list_int32)
     k(int32)
    Returns:
     int32
    """
    # Write your code here.
    import heapq
    
    heapq.heapify(numbers)
    
    while len(numbers) > k:
        heapq.heappop(numbers)
        
    if len(numbers) == k:    
        return numbers[0]

'''
The below solution is an improvement over the above solution
where leverage quick select algorithm to find the kth largest element in the array. 
The time complexity of this algorithm is O(n) on average and O(n^2) in the worst case. 
The space complexity is O(1) for the in-place partitioning.
'''

def kth_largest_in_an_array_quick_select(numbers, k):
    """
    Args:
     numbers(list_int32)
     k(int32)
    Returns:
     int32
    """
    # Write your code here.
    import random
    def quickSelect(numbers, k, start, end):
        
        left = start
        pivot = random.randint(start, end)
        numbers[start],numbers[pivot] = numbers[pivot],numbers[start]
    
        for right in range(start+1, end+1):
            if numbers[right] > numbers[start]:
                continue
            else:
                left += 1
                numbers[left], numbers[right] = numbers[right],numbers[left]
                
        numbers[left], numbers[start] = numbers[start],numbers[left]
        if k == left:
            return numbers[left]
        elif k < left:
            return quickSelect(numbers, k, start, left-1)
        else:
            return quickSelect(numbers, k, left+1, end)
            
    
    return quickSelect(numbers, len(numbers)-k, 0, len(numbers)-1)