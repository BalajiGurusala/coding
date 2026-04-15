"""2 Sum In An Array
Given an array and a target number, find the indices of the two values from the array that sum up to the given target number.

{
"numbers": [5, 3, 10, 45, 1],
"target": 6
}

Output:
[0,4]
"""

def two_sum_unsorted_array(numbers, target):
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
            return[dict_num[new_target], idx]
        else:
            dict_num[num] = idx
    return [-1, -1]