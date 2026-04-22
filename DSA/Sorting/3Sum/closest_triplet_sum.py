'''
Given a target number and a list of numbers, find a triplet of numbers from the list such that sum of that triplet is the closest to the target. Return that sum.
Input:
{
"target": 1,
"numbers": [-1, 2, 1, -4]
}
Output:
2
explanation:
The triplet [-1, 2, 1] has the closest sum to the target.
'''
def find_closest_triplet_sum(target, numbers):
    """
    Args:
     target(int32)
     numbers(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    numbers.sort()
    min = float('inf')
    n = len(numbers)
    closest_sum = 0
    for i in range(n-2):
        left = i+1
        right = n-1
        while left < right:
            current_sum = numbers[i]+numbers[left]+numbers[right]
            current_diff = abs(current_sum-target)
            
            if current_sum == target:
                return current_sum
            elif current_diff < min:
                min = current_diff
                closest_sum = current_sum
            
            if current_sum < target:
                left += 1
            else:
                right -= 1
    
    return closest_sum

def find_closest_triplet_sum(target, numbers):
    """
    Args:
     target(int32)
     numbers(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    numbers.sort()
    min = float('inf')
    #global_closest_sum = float('inf')
    global_closest_sum = numbers[0]+numbers[1]+numbers[2]
    n = len(numbers)
    for i in range(n-2):
        current_closest_sum = two_sum(numbers, target, i)
        if current_closest_sum == target:
            return current_closest_sum
            
        if abs(current_closest_sum - target) < abs(global_closest_sum - target):
            global_closest_sum = current_closest_sum
    return global_closest_sum

def two_sum(numbers, target, prev_index):

    left = prev_index+1
    right = len(numbers)-1
    local_min = float('inf')
    #local_closest_sum = float('inf')
    local_closest_sum = numbers[prev_index]+numbers[left]+numbers[right]
    while left < right:
        current_sum = numbers[prev_index]+numbers[left]+numbers[right]
        current_diff = abs(current_sum-target)
        
        if current_sum == target:
            return current_sum
        elif current_diff < local_min:
            local_min = current_diff
            local_closest_sum = current_sum
        
        if current_sum < target:
            left += 1
        else:
            right -= 1
    
    return local_closest_sum