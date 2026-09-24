'''Given an array of integers, return a new array containing the squares of each number, 
sorted in non-decreasing order.
Input:
{
 "numbers": [-4, -1, 0, 3, 10]
}
Output:
[0, 1, 9, 16, 100]
'''

'''
Time Complexity: O(n log n) for the heap and sort-based approaches.
Space Complexity: O(n) for all approaches.
'''
def generate_sorted_array_of_squares_v1(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    heap = []
    import heapq
    result = []
    for num in numbers:
        if num < 0:
            heapq.heappush(heap, -num)
        else:
            heapq.heappush(heap, num)
    
    while len(heap):
        result.append(heapq.heappop(heap)**2)
    return result



def generate_sorted_array_of_squares_v2(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    new_list = []
    for num in numbers:
        new_list.append(num*num)
    new_list.sort()
    return new_list

'''
Time Complexity: O(n) for the two-pointer approach + O(n log n) for the initial sort.
Space Complexity: O(n) for the result array.
'''
def generate_sorted_array_of_squares_v3(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    n = len(numbers)
    result = [0]*n
    left = 0
    right = len(numbers)-1
    numbers.sort()
    for i in range(n-1, -1, -1):
        left_sq = numbers[left]**2
        right_sq = numbers[right]**2
        if  left_sq >= right_sq:
            result[i] = left_sq
            left += 1
        else:
            result[i] = right_sq
            right -= 1
    return result

if __name__ == "__main__":
    numbers = [-4, -1, 0, 3, 10]
    print(generate_sorted_array_of_squares_v1(numbers))
    print(generate_sorted_array_of_squares_v2(numbers))
    print(generate_sorted_array_of_squares_v3(numbers))

    numbers = [-4, -1, 0, 6, 5]
    print(generate_sorted_array_of_squares_v1(numbers))
    print(generate_sorted_array_of_squares_v2(numbers))
    print(generate_sorted_array_of_squares_v3(numbers))
