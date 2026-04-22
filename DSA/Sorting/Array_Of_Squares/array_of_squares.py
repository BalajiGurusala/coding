def generate_sorted_array_of_squares(numbers):
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



def generate_sorted_array_of_squares(numbers):
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


def generate_sorted_array_of_squares(numbers):
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