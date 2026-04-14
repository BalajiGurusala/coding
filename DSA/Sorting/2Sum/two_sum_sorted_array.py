"""
Given an array sorted in non-decreasing order and a target number, find the indices of the 
two values from the array that sum up to the given target number.
{
"numbers": [1, 2, 3, 5, 10],
"target": 7
}
Output:
[1, 3]
"""

# The Below solution is more efficient for sorted array with O(n) time complexity and O(1) space complexity. 
def pair_sum_sorted_array_two_pointer(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    left = 0
    right = len(numbers)-1
    while left < right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            return [left, right]
        
    return [-1, -1]

# This is an alternative solution using a dictionary to store the indices of the numbers.
#This requires addtional space complexity of O(n) but it suits for unsorted array as well. 
def pair_sum_sorted_array_dict(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    dict_num = {}
    
    for idx, num in enumerate(numbers):
        new_target = target - num
        if new_target in dict_num:
            return [dict_num[new_target], idx]
        else:
            dict_num[num] = idx
        
    return [-1, -1]

# This is another alternative solution using binary search to find the 
# complement of each number. However this takes o(n log n) time complexity 
# due to the binary search for each element.
def pair_sum_sorted_array_binary_search(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    def binary_search(numbers, target, start, end):
        if end >= start:
            mid = (end + start)//2
            if numbers[mid] == target:
                return (True, mid)
            elif target > numbers[mid]:
                return binary_search(numbers, target, mid+1, end)
            else:
                return binary_search(numbers, target, start, mid-1)
        
        return [False, -1]
    
    for idx, num in enumerate(numbers):
        new_target = target - num
        found, idx2 = binary_search(numbers, new_target, idx+1, len(numbers)-1)
        if found:
            return [idx, idx2]
    return[-1, -1]