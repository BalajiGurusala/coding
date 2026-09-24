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


#Decision problem approach using a hash set
def two_sum_unsorted_array_hashset(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    seen = set()
    for idx, num in enumerate(numbers):
        new_target = target - num
        if new_target in seen:
            return [numbers.index(new_target), idx]
        seen.add(num)
    return [-1, -1]


if __name__ == "__main__":
    numbers = [5, 3, 10, 45, 1]
    target = 6
    print(two_sum_unsorted_array(numbers, target))
    print(two_sum_unsorted_array_hashset(numbers, target))

    numbers = [2, 7, 11, 15]
    target = 9
    print(two_sum_unsorted_array(numbers, target))
    print(two_sum_unsorted_array_hashset(numbers, target))

    numbers = [1, 2, 3, 4, 5]
    target = 10
    print(two_sum_unsorted_array(numbers, target))
    print(two_sum_unsorted_array_hashset(numbers, target))