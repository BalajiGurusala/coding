
'''
Sort All Characters
Given an array of characters, sort the array in-place such that all the characters are in ascending order based on their ASCII values.
Input:
{
"arr": ["a", "s", "d", "f", "g", "*", "&", "!", "z", "y"]
}
Output:
["!", "&", "*", "a", "d", "f", "g", "s", "y", "z"]
'''
from random import random


def sort_array(arr):
    """
    Args:
     arr(list_char)
    Returns:
     list_char
    """
    # Write your code here.
    arr.sort(key = ord)
    return arr


'''Time Complexity: O(n log n) due to the sorting step, 
where n is the number of characters in the array.
Space Complexity: O(1) if the sorting is done in place, 
otherwise O(n) if a new sorted array is created.
ord() function is not used to get the ASCII value of the character for sorting 
as the default sorting of characters in Python is based on their ASCII values.'''
def sort_array_optimal(arr):
    """
    Args:
     arr(list_char)
    Returns:
     list_char
    """
    # Write your code here.)
    arr.sort()
    return arr



def lomutos_partition(arr, start, end):
    left=start
    for right in range(left+1, end+1):
        if arr[right] <= arr[start]:
            left += 1
            arr[left], arr[right] = arr[right], arr[left]
        else:
            continue
    arr[start], arr[left] = arr[left], arr[start]
    return left
    

def quick_sort_helper(arr, start, end):
    
    if start >= end:
        return
    
    pivot = random.randint(start, end)
    arr[start], arr[pivot] = arr[pivot], arr[start]
    
    split_idx = lomutos_partition(arr, start, end)
    
    quick_sort_helper(arr, start, split_idx-1)
    quick_sort_helper(arr, split_idx+1, end)


def sort_array(arr):
    """
    Args:
     arr(list_char)
    Returns:
     list_char
    """
    # Write your code here.
    quick_sort_helper(arr, 0, len(arr)-1)
    return arr



def lomutos_three_way_partition(arr, start, end):
    left=start
    middle=start+1
    right=end
    while middle <= right:
        if arr[middle] == arr[start]:
            middle += 1
            
        elif arr[middle] > arr[start]:
            arr[right], arr[middle] = arr[middle], arr[right]
            right -= 1
        else:
            left += 1
            arr[left], arr[middle] = arr[middle], arr[left]
            middle += 1
            
    arr[start], arr[left] = arr[left], arr[start]
    return left-1, right
    

def quick_sort_helper_optimal(arr, start, end):
    
    if start >= end:
        return
    
    pivot = random.randint(start, end)
    arr[start], arr[pivot] = arr[pivot], arr[start]
    
    split_idx_left, split_idx_right = lomutos_three_way_partition(arr, start, end)
    
    quick_sort_helper_optimal(arr, start, split_idx_left)
    quick_sort_helper_optimal(arr, split_idx_right, end)


def sort_array(arr):
    """
    Args:
     arr(list_char)
    Returns:
     list_char
    """
    # Write your code here.
    quick_sort_helper_optimal(arr, 0, len(arr)-1)
    return arr
