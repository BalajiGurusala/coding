'''
Top K Frequent Elements
Given an integer array and a number k, find the k most frequent elements in the array.
Input:
{
"arr": [1, 2, 3, 2, 4, 3, 1],
"k": 2
}
output:
[1, 2] or [1,3] or [2,3]
'''
def find_top_k_frequent_elements(arr, k):
    # Time Complexity: O(n + n log n) = O(n log n), where n is the length of arr
    # Space Complexity: O(n) for the frequency dictionary and result list
    """
    Args:
     arr(list_int32)
     k(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    dict_num = {}
    result = []
    for num in arr:
        if num in dict_num:
            dict_num[num] += 1
        else:
            dict_num[num] = 1
    sorted_dict = sorted(dict_num.items(), key = lambda x: x[1], reverse=True)
    i = 0
    for val, count in sorted_dict:
        result.append(val)
        i += 1
        if (i == k):
            break
    return result


def find_top_k_frequent_elements_improved(arr, k):
    # Time Complexity: O(n + k log n), where n is the length of arr
    # Space Complexity: O(n) for the frequency dictionary and result list
    """
    Args:
     arr(list_int32)
     k(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    dict_num = {}
    for num in arr:
        dict_num[num] = dict_num.get(num,0)+1
        
    result = sorted(dict_num, key = dict_num.get, reverse=True)[:k]
    return result



def find_top_k_frequent_elements_heap(arr, k):
    # Time Complexity: O(n + n log k), where n is the length of arr
    # Space Complexity: O(n) for the frequency dictionary and O(k) for the heap
    """
    Args:
     arr(list_int32)
     k(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    dict_num = {}
    heap = []
    result = []
    import heapq
    for num in arr:
        dict_num[num] = dict_num.get(num,0)+1
    
    for num, freq in dict_num.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    for i in range(len(heap)):
        result.append(heap[i][1])
   
    return result